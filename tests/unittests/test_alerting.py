from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import (
    APIModel,
    Alert,
    Silence,
    AlertmanagerConfig,
    AlertmanagerReceivers,
    RulerRule,
    DatasourceRuleQuery,
)
from src.grafana_api.alerting import Alerting


class AlertingTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([dict({"receivers": "test"})]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([dict({"receivers": "test"})]),
            alerting.get_alertmanager_alerts(),
        )

    def test_get_alertmanager_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_alerts("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([]))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_alerts()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alert: Alert = Alert("test", "test", {"test": "test"}, "test", {"test": "test"})

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.create_or_update_alertmanager_alerts([alert]))

    def test_create_or_update_alertmanager_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_alertmanager_alerts([])

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_alerts_no_alerts_created(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alert: Alert = Alert("test", "test", {"test": "test"}, "test", {"test": "test"})

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_alerts([alert])

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_group_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"alerts": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"alerts": "test"}]),
            alerting.get_alertmanager_group_alerts(),
        )

    def test_get_alertmanager_group_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_group_alerts("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_group_alerts_no_group_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_group_alerts()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.delete_alertmanager_silence_by_id("test"))

    def test_delete_alertmanager_silence_by_id_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_alertmanager_silence_by_id("", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_silence_by_id_no_silence_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.delete_alertmanager_silence_by_id("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": "test"}),
            alerting.get_alertmanager_silence_by_id("test"),
        )

    def test_get_alertmanager_silence_by_id_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_silence_by_id("", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silence_by_id_no_silence_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_silence_by_id("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": "test"}]), alerting.get_alertmanager_silences())

    def test_get_alertmanager_silences_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_silences("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences_no_silence_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": None}]))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_silences()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": "test"}),
            alerting.create_or_update_alertmanager_silence(silence),
        )

    def test_create_or_update_alertmanager_silences_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_alertmanager_silence(None, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence_no_silence_created(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_silence(silence)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"config": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"config": "test"}), alerting.get_alertmanager_status())

    def test_get_alertmanager_status_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_status("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status_no_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"config": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_status()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict(
                {"message": "configuration deleted; the default is applied"}
            )
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.delete_alertmanager_config())

    def test_delete_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_alertmanager_config("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"config": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.delete_alertmanager_config()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"alertmanager_config": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"alertmanager_config": "test"}),
            alerting.get_alertmanager_config(),
        )

    def test_get_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_config("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_config_no_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"config": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_alertmanager_config()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "configuration created"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            alerting.create_or_update_alertmanager_config(
                alertmanager_config, template_files={"test": "test"}
            ),
        )

    def test_create_or_update_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_alertmanager_config(None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config_creation_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"alertmanager_config": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_config(alertmanager_config)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_alertmanager_receivers(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_receivers: AlertmanagerReceivers = AlertmanagerReceivers(
            "test",
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
        )

        call_the_api_mock.return_value.status_code = 200

        self.assertEqual(
            None,
            alerting.test_alertmanager_receivers(
                {"test": "test"}, list([alertmanager_receivers])
            ),
        )

    def test_test_alertmanager_receivers_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_alertmanager_receivers(dict(), None, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_alertmanager_receivers_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_receivers: AlertmanagerReceivers = AlertmanagerReceivers(
            "test",
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
        )

        call_the_api_mock.return_value.status_code = 600

        with self.assertRaises(Exception):
            alerting.test_alertmanager_receivers(
                {"test": "test"}, list([alertmanager_receivers])
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_alertmanager_receivers_test_not_found(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_receivers: AlertmanagerReceivers = AlertmanagerReceivers(
            "test",
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
            ["test"],
        )

        call_the_api_mock.return_value.status_code = 404

        with self.assertRaises(Exception):
            alerting.test_alertmanager_receivers(
                {"test": "test"}, list([alertmanager_receivers])
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"data": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"data": "test"}), alerting.get_prometheus_alerts())

    def test_get_prometheus_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_alerts("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"data": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_prometheus_alerts()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"data": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"data": "test"}), alerting.get_prometheus_rules())

    def test_get_prometheus_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_rules("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"data": None}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_prometheus_rules("grafana")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"data": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"data": "test"}), alerting.get_ruler_rules())

    def test_get_ruler_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_rules("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_ruler_rules()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ruler_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.delete_ruler_namespace("test"))

    def test_delete_ruler_namespace_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_ruler_namespace("", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ruler_namespace_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.delete_ruler_namespace("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_groups_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"test": "test"}),
            alerting.get_ruler_groups_by_namespace("test"),
        )

    def test_get_ruler_groups_by_namespace_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_groups_by_namespace("", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_groups_by_namespace_no_groups_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_ruler_groups_by_namespace("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_ruler_group_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        ruler_rule: RulerRule = RulerRule(
            "test", {"test": "test"}, "test", {"test": "test"}, {"test": "test"}, "test"
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            alerting.create_or_update_ruler_group_by_namespace(
                "test", "test", [ruler_rule]
            ),
        )

    def test_create_or_update_ruler_group_by_namespace_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_ruler_group_by_namespace("", "", None, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_ruler_group_by_namespace_creation_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        ruler_rule: RulerRule = RulerRule(
            "test", {"test": "test"}, "test", {"test": "test"}, {"test": "test"}, "test"
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.create_or_update_ruler_group_by_namespace(
                "test", "test", [ruler_rule]
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.delete_ruler_group("test", "test"))

    def test_delete_ruler_group_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_ruler_group("", "", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ruler_group_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.delete_ruler_group("test", "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"test": "test"}), alerting.get_ruler_group("test", "test")
        )

    def test_get_ruler_group_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_group("", "", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ruler_group_no_ruler_group_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_ruler_group("test", "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"test": "test"}), alerting.test_rule([datasource_rule_query])
        )

    def test_test_rule_no_data_query(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_rule(list())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.text = Mock(return_value="")

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.test_rule([datasource_rule_query])

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_recipient_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"test": "test"}),
            alerting.test_recipient_rule("test", "test", [datasource_rule_query]),
        )

    def test_test_recipient_rule_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_recipient_rule("", "", list(), "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_test_recipient_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.test_recipient_rule("test", "test", [datasource_rule_query])

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(None, alerting.delete_ngalert_organization_configuration())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration_deletion_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.delete_ngalert_organization_configuration()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 200
        call_the_api_mock.return_value.json = Mock(return_value=dict({"test": "test"}))

        self.assertEqual(
            dict({"test": "test"}), alerting.get_ngalert_organization_configuration()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 404

        with self.assertRaises(Exception):
            alerting.get_ngalert_organization_configuration()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_general_exception(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 600

        with self.assertRaises(Exception):
            alerting.get_ngalert_organization_configuration()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            alerting.create_or_update_ngalert_organization_configuration(["test"]),
        )

    def test_create_or_update_ngalert_organization_configuration_no_alert_managers(
        self,
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_ngalert_organization_configuration(list(), "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.create_or_update_ngalert_organization_configuration(["test"])

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"test": "test"}), alerting.get_ngalert_alertmanagers_by_organization()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            alerting.get_ngalert_alertmanagers_by_organization()
