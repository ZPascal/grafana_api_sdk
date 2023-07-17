import os

import time
from unittest import TestCase

from grafana_api.alerting_provisioning import AlertingProvisioning
from grafana_api.model import (
    APIModel,
    AlertRule,
    AlertRuleQueryModel,
    AlertQuery,
    AlertRuleQueryModelCondition,
    EmbeddedContactPoint,
    Route,
    MuteTimeInterval,
    TimeInterval,
    TimeRange,
)


class AlertingProvisioningTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    alerting_provisioning: AlertingProvisioning = AlertingProvisioning(model)

    @classmethod
    def setUpClass(cls) -> None:
        time_interval: TimeInterval = TimeInterval(
            ["1"], ["1:3"], weekdays=["monday"], years=["2023:2035"]
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval(
            "test1", [time_interval]
        )
        cls.alerting_provisioning.add_mute_timing(mute_time_interval)

        time_interval: TimeInterval = TimeInterval(
            ["1"], ["1:3"], weekdays=["monday"], years=["2023:2035"]
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval("test", [time_interval])
        cls.alerting_provisioning.add_mute_timing(mute_time_interval)

        cls.alerting_provisioning.create_or_update_message_template("test", "TEST")

    def test_a_get_alert_rule(self):
        self.assertEqual(
            1, self.alerting_provisioning.get_alert_rule("Z9GoLXx7z").get("id")
        )

    def test_b_add_alert_rule(self):
        self.assertIsNone(
            self.alerting_provisioning.add_alert_rule(
                self.__create_alert_rule("Z9GoLXx7y", "Test1")
            )
        )
        self.assertEqual(
            "Test1", self.alerting_provisioning.get_alert_rule("Z9GoLXx7y").get("title")
        )

    def test_c_update_alert_rule(self):
        self.assertIsNone(
            self.alerting_provisioning.update_alert_rule(
                "Z9GoLXx7y", self.__create_alert_rule("Z9GoLXx7y", "Test1-1")
            )
        )
        self.assertEqual(
            "Test1-1",
            self.alerting_provisioning.get_alert_rule("Z9GoLXx7y").get("title"),
        )

    def test_d_update_the_interval_of_a_alert_rule_group(self):
        self.assertIsNone(
            self.alerting_provisioning.update_the_interval_of_a_alert_rule_group(
                "6U_QdWJnz", "Test", 1200
            )
        )
        os.environ["TZ"] = "Europe/Berlin"
        time.tzset()

        self.assertIn(
            time.strftime("%Y-%m-%dT%H:%M"),
            self.alerting_provisioning.get_alert_rule("Z9GoLXx7y").get("updated"),
        )

    def test_e_delete_alert_rule(self):
        self.assertIsNone(self.alerting_provisioning.delete_alert_rule("Z9GoLXx7y"))

        with self.assertRaises(Exception):
            self.alerting_provisioning.get_alert_rule("Z9GoLXx7y")

    def test_g_get_all_contact_points(self):
        self.assertEqual(
            "email receiver",
            self.alerting_provisioning.get_all_contact_points()[0].get("name"),
        )

    def test_h_add_contact_point(self):
        embedded_contact_point: EmbeddedContactPoint = EmbeddedContactPoint(
            "test", "email", {"addresses": "<example@email.com>"}, False, "test", "test"
        )
        self.alerting_provisioning.add_contact_point(embedded_contact_point)
        self.assertEqual(
            "test", self.alerting_provisioning.get_all_contact_points()[1].get("name")
        )

    def test_i_update_contact_point(self):
        embedded_contact_point: EmbeddedContactPoint = EmbeddedContactPoint(
            "test1",
            "email",
            {"addresses": "<example@email.com>"},
            False,
            "test",
            "test",
        )
        self.alerting_provisioning.update_contact_point("test", embedded_contact_point)
        self.assertEqual(
            "test1", self.alerting_provisioning.get_all_contact_points()[1].get("name")
        )

    def test_j_get_notification_policies(self):
        self.assertEqual(
            "grafana-default-email",
            self.alerting_provisioning.get_notification_policies().get("receiver"),
        )

    def test_k_add_notification_policies(self):
        route: Route = Route(
            False,
            ["grafana_folder", "alertname"],
            "test1",
            "test",
            group_wait="5m",
            group_interval="30s",
            repeat_interval="4h",
        )
        self.alerting_provisioning.add_notification_policies(route)
        self.assertEqual(
            "test1",
            self.alerting_provisioning.get_notification_policies().get("receiver"),
        )

    def test_l_delete_contact_point(self):
        self.alerting_provisioning.delete_contact_point("test")
        self.assertEqual(1, len(self.alerting_provisioning.get_all_contact_points()))

    def test_m_get_all_mute_timings(self):
        self.assertEqual(
            "test1", self.alerting_provisioning.get_all_mute_timings()[0].get("name")
        )

    def test_n_get_mute_timing(self):
        self.assertEqual(
            "test", self.alerting_provisioning.get_mute_timing("test").get("name")
        )

    def test_o_add_mute_timing(self):
        time_interval: TimeInterval = TimeInterval(
            ["1"], ["1:2"], weekdays=["monday"], years=["2023:2040"]
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval(
            "test2", [time_interval]
        )
        self.alerting_provisioning.add_mute_timing(mute_time_interval)
        self.assertEqual(
            "test2", self.alerting_provisioning.get_mute_timing("test2").get("name")
        )

    def test_p_update_mute_timing(self):
        time_interval: TimeInterval = TimeInterval(
            ["2"],
            ["1:4"],
            times=[TimeRange("14:00", "15:00")],
            weekdays=["monday"],
            years=["2023:2035"],
        )
        mute_time_interval: MuteTimeInterval = MuteTimeInterval(
            "test2", [time_interval]
        )
        self.alerting_provisioning.update_mute_timing("test2", mute_time_interval)
        self.assertEqual(
            ["2"],
            self.alerting_provisioning.get_mute_timing("test2")
            .get("time_intervals")[0]
            .get("days_of_month"),
        )
        self.assertEqual(
            ["1:4"],
            self.alerting_provisioning.get_mute_timing("test2")
            .get("time_intervals")[0]
            .get("months"),
        )
        self.assertEqual(
            [{"start_time": "14:00", "end_time": "15:00"}],
            self.alerting_provisioning.get_mute_timing("test2")
            .get("time_intervals")[0]
            .get("times"),
        )

    def test_q_delete_mute_timing(self):
        self.alerting_provisioning.delete_mute_timing("test1")
        self.alerting_provisioning.delete_mute_timing("test2")
        self.assertEqual(1, len(self.alerting_provisioning.get_all_mute_timings()))

    def test_r_get_all_message_templates(self):
        self.assertEqual(
            "test",
            self.alerting_provisioning.get_all_message_templates()[0].get("name"),
        )

    def test_s_get_message_template(self):
        self.assertEqual(
            '{{ define "test" }}\n  TEST\n{{ end }}',
            self.alerting_provisioning.get_message_template("test").get("template"),
        )

    def test_t_create_or_update_message_template(self):
        self.alerting_provisioning.create_or_update_message_template("test1", "TEST1")
        self.assertEqual(
            '{{ define "test1" }}\n  TEST1\n{{ end }}',
            self.alerting_provisioning.get_message_template("test1").get("template"),
        )

    def test_u_delete_message_template(self):
        self.assertEqual(2, len(self.alerting_provisioning.get_all_message_templates()))
        self.alerting_provisioning.delete_message_template("test1")
        self.assertEqual(1, len(self.alerting_provisioning.get_all_message_templates()))

    def doCleanups(self):
        route: Route = Route(
            False,
            ["grafana_folder", "alertname"],
            "grafana-default-email",
            "test",
            group_wait="5m",
            group_interval="30s",
            repeat_interval="4h",
        )
        self.alerting_provisioning.add_notification_policies(route)

    @staticmethod
    def __create_alert_rule(uid: str, title: str) -> AlertRule:
        alert_rule_query_model_condition: AlertRuleQueryModelCondition = (
            AlertRuleQueryModelCondition([20], "gt", "and", ["A"], [], "lost", "query")
        )

        alert_rule_query_model: AlertRuleQueryModel = AlertRuleQueryModel(
            [alert_rule_query_model_condition],
            {"type": "__expr__", "uid": "-100"},
            "",
            False,
            1000,
            43200,
            "A",
            "classic_conditions",
        )

        alert_query: AlertQuery = AlertQuery(
            "5yBH2Yxnk", alert_rule_query_model, "", "A", 600, 0
        )
        return AlertRule(
            "B",
            [alert_query],
            "Alerting",
            "6U_QdWJnz",
            "NoData",
            4,
            "Test",
            title,
            uid,
            "5m",
        )
