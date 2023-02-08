from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

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

        call_the_api_mock.return_value.data = b"Logged in"

        self.assertEqual(
            None, other_http.renew_login_session_based_on_remember_cookie()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_renew_login_session_based_on_remember_cookie_no_valid_result(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        call_the_api_mock.return_value.data = b""

        with self.assertRaises(Exception):
            other_http.renew_login_session_based_on_remember_cookie()

    @patch("urllib3.PoolManager")
    def test_get_health_status(self, pool_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        pool_mock.return_value.request.return_value.data = b'{"commit": "087143285"}'

        self.assertEqual(dict({"commit": "087143285"}), other_http.get_health_status())

    @patch("urllib3.PoolManager")
    def test_get_health_status_no_valid_result(self, pool_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        pool_mock.return_value.request.return_value.data = b"{}"

        with self.assertRaises(Exception):
            other_http.get_health_status()

    @patch("urllib3.PoolManager")
    def test_get_metrics(self, pool_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        pool_mock.return_value.request.return_value.data = b"test"

        self.assertEqual("test", other_http.get_metrics())

    @patch("urllib3.PoolManager")
    def test_get_metrics_no_valid_result(self, pool_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        other_http: OtherHTTP = OtherHTTP(grafana_api_model=model)

        pool_mock.return_value.request.return_value.data = b""

        with self.assertRaises(Exception):
            other_http.get_metrics()
