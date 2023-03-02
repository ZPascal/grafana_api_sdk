from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.licensing import Licensing


class LicenseTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_check_license_availability(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value.status = 200
        call_the_api_mock.return_value.data = b"true"

        self.assertEqual(True, licensing.check_license_availability())

    @patch("grafana_api.api.Api.call_the_api")
    def test_check_license_availability_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value.status = 400

        with self.assertRaises(Exception):
            licensing.check_license_availability()

    @patch("grafana_api.api.Api.call_the_api")
    def test_manually_force_license_refresh(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"jti": "2"})

        self.assertEqual(dict({"jti": "2"}), licensing.manually_force_license_refresh())

    @patch("grafana_api.api.Api.call_the_api")
    def test_manually_force_license_refresh_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            licensing.manually_force_license_refresh()

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_license_from_database(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200})

        self.assertEqual(None, licensing.remove_license_from_database())

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_license_from_database_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            licensing.remove_license_from_database()

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_license_from_database_remove_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        licensing: Licensing = Licensing(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            licensing.remove_license_from_database()
