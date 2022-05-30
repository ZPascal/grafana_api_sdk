from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.licensing import Licensing


class LicenseTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_check_license_availability(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 200
        call_the_api_mock.return_value.text = "true"

        self.assertEqual(True, licensing.check_license_availability())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_check_license_availability_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 400

        with self.assertRaises(Exception):
            licensing.check_license_availability()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_manually_force_license_refresh(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"jti": "2"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"jti": "2"}), licensing.manually_force_license_refresh())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_manually_force_license_refresh_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            licensing.manually_force_license_refresh()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_remove_license_from_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 200

        self.assertEqual(None, licensing.remove_license_from_dashboard())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_remove_license_from_dashboard_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        mock: Mock = Mock()
        mock.return_value.json = dict()

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            licensing.remove_license_from_dashboard()
