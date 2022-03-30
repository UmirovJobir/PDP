from django.test import TestCase

from music.models import Artist, Album
from music.serializers import ArtistSerializer, SongSerializer


class TestArtistserializers(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Example Artist', picture="http://example.com")
        self.artist2 = Artist.objects.create(name='Example Artist 2', picture="http://example.com")

    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == 'Example Artist'
        assert data['picture'] == 'http://example.com'


class TestSongSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Example Artist', picture="http://example.com")
        self.album = Album.objects.create(artist=self.artist, title="Example Album")

    def test_is_valid(self):
        data = {
            'title': "Example Song",
            'album': self.album.id,
            'cover': "",
            'source': "http://example.com/music.mp3",
            'listened': 0,
        }

        serializer = SongSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_is_not_valid(self):
        data = {
            'title': "Example Song",
            'album': self.album.id,
            'cover': "",
            'source': "http://example.com/music",
            'listened': 0,
        }

        serializer = SongSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['source'][0]), 'Mp3 file is required')
