from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.preferences import Preferences


class PreferencesTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_user_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"homeDashboardId": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"homeDashboardId": "test"}),
            preferences.get_current_user_preferences(),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_user_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            preferences.get_current_user_preferences()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Preferences updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            preferences.update_current_user_preferences("test", 0, "test"),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences_no_modified_values(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            preferences.update_current_user_preferences("", None, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            preferences.update_current_user_preferences("test", 0, "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_org_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"homeDashboardId": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"homeDashboardId": "test"}),
            preferences.get_current_org_preferences(),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_org_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            preferences.get_current_org_preferences()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Preferences updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            preferences.update_current_org_preferences("test", 0, "test"),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences_no_modified_values(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            preferences.update_current_org_preferences("", None, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            preferences.update_current_org_preferences("test", 0, "test")
