from unittest import TestCase
from unittest.mock import MagicMock, patch

from pytest_httpx import HTTPXMock
from httpx import ConnectError

from grafana_api.model import APIModel
from grafana_api.other_http import OtherHTTP


class OtherHTTPTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_frontend_settings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"allowOrgCreate": True})

        self.assertEqual(
            dict({"allowOrgCreate": True}), other_http.get_frontend_settings()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_frontend_settings_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            other_http.get_frontend_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_renew_login_session_based_on_remember_cookie(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Logged in"})

        self.assertEqual(
            None, other_http.renew_login_session_based_on_remember_cookie()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_renew_login_session_based_on_remember_cookie_no_valid_result(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            other_http.renew_login_session_based_on_remember_cookie()

    @patch("httpx.Client")
    def test_get_health_status(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = (
            '{"commit": "087143285"}'
        )

        self.assertEqual(dict({"commit": "087143285"}), other_http.get_health_status())

    @patch("httpx.Client")
    def test_get_health_status_no_valid_result(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = "{}"

        with self.assertRaises(Exception):
            other_http.get_health_status()

    @patch("httpx.Client")
    def test_get_metrics(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = "test"

        self.assertEqual("test", other_http.get_metrics())

    @patch("httpx.Client")
    def test_get_metrics_basic_auth(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = "test"

        self.assertEqual("test", other_http.get_metrics("test", "test"))

    @patch("httpx.Client")
    def test_get_metrics_request_issue(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.side_effect = ConnectError("Test")

        with self.assertRaises(ConnectError):
            other_http.get_metrics()

    @patch("httpx.Client")
    def test_get_metrics_no_valid_result(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = ""

        with self.assertRaises(Exception):
            other_http.get_metrics()

    @patch("httpx.Client")
    def test_get_plugin_metrics(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = "test"

        self.assertEqual("test", other_http.get_plugin_metrics("test"))

    @patch("httpx.Client")
    def test_get_plugin_metrics_basic_auth(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = "test"

        self.assertEqual("test", other_http.get_plugin_metrics("test", "test", "test"))

    @patch("httpx.Client")
    def test_get_plugin_metrics_no_plugin_id(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = ""

        with self.assertRaises(ValueError):
            other_http.get_plugin_metrics("")

    @patch("httpx.Client")
    def test_get_plugin_metrics_no_valid_result(self, httpx_client_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = ""

        with self.assertRaises(Exception):
            other_http.get_plugin_metrics("test")


def test_get_plugin_metrics_http2_support(httpx_mock: HTTPXMock):
    httpx_mock.add_response(text="test")
    model: APIModel = APIModel(
        host="https://test.com", token="test", http2_support=True
    )
    other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

    assert other_http.get_plugin_metrics("test") == "test"
