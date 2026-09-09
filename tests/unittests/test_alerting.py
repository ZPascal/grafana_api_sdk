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

        call_the_api_mock.return_value = [{"receivers": "test"}]

        self.assertEqual(
            [{"receivers": "test"}],
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

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alert: Alert = Alert("test", "test", {"test": "test"}, "test", {"test": "test"})

        call_the_api_mock.return_value = {}

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

        call_the_api_mock.return_value = {"message": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.create_or_update_alertmanager_alerts([alert])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_group_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = [{"alerts": "test"}]

        self.assertEqual(
            [{"alerts": "test"}],
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

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_group_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "silence deleted"}

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

        call_the_api_mock.return_value = {"id": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_alertmanager_silence_by_id("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silence_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": "test"}

        self.assertEqual(
            {"id": "test"},
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

        call_the_api_mock.return_value = {"id": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_silence_by_id("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = [{"id": "test"}]

        self.assertEqual([{"id": "test"}], alerting.get_alertmanager_silences())

    def test_get_alertmanager_silences_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_silences("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_silences_no_silence_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = [{"id": None}]

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_silences()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {"id": "test"}

        self.assertEqual(
            {"id": "test"},
            alerting.create_or_update_alertmanager_silence(silence),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_silence_return_silence_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        silence: Silence = Silence(
            "test", "test", "test", "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {"silenceID": "test"}

        self.assertEqual(
            {"silenceID": "test"},
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

        call_the_api_mock.return_value = {"id": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.create_or_update_alertmanager_silence(silence)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"config": "test"}

        self.assertEqual({"config": "test"}, alerting.get_alertmanager_status())

    def test_get_alertmanager_status_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_alertmanager_status("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_status_no_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"config": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_status()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {
            "message": "configuration deleted; the default is applied",
            "status": 200,
        }

        self.assertIsNone(alerting.delete_alertmanager_config())

    def test_delete_alertmanager_config_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_alertmanager_config("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"config": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config_provisioned_client_error(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {
            "message": "provisioned and cannot be changed",
            "status": 400,
        }

        with self.assertRaises(SystemError):
            alerting.delete_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alertmanager_config_server_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "server error", "status": 500}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"alertmanager_config": "test"}

        self.assertEqual(
            {"alertmanager_config": "test"},
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

        call_the_api_mock.return_value = {"config": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_alertmanager_config()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = {
            "message": "policies were updated",
            "status": 200,
        }

        self.assertIsNone(alerting.create_or_update_alertmanager_config(
            alertmanager_config, template_files={"test": "test"}
        ))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config_policy_update_rejected(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = {
            "message": "policies were provisioned and cannot be changed through the UI",
            "status": 400,
        }

        with self.assertRaises(SystemError):
            alerting.create_or_update_alertmanager_config(
                alertmanager_config, template_files={"test": "test"}
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config_success(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = {"message": "ok", "status": 200}

        self.assertIsNone(alerting.create_or_update_alertmanager_config(alertmanager_config))

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

        call_the_api_mock.return_value = {"alertmanager_config": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.create_or_update_alertmanager_config(alertmanager_config)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_alertmanager_config_server_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            {"test": "test"}, ["test"], ["test"], ["test"], {"test": "test"}, ["test"]
        )

        call_the_api_mock.return_value = {"message": "server error", "status": 500}

        with self.assertRaises(Exception):  # noqa: B017
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

        call_the_api_mock.return_value = {"status": 200}

        self.assertEqual(
            None,
            alerting.test_alertmanager_receivers(
                {"test": "test"}, [alertmanager_receivers]
            ),
        )

    def test_test_alertmanager_receivers_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_alertmanager_receivers({}, None, "")

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

        call_the_api_mock.return_value = {"status": 600, "test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.test_alertmanager_receivers(
                {"test": "test"}, [alertmanager_receivers]
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

        call_the_api_mock.return_value = {"status": 404, "test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.test_alertmanager_receivers(
                {"test": "test"}, [alertmanager_receivers]
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_alertmanager_receivers_unexpected_4xx_warning(
        self, call_the_api_mock
    ):
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

        call_the_api_mock.return_value = {"status": 422, "message": "unprocessable"}

        with self.assertRaises(SystemError):
            alerting.test_alertmanager_receivers(
                {"test": "test"}, [alertmanager_receivers]
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": "test"}

        self.assertEqual({"data": "test"}, alerting.get_prometheus_alerts())

    def test_get_prometheus_alerts_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_alerts("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_alerts_no_alerts_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_prometheus_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": "test"}

        self.assertEqual({"data": "test"}, alerting.get_prometheus_rules())

    def test_get_prometheus_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_prometheus_rules("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_prometheus_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": None}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_prometheus_rules("grafana")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": "test"}

        self.assertEqual({"data": "test"}, alerting.get_ruler_rules())

    def test_get_ruler_rules_no_recipient(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_ruler_rules("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_rules_no_rules_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ruler_rules()

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

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

        call_the_api_mock.return_value = {"test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_ruler_namespace("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_groups_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"},
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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ruler_groups_by_namespace("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ruler_group_by_namespace(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        ruler_rule: RulerRule = RulerRule(
            "test", {"test": "test"}, "test", {"test": "test"}, {"test": "test"}, "test"
        )

        call_the_api_mock.return_value = {}

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

        call_the_api_mock.return_value = {"test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.create_or_update_ruler_group_by_namespace(
                "test", "test", [ruler_rule]
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

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

        call_the_api_mock.return_value = {"test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_ruler_group("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ruler_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"}, alerting.get_ruler_group("test", "test")
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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ruler_group("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"}, alerting.test_rule([datasource_rule_query])
        )

    def test_test_rule_no_data_query(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_rule([])

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.test_rule([datasource_rule_query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_datasource_uid_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "test", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"},
            alerting.test_datasource_uid_rule("test", "test", [datasource_rule_query]),
        )

    def test_test_datasource_uid_rule_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_datasource_uid_rule("", "", [], "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_backtest_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "datasourceUid", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"},
            alerting.test_backtest_rule("test", [datasource_rule_query]),
        )

    def test_test_backtest_rule_no_condition(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_backtest_rule("", [])

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_backtest_rule_no_fields(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "datasourceUid", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.test_backtest_rule("test", [datasource_rule_query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_datasource_uid_rule_test_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            "test", {"test": "test"}, "datasourceUid", "test", {"test": "test"}
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.test_datasource_uid_rule("test", "test", [datasource_rule_query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        self.assertEqual(None, alerting.delete_ngalert_organization_configuration())

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_ngalert_organization_configuration_deletion_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.delete_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}

        self.assertEqual(
            {"status": 200, "test": "test"},
            alerting.get_ngalert_organization_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 404, "test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_organization_configuration_general_exception(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 600, "test": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ngalert_organization_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

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
            alerting.create_or_update_ngalert_organization_configuration([], "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_ngalert_organization_configuration_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.create_or_update_ngalert_organization_configuration(["test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"}, alerting.get_ngalert_alertmanagers_by_organization()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_ngalert_alertmanagers_by_organization_no_configuration_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: Alerting = Alerting(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting.get_ngalert_alertmanagers_by_organization()
