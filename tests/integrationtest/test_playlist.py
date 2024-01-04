import os

from unittest import TestCase

from grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from grafana_api.playlist import Playlist


class PlaylistTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    playlist: Playlist = Playlist(model)

    def test_search_playlist(self):
        self.assertEqual("Test1", self.playlist.search_playlist()[0].get("name"))

    def test_get_playlist(self):
        self.assertEqual("Test1", self.playlist.get_playlist("b86fcd43-4651-4277-841d-90fff83acfa9").get("name"))

    def test_get_playlist_items(self):
        self.assertEqual(
            "tests", self.playlist.get_playlist_items("b86fcd43-4651-4277-841d-90fff83acfa9")[0].get("value")
        )

    def test_a_create_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_id",
            value="653",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test1", "5m", list([playlist_item])
        )
        self.playlist.create_playlist(playlist_object)

        self.assertEqual("Test1", self.playlist.search_playlist()[0].get("name"))

    def test_b_update_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_id",
            value="653",
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
