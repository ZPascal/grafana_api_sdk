from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import (
    APIModel,
    AlertRule,
    AlertQuery,
    AlertRuleQueryModel,
    AlertRuleQueryModelCondition,
    EmbeddedContactPoint,
    Route,
    Matcher,
    MatchType,
)
from grafana_api.alerting_provisioning import AlertingProvisioning


class AlertingProvisioningTestCase(TestCase):
    def setUp(self):
        self.alert_rule: AlertRule = self.__create_alert_rule_mock()
        self.embedded_contact_point: EmbeddedContactPoint = EmbeddedContactPoint(
            "test", "test", {"test": "test"}
        )
        matcher: Matcher = Matcher("test", MatchType.MatchEqual, "test")
        route_2: Route = Route(
            False, ["test"], ["test"], "test", 1, 1, [matcher], "test", 1
        )
        self.route: Route = Route(
            False,
            ["test"],
            ["test"],
            "test",
            1,
            1,
            [matcher],
            "test",
            1,
            routes=[route_2],
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"test": "test"})

        self.assertEqual(
            dict({"test": "test"}),
            alerting_provisioning.get_alert_rule("test"),
        )

    def test_get_alert_rule_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.get_alert_rule("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_rule_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting_provisioning.get_alert_rule("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None,
            alerting_provisioning.add_alert_rule(self.alert_rule),
        )

    def test_add_alert_rule_no_alert_rule(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.add_alert_rule(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_alert_rule_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.add_alert_rule(self.alert_rule)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None,
            alerting_provisioning.update_alert_rule("test", self.alert_rule),
        )

    def test_update_alert_rule_no_alert_rule(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.update_alert_rule("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_alert_rule_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.update_alert_rule("", self.alert_rule)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_the_interval_of_a_alert_rule_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None,
            alerting_provisioning.update_the_interval_of_a_alert_rule_group(
                "test", "test", 1
            ),
        )

    def test_update_the_interval_of_a_alert_rule_group_no_folder_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.update_the_interval_of_a_alert_rule_group("", "", 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_the_interval_of_a_alert_rule_group_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.update_the_interval_of_a_alert_rule_group(
                "test", "test", 1
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None,
            alerting_provisioning.delete_alert_rule("test"),
        )

    def test_delete_alert_rule_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.delete_alert_rule("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alert_rule_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.delete_alert_rule("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_contact_points(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = list([{"test": "test"}])

        self.assertEqual(
            list([{"test": "test"}]),
            alerting_provisioning.get_all_contact_points(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_contact_points_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting_provisioning.get_all_contact_points()

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None, alerting_provisioning.add_contact_point(self.embedded_contact_point)
        )

    def test_add_contact_point_no_embedded_contact_point(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.add_contact_point(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_contact_point_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.add_contact_point(self.embedded_contact_point)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None,
            alerting_provisioning.update_contact_point(
                "test", self.embedded_contact_point
            ),
        )

    def test_update_contact_point_no_embedded_contact_point(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.update_contact_point("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_contact_point_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.update_contact_point(
                "test", self.embedded_contact_point
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(None, alerting_provisioning.delete_contact_point("test"))

    def test_delete_contact_point_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.delete_contact_point("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_contact_point_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.delete_contact_point("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201, "test": "test"})

        self.assertEqual(
            dict({"status": 201, "test": "test"}),
            alerting_provisioning.get_notification_policies(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.get_notification_policies()

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_notification_policies(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 201})

        self.assertEqual(
            None, alerting_provisioning.add_notification_policies(self.route)
        )

    def test_add_notification_policies_no_rule(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.add_notification_policies(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_notification_policies_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            alerting_provisioning.add_notification_policies(self.route)

    @staticmethod
    def __create_alert_rule_mock() -> AlertRule:
        alert_rule_query_model_condition: AlertRuleQueryModelCondition = (
            AlertRuleQueryModelCondition(
                ["test"], "test", "test", ["test"], ["test"], "test", "test"
            )
        )
        alert_rule_query_model: AlertRuleQueryModel = AlertRuleQueryModel(
            [alert_rule_query_model_condition],
            {"test": "test"},
            "test",
            False,
            1,
            1,
            "test",
            "test",
        )
        alert_query: AlertQuery = AlertQuery(
            "test", alert_rule_query_model, "test", "test", 1, 1
        )
        return AlertRule(
            "test", [alert_query], "test", "test", "test", 1, "test", "test", "test", 1
        )
