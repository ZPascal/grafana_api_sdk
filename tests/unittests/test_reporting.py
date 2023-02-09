from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.reporting import Reporting


class ReportingTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Report was sent"})

        self.assertEqual(None, reporting.send_report(1, emails="test,test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            reporting.send_report(0, emails="")

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            reporting.send_report(1, use_emails_from_report=True)
