from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from grafana_api.legacy_playlist import LegacyPlaylist


class LegacyPlaylistTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), playlist.get_playlist(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            playlist.get_playlist(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            playlist.get_playlist(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), playlist.get_playlist_items(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            playlist.get_playlist_items(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.get_playlist_items(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), playlist.get_playlist_dashboards(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            playlist.get_playlist_dashboards(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            playlist.get_playlist_dashboards(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), playlist.update_playlist(1, playlist_object))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_playlist_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            playlist.update_playlist(1, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(
            type="test", value="test", order=1, title="test"
        )
        playlist_object: PlaylistObject = PlaylistObject(
            "test", "5m", list([playlist_items])
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            playlist.update_playlist(1, playlist_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200}

        self.assertEqual(None, playlist.delete_playlist(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value.status = 400

        with self.assertRaises(ValueError):
            playlist.delete_playlist(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        playlist: LegacyPlaylist = LegacyPlaylist(grafana_api_model=model)

        call_the_api_mock.return_value.status = 400

        with self.assertRaises(Exception):
            playlist.delete_playlist(1)
