from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.legacy_alerting import Alerting


class AlertingTestCase(TestCase):

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": "test"})])

        self.assertEqual(list([dict({"id": "test"})]), alerting.get_alerts())

    @patch("src.grafana_api.utils.Utils.call_the_api")
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

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_alerts()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alerts_by_dashboard_ids(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": "test"})])

        self.assertEqual(list([dict({"id": "test"})]), alerting.get_alerts_by_dashboard_ids(list([1, 2])))

    def test_get_alerts_by_dashboard_ids_no_dashboard_ids(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alerts_by_dashboard_ids(list())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alerts_by_dashboard_ids_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_alerts_by_dashboard_ids(list([1, 2]))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alert_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(dict({"id": "test"}), alerting.get_alert_by_id(1))

    def test_get_alert_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alert_by_id(0)

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_alert_by_id_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_alert_by_id(1)

    @patch("src.grafana_api.utils.Utils.call_the_api")
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

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_pause_alert_by_id_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.pause_alert_by_id(1)
