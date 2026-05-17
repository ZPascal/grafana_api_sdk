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
    base_uid: str = None
    created_uid: str = None  # UID of the playlist created in test_a

    @classmethod
    def setUpClass(cls) -> None:
        # Clean up any orphaned playlists from previous runs (Test1 and Test2)
        for orphan_name in ("Test1", "Test2"):
            try:
                for pl in cls.playlist.search_playlist(query=orphan_name):
                    try:
                        cls.playlist.delete_playlist(pl.get("uid"))
                    except Exception:
                        pass
            except Exception:
                pass

        # Create the baseline "Test1" playlist that tests expect as pre-existing
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_uid",
            value="tests",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test1", "5m", [playlist_item]
        )
        result = cls.playlist.create_playlist(playlist_object)
        cls.base_uid = result.get("uid")

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.base_uid:
            try:
                cls.playlist.delete_playlist(cls.base_uid)
            except Exception:
                pass

    def test_search_playlist(self):
        self.assertEqual("Test1", self.playlist.search_playlist()[0].get("name"))

    def test_get_playlist(self):
        self.assertEqual(
            "Test1", self.playlist.get_playlist(self.__class__.base_uid).get("name")
        )

    def test_get_playlist_items(self):
        self.assertEqual(
            "dashboard_by_uid",
            self.playlist.get_playlist_items(self.__class__.base_uid)[0].get("type"),
        )

    def test_a_create_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_uid",
            value="tests",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test1", "5m", [playlist_item]
        )
        result = self.playlist.create_playlist(playlist_object)
        self.__class__.created_uid = result.get("uid")

        self.assertEqual("Test1", self.playlist.search_playlist()[0].get("name"))

    def test_b_update_playlist(self):
        playlist_item: PlaylistItemObject = PlaylistItemObject(
            type="dashboard_by_uid",
            value="tests",
            order=1,
            title="Github Integrationtest/Test 1",
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "Test2", "5m", [playlist_item]
        )

        self.playlist.update_playlist(
            self.__class__.created_uid, playlist_object
        )

        updated = self.playlist.get_playlist(self.__class__.created_uid)
        self.assertEqual("Test2", updated.get("name"))

    def test_c_delete_playlist(self):
        self.playlist.delete_playlist(self.__class__.created_uid)

        self.assertEqual(1, len(self.playlist.search_playlist()))
