from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.legacy_alerting import Alerting


class LegacyAlertingTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": "test"})])

        self.assertEqual(list([dict({"id": "test"})]), alerting.get_alerts())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alerts_custom_querystring(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": "test"})])

        self.assertEqual(list([dict({"id": "test"})]), alerting.get_alerts("test"))

    def test_get_alerts_empty_api_string(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alerts("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alerts_by_dashboard_ids(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": "test"})])

        self.assertEqual(
            list([dict({"id": "test"})]),
            alerting.get_alerts_by_dashboard_ids(list([1, 2])),
        )

    def test_get_alerts_by_dashboard_ids_no_dashboard_ids(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alerts_by_dashboard_ids(list())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alerts_by_dashboard_ids_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_alerts_by_dashboard_ids(list([1, 2]))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(dict({"id": "test"}), alerting.get_alert_by_id(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_by_id_upper_case_id_result(self, call_the_api_mock):
        # ISSUE: https://github.com/grafana/grafana/issues/51141
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"Id": "test", "PanelId": 112, "NewStateDate": "2022-06-17T09:34:08Z"}
        )

        self.assertEqual(
            dict(
                {"id": "test", "panelId": 112, "newStateDate": "2022-06-17T09:34:08Z"}
            ),
            alerting.get_alert_by_id(1),
        )

    def test_get_alert_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alert_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_by_id_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_alert_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_pause_alert_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "alert paused"})

        self.assertEqual(None, alerting.pause_alert_by_id(1))

    def test_pause_alert_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.pause_alert_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_pause_alert_by_id_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.pause_alert_by_id(1)
