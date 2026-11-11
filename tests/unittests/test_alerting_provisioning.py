import warnings
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
    MuteTimeInterval,
    TimeInterval,
    TimeRange,
)
from grafana_api.alerting_provisioning import AlertingProvisioning


class AlertingProvisioningTestCase(TestCase):
    def setUp(self):
        self.alert_rule: AlertRule = self._create_alert_rule_mock()
        self.embedded_contact_point: EmbeddedContactPoint = EmbeddedContactPoint(
            "test", "test", {"test": "test"}
        )
        matcher: Matcher = Matcher("test", MatchType.MatchEqual, "test")
        route_2: Route = Route(False, ["test"], "test", "test")
        self.route: Route = Route(
            False,
            ["test"],
            "test",
            "test",
            object_matchers=[matcher],
            routes=[route_2],
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"id": "test"}

        self.assertEqual(
            {"id": "test"},
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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_alert_rule("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.add_alert_rule(self.alert_rule)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.update_alert_rule("test", self.alert_rule)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_the_interval_of_a_alert_rule_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.update_the_interval_of_a_alert_rule_group(
                "test", "test", 1
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_alert_rule(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 204}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.delete_alert_rule("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_contact_points(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = [{"test": "test"}]

        self.assertEqual(
            [{"test": "test"}],
            alerting_provisioning.get_all_contact_points(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_contact_points_empty(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = []

        self.assertEqual([], alerting_provisioning.get_all_contact_points())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_contact_points_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"message": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_all_contact_points()

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.add_contact_point(self.embedded_contact_point)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.update_contact_point(
                "test", self.embedded_contact_point
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_contact_point(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.delete_contact_point("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201, "test": "test"}

        self.assertEqual(
            {"status": 201, "test": "test"},
            alerting_provisioning.get_notification_policies(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_notification_policies()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_by_receiver(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        child: dict = {"receiver": "test1", "routes": [{"receiver": "test2"}]}
        call_the_api_mock.return_value = {
            "status": 200,
            "receiver": "test1",
            "routes": [child, {"receiver": "test3"}],
        }

        policies: list = alerting_provisioning.get_notification_policies_by_receiver(
            "test1"
        )

        self.assertEqual(2, len(policies))
        self.assertEqual(child, policies[1])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_by_receiver_nested(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {
            "status": 200,
            "receiver": "test1",
            "routes": [{"receiver": "test3", "routes": [{"receiver": "test2"}]}],
        }

        self.assertEqual(
            [{"receiver": "test2"}],
            alerting_provisioning.get_notification_policies_by_receiver("test2"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_by_receiver_no_match(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "receiver": "test1"}

        self.assertEqual(
            [], alerting_provisioning.get_notification_policies_by_receiver("test2")
        )

    def test_get_notification_policies_by_receiver_no_receiver(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.get_notification_policies_by_receiver("")

        with self.assertRaises(ValueError):
            alerting_provisioning.get_notification_policies_by_receiver(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_by_receiver_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_notification_policies_by_receiver("test1")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_notification_policies(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

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

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.add_notification_policies(self.route)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_mute_timings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = [{"test": "test"}]

        self.assertEqual(
            [{"test": "test"}], alerting_provisioning.get_all_mute_timings()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_mute_timings_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_all_mute_timings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_mute_timing(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"test": "test"}

        self.assertEqual(
            {"test": "test"}, alerting_provisioning.get_mute_timing("test")
        )

    def test_get_mute_timing_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.get_mute_timing("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_mute_timing_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_mute_timing("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_mute_timing(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )
        time_range: TimeRange = TimeRange(1, 1)
        time_interval: TimeInterval = TimeInterval(
            ["test"], ["test"], [time_range], ["test"], ["test"]
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval("test", [time_interval])

        call_the_api_mock.return_value = {"status": 201}

        self.assertEqual(
            None, alerting_provisioning.add_mute_timing(mute_time_interval)
        )

    def test_add_mute_timing_no_mute_time_interval(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.add_mute_timing(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_mute_timing_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval("test")

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.add_mute_timing(mute_time_interval)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_mute_timing(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval("test", None)

        call_the_api_mock.return_value = {"status": 201}

        self.assertEqual(
            None, alerting_provisioning.update_mute_timing("test", mute_time_interval)
        )

    def test_update_mute_timing_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.update_mute_timing("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_mute_timing_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval("test")

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.update_mute_timing("test", mute_time_interval)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_mute_timing(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

        self.assertEqual(None, alerting_provisioning.delete_mute_timing("test"))

    def test_delete_mute_timing_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.delete_mute_timing("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_mute_timing_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.delete_mute_timing("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_message_templates(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = [{"test": "test"}]

        self.assertEqual(
            [{"test": "test"}], alerting_provisioning.get_all_message_templates()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_message_templates_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_all_message_templates()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_message_template(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201, "test": "test"}

        self.assertEqual(
            {"status": 201, "test": "test"},
            alerting_provisioning.get_message_template("test"),
        )

    def test_get_message_template_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.get_message_template("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_message_template_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.get_message_template("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_message_template(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

        self.assertEqual(
            None,
            alerting_provisioning.create_or_update_message_template("test", "test"),
        )

    def test_create_or_update_message_template_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.create_or_update_message_template("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_or_update_message_template_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.create_or_update_message_template("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_message_template(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 201}

        self.assertEqual(None, alerting_provisioning.delete_message_template("test"))

    def test_delete_message_template_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            alerting_provisioning.delete_message_template("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_message_template_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            alerting_provisioning.delete_message_template("test")

    def test_create_time_range_list(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting_provisioning: AlertingProvisioning = AlertingProvisioning(
            grafana_api_model=model
        )
        self.assertEqual(
            None,
            alerting_provisioning._create_time_range_list(None),
        )

    @staticmethod
    def _create_alert_rule_mock() -> AlertRule:
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
            "test",
            [alert_query],
            "test",
            "test",
            "test",
            1,
            "test",
            "test",
            "test",
            "1m",
        )


DEPRECATED_METHODS: list = [
    "get_alert_rule",
    "add_alert_rule",
    "update_alert_rule",
    "delete_alert_rule",
    "get_all_contact_points",
    "add_contact_point",
    "update_contact_point",
    "delete_contact_point",
    "get_notification_policies",
    "get_notification_policies_by_receiver",
    "add_notification_policies",
    "get_all_mute_timings",
    "get_mute_timing",
    "add_mute_timing",
    "update_mute_timing",
    "delete_mute_timing",
    "get_all_message_templates",
    "get_message_template",
    "create_or_update_message_template",
    "delete_message_template",
    "update_the_interval_of_a_alert_rule_group",
]


class AlertingProvisioningDeprecationTestCase(TestCase):
    def setUp(self):
        self.provisioning: AlertingProvisioning = AlertingProvisioning(
            APIModel(host=MagicMock(), token=MagicMock())
        )

    def test_every_public_method_is_covered(self):
        public: set = {
            name
            for name in dir(AlertingProvisioning)
            if not name.startswith("_") and callable(getattr(AlertingProvisioning, name))
        }

        self.assertEqual(set(DEPRECATED_METHODS), public)

    @patch("grafana_api.api.Api.call_the_api")
    def test_all_public_methods_warn_that_there_is_no_stable_replacement(self, call_the_api_mock):
        call_the_api_mock.return_value = {"status": 200}
        for name in DEPRECATED_METHODS:
            with self.subTest(method=name):
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    try:
                        getattr(self.provisioning, name)(
                            *[MagicMock() for _ in range(self._argument_count(name))]
                        )
                    except Exception:
                        pass

                messages: list = [
                    str(w.message) for w in caught if issubclass(w.category, DeprecationWarning)
                ]
                self.assertEqual(1, len(messages))
                self.assertIn("no stable replacement", messages[0])
                self.assertNotIn("AlertingAppPlatform", messages[0])

    def test_deprecated_methods_keep_their_name(self):
        for name in DEPRECATED_METHODS:
            self.assertEqual(name, getattr(AlertingProvisioning, name).__name__)

    @staticmethod
    def _argument_count(name: str) -> int:
        import inspect

        parameters = inspect.signature(getattr(AlertingProvisioning, name)).parameters
        return len([p for p in parameters.values() if p.name != "self" and p.default is p.empty])


class AlertingProvisioningWarnsOnceTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_policies_by_receiver_warns_exactly_once(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"status": 200, "receiver": "test", "routes": []}
        provisioning: AlertingProvisioning = AlertingProvisioning(
            APIModel(host=MagicMock(), token=MagicMock())
        )

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            provisioning.get_notification_policies_by_receiver("test")

        self.assertEqual(
            1, len([w for w in caught if issubclass(w.category, DeprecationWarning)])
        )
        self.assertEqual(1, call_the_api_mock.call_count)
