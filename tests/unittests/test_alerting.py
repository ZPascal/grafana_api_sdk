from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import (
    APIModel,
    Alert,
    Silence,
    AlertmanagerConfig,
    AlertmanagerReceivers,
    RulerRule,
    DatasourceRuleQuery,
)
from grafana_api.alerting import Alerting


class AlertingTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"receivers": "test"})])

        self.assertEqual(
            list([dict({"receivers": "test"})]),
            alerting.get_alertmanager_alerts(),
        )

    def test_get_alertmanager_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_alerts("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([])

        with self.assertRaises(Exception):
            alerting.get_alertmanager_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alert: Alert = Alert("test", "test", {"test": "test"}, "test", {"test": "test"})

        call_the_api_mock.return_value = dict()

        self.assertEqual(None, alerting.create_or_update_alertmanager_alerts([alert]))

    def test_create_or_update_alertmanager_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_alertmanager_alerts([])

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_alerts_no_alerts_created(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alert: Alert = Alert("test", "test", {"test": "test"}, "test", {"test": "test"})

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_alerts([alert])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_group_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"alerts": "test"}])

        self.assertEqual(
            list([{"alerts": "test"}]),
            alerting.get_alertmanager_group_alerts(),
        )

    def test_get_alertmanager_group_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_group_alerts("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_group_alerts_no_group_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_alertmanager_group_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        self.assertEqual(None, alerting.delete_alertmanager_silence_by_id("test"))

    def test_delete_alertmanager_silence_by_id_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_alertmanager_silence_by_id("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_silence_by_id_no_silence_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": None})

        with self.assertRaises(Exception):
            alerting.delete_alertmanager_silence_by_id("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            alerting.get_alertmanager_silence_by_id("test"),
        )

    def test_get_alertmanager_silence_by_id_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_silence_by_id("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silence_by_id_no_silence_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": None})

        with self.assertRaises(Exception):
            alerting.get_alertmanager_silence_by_id("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": "test"}])

        self.assertEqual(list([{"id": "test"}]), alerting.get_alertmanager_silences())

    def test_get_alertmanager_silences_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_silences("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences_no_silence_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": None}])

        with self.assertRaises(Exception):
            alerting.get_alertmanager_silences()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            alerting.create_or_update_alertmanager_silence(silence),
        )

    def test_create_or_update_alertmanager_silences_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_or_update_alertmanager_silence(None, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence_no_silence_created(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict({"id": None})

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_silence(silence)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"config": "test"})

        self.assertEqual(dict({"config": "test"}), alerting.get_alertmanager_status())

    def test_get_alertmanager_status_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_status("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status_no_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"config": None})

        with self.assertRaises(Exception):
            alerting.get_alertmanager_status()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "configuration deleted; the default is applied"}
        )

        self.assertEqual(None, alerting.delete_alertmanager_config())

    def test_delete_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_alertmanager_config("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"config": None})

        with self.assertRaises(Exception):
            alerting.delete_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"alertmanager_config": "test"})

        self.assertEqual(
            dict({"alertmanager_config": "test"}),
            alerting.get_alertmanager_config(),
        )

    def test_get_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_config("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_config_no_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"config": None})

        with self.assertRaises(Exception):
            alerting.get_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = dict({"message": "configuration created"})

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

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config_creation_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = dict({"alertmanager_config": None})

        with self.assertRaises(Exception):
            alerting.create_or_update_alertmanager_config(alertmanager_config)

    @patch("grafana_api.api.Api.call_the_api")
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

        call_the_api_mock.return_value = dict({"status": 200})

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

    @patch("grafana_api.api.Api.call_the_api")
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

        call_the_api_mock.return_value = dict({"status": 600, "test": "test"})

        with self.assertRaises(Exception):
            alerting.test_alertmanager_receivers(
                {"test": "test"}, list([alertmanager_receivers])
            )

    @patch("grafana_api.api.Api.call_the_api")
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

        call_the_api_mock.return_value = dict({"status": 404, "test": "test"})

        with self.assertRaises(Exception):
            alerting.test_alertmanager_receivers(
                {"test": "test"}, list([alertmanager_receivers])
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"data": "test"})

        self.assertEqual(dict({"data": "test"}), alerting.get_prometheus_alerts())

    def test_get_prometheus_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_alerts("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"data": None})

        with self.assertRaises(Exception):
            alerting.get_prometheus_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"data": "test"})

        self.assertEqual(dict({"data": "test"}), alerting.get_prometheus_rules())

    def test_get_prometheus_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_rules("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"data": None})

        with self.assertRaises(Exception):
            alerting.get_prometheus_rules("grafana")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"data": "test"})

        self.assertEqual(dict({"data": "test"}), alerting.get_ruler_rules())

    def test_get_ruler_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_rules("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_ruler_rules()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        self.assertEqual(None, alerting.delete_ruler_namespace("test"))

    def test_delete_ruler_namespace_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_ruler_namespace("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_namespace_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test"})

        with self.assertRaises(Exception):
            alerting.delete_ruler_namespace("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_groups_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}),
            alerting.get_ruler_groups_by_namespace("test"),
        )

    def test_get_ruler_groups_by_namespace_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_groups_by_namespace("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_groups_by_namespace_no_groups_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_ruler_groups_by_namespace("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ruler_group_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        ruler_rule: RulerRule = RulerRule(
            "test", {"test": "test"}, "test", {"test": "test"}, {"test": "test"}, "test"
        )

        call_the_api_mock.return_value = dict()

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

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ruler_group_by_namespace_creation_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        ruler_rule: RulerRule = RulerRule(
            "test", {"test": "test"}, "test", {"test": "test"}, {"test": "test"}, "test"
        )

        call_the_api_mock.return_value = dict({"test": "test"})

        with self.assertRaises(Exception):
            alerting.create_or_update_ruler_group_by_namespace(
                "test", "test", [ruler_rule]
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        self.assertEqual(None, alerting.delete_ruler_group("test", "test"))

    def test_delete_ruler_group_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_ruler_group("", "", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_group_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test"})

        with self.assertRaises(Exception):
            alerting.delete_ruler_group("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}), alerting.get_ruler_group("test", "test")
        )

    def test_get_ruler_group_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_group("", "", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_group_no_ruler_group_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_ruler_group("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}), alerting.test_rule([datasource_rule_query])
        )

    def test_test_rule_no_data_query(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_rule(list())

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.test_rule([datasource_rule_query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_recipient_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}),
            alerting.test_recipient_rule("test", "test", [datasource_rule_query]),
        )

    def test_test_recipient_rule_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_recipient_rule("", "", list(), "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_recipient_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.test_recipient_rule("test", "test", [datasource_rule_query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        self.assertEqual(None, alerting.delete_ngalert_organization_configuration())

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration_deletion_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            alerting.delete_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            alerting.get_ngalert_organization_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404, "test": "test"})

        with self.assertRaises(Exception):
            alerting.get_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_general_exception(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600, "test": "test"})

        with self.assertRaises(Exception):
            alerting.get_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

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

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            alerting.create_or_update_ngalert_organization_configuration(["test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}), alerting.get_ngalert_alertmanagers_by_organization()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_ngalert_alertmanagers_by_organization()
