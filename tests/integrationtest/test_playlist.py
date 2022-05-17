import os
from unittest import TestCase

from src.grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from src.grafana_api.playlist import Playlist


class PlaylistTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        username=os.environ["GRAFANA_USERNAME"],
        password=os.environ["GRAFANA_PASSWORD"],
    )
    playlist: Playlist = Playlist(model)

    def test_get_user(self):
        print(self.playlist.search_playlist())
        #self.assertEqual(8, self.playlist.search_playlist())