from django.test import TestCase, Client

from music.models import Artist, Album, Song


class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Example Artist', picture="http://example.com")
        self.client = Client()

    def test_get_all_albums(self):
        response = self.client.get('/artists/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Example Artist')
        self.assertEquals(data[0]['picture'], 'http://example.com')


class TestSongViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name='Example Artist', picture="http://example.com")
        self.album = Album.objects.create(artist=self.artist, title="Example Album")
        self.song = Song.objects.create(album=self.album, title='Test Song')
        self.client = Client()

    def test_search(self):
        response = self.client.get('/songs/?search=Test')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['title'],'Test Song')