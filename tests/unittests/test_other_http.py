from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.other_http import OtherHTTP


class OtherHTTPTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_frontend_settings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"allowOrgCreate": True}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"allowOrgCreate": True}), other_http.get_frontend_settings()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_frontend_settings_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            other_http.get_frontend_settings()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_renew_login_session_based_on_remember_cookie(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.text = "Logged in"

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, other_http.renew_login_session_based_on_remember_cookie()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_renew_login_session_based_on_remember_cookie_no_valid_result(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            other_http.renew_login_session_based_on_remember_cookie()

    @patch("requests.get")
    def test_get_health_status(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"commit": "087143285"}))

        get_mock.return_value = mock

        self.assertEqual(dict({"commit": "087143285"}), other_http.get_health_status())

    @patch("requests.get")
    def test_get_health_status_no_valid_result(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        get_mock.return_value = mock

        with self.assertRaises(Exception):
            other_http.get_health_status()

    @patch("requests.get")
    def test_get_metrics(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.text = "test"

        get_mock.return_value = mock

        self.assertEqual("test", other_http.get_metrics())

    @patch("requests.get")
    def test_get_metrics_no_valid_result(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        mock: Mock = Mock()
        mock.text = ""

        get_mock.return_value = mock

        with self.assertRaises(Exception):
            other_http.get_metrics()
