import os
from unittest import TestCase

from src.grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from src.grafana_api.playlist import Playlist


class PlaylistTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    playlist: Playlist = Playlist(model)

    def test_search_playlist(self):
        self.assertEqual("Test", self.playlist.search_playlist()[0].get("name"))

    def test_get_playlist(self):
        self.assertEqual("Test", self.playlist.get_playlist("ueqwRg6nk").get("name"))

    def test_get_playlist_items(self):
        self.assertEqual("152", self.playlist.get_playlist_items("ueqwRg6nk")[0].get("value"))

    def test_get_playlist_dashboards(self):
        self.assertEqual(152, self.playlist.get_playlist_dashboards("ueqwRg6nk")[0].get("id"))

    def test_a_create_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_id",
            value="152",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test1", "5m", list([playlist_item])
        )
        self.playlist.create_playlist(playlist_object)

        self.assertEqual("Test1", self.playlist.search_playlist()[1].get("name"))

    def test_b_update_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_id",
            value="152",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test2", "5m", list([playlist_item])
        )

        self.playlist.update_playlist(
            self.playlist.search_playlist()[1].get("uid"), playlist_object
        )

        self.assertEqual("Test2", self.playlist.search_playlist()[1].get("name"))

    def test_c_delete_playlist(self):
        self.playlist.delete_playlist(self.playlist.search_playlist()[1].get("uid"))

        self.assertEqual(1, len(self.playlist.search_playlist()))
