from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel
from grafana_api.preferences import Preferences


class PreferencesTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_current_user_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"homeDashboardId": "test"})

        self.assertEqual(
            dict({"homeDashboardId": "test"}),
            preferences.get_current_user_preferences(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_current_user_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            preferences.get_current_user_preferences()

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Preferences updated"})

        self.assertEqual(
            None,
            preferences.update_current_user_preferences("test", 0, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences_no_modified_values(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            preferences.update_current_user_preferences("", None, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_user_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            preferences.update_current_user_preferences("test", 0, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_current_org_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"homeDashboardId": "test"})

        self.assertEqual(
            dict({"homeDashboardId": "test"}),
            preferences.get_current_org_preferences(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_current_org_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            preferences.get_current_org_preferences()

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Preferences updated"})

        self.assertEqual(
            None,
            preferences.update_current_org_preferences("test", 0, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences_no_modified_values(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            preferences.update_current_org_preferences("", None, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_current_org_preferences_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        preferences: Preferences = Preferences(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            preferences.update_current_org_preferences("test", 0, "test")
