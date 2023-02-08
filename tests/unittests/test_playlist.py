from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from grafana_api.playlist import Playlist


class PlaylistTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_search_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"uid": "test"}])

        self.assertEqual(list([{"uid": "test"}]), playlist.search_playlist())

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.search_playlist()

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_playlist_query_defined(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.search_playlist(query="Test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_playlist_limit_defined(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.search_playlist(limit=1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_playlist_query_and_limit_defined(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.search_playlist(query="Test", limit=1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"uid": "test"})

        self.assertEqual(dict({"uid": "test"}), playlist.get_playlist("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_playlist_uid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            playlist.get_playlist("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            playlist.get_playlist("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"uid": "test", "value": "test"}])

        self.assertEqual(
            list([{"uid": "test", "value": "test"}]),
            playlist.get_playlist_items("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_playlist_uid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            playlist.get_playlist_items("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.get_playlist_items("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"uid": "test", "title": "test"}])

        self.assertEqual(
            list([{"uid": "test", "title": "test"}]),
            playlist.get_playlist_dashboards("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_playlist_uid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            playlist.get_playlist_dashboards("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.get_playlist_dashboards("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict({"uid": "test"})

        self.assertEqual(
            dict({"uid": "test"}), playlist.create_playlist(playlist_object)
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_playlist_no_playlist_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            playlist.create_playlist(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            playlist.create_playlist(playlist_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict({"uid": "test"})

        self.assertEqual(
            dict({"uid": "test"}), playlist.update_playlist("test", playlist_object)
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_playlist_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            playlist.update_playlist("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            playlist.update_playlist("test", playlist_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value.status = 200

        self.assertEqual(None, playlist.delete_playlist("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_playlist_uid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value.status = 400

        with self.assertRaises(ValueError):
            playlist.delete_playlist("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: Playlist = Playlist(grafana_api_model=model)

        call_the_api_mock.return_value.status = 400

        with self.assertRaises(Exception):
            playlist.delete_playlist("test")
