from rest_framework import status
from django.db import transaction
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from music.models import Song, Album, Artist
from music.serializers import SongSerializer, AlbumSerializer, ArtistSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.postgres.search import TrigramSimilarity


class SongViewSet(ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['listened', '-listened']
    search_fields = ["title", "album__artist__name", "album__title"]

    def get_queryset(self):
        queryset = Song.objects.all()
        query = self.request.query_params.get('search')
        artist = self.request.query_params.get('artist')
        if query is not None:
            queryset = Song.objects.annotate(similarity=TrigramSimilarity('title', query)
                                             ).filter(similarity__gt=0.1).order_by('-similarity')
        elif artist is not None:
            queryset = Song.objects.annotate(similarity=TrigramSimilarity('artist__name', artist)
                                             ).filter(similarity__gt=0.1).order_by('-similarity')
        return queryset


    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with transaction.atomic():
            song.listened += 1
            song.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset
        songs = songs.order_by('-listened')[:10]
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)


class AlbumViewSet(ReadOnlyModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewSet(ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=["GET"])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)

        return Response(serializer.data)





# class SongsAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(data=serializer.data)
#
