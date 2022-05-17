from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel, PlaylistObject, PlaylistItemObject
from src.grafana_api.playlist import Playlist


class PlaylistTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": 1}]), playlist.search_playlist())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.search_playlist()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_playlist_query_defined(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.search_playlist(query="Test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_playlist_limit_defined(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.search_playlist(limit=1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_playlist_query_and_limit_defined(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.search_playlist(query="Test", limit=1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"id": 1}), playlist.get_playlist(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.get_playlist(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.get_playlist(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_items(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": 1}]), playlist.get_playlist_items(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.get_playlist_items(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_items_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.get_playlist_items(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": 1}]), playlist.get_playlist_dashboards(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.get_playlist_dashboards(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_playlist_dashboards_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.get_playlist_dashboards(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(type="test", value="test", order=1, title="test")
        playlist_object: PlaylistObject = PlaylistObject("test", "5m", list([playlist_items]))

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"id": 1}), playlist.create_playlist(playlist_object))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_playlist_no_playlist_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.create_playlist(None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(type="test", value="test", order=1, title="test")
        playlist_object: PlaylistObject = PlaylistObject("test", "5m", list([playlist_items]))

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.create_playlist(playlist_object)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(type="test", value="test", order=1, title="test")
        playlist_object: PlaylistObject = PlaylistObject("test", "5m", list([playlist_items]))

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"id": 1}), playlist.update_playlist(1, playlist_object))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_playlist_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.update_playlist(1, None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)
        playlist_items: PlaylistItemObject = PlaylistItemObject(type="test", value="test", order=1, title="test")
        playlist_object: PlaylistObject = PlaylistObject("test", "5m", list([playlist_items]))

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.update_playlist(1, playlist_object)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_playlist(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, playlist.delete_playlist(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_playlist_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            playlist.delete_playlist(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_playlist_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), token=MagicMock()
        )
        playlist: Playlist = Playlist(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "error"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            playlist.delete_playlist(1)
