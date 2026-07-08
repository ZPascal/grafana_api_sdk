import os

import time
from unittest import TestCase

from grafana_api.model import (
    APIModel,
    DatasourceRuleQuery,
)
from grafana_api.alerting import Alerting


class AlertingTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    alerting: Alerting = Alerting(model)

    def test_get_alertmanager_config(self):
        self.assertEqual(
            "grafana-default-email",
            self.alerting.get_alertmanager_config()
            .get("alertmanager_config")
            .get("route")
            .get("receiver"),
        )

    def test_get_prometheus_alerts(self):
        MAX_TRIES: int = 3

        for i in range(0, MAX_TRIES):
            if (
                len(self.alerting.get_prometheus_alerts().get("data").get("alerts"))
                != 0
            ):
                time.sleep(0.1 + i / 2)
                self.assertEqual(
                    "Test",
                    self.alerting.get_prometheus_alerts()
                    .get("data")
                    .get("alerts")[0]
                    .get("labels")
                    .get("alertname"),
                )
            elif i == MAX_TRIES:
                self.fail("Conditions not yet fulfilled.")

    def test_get_prometheus_rules(self):
        self.assertEqual(
            "Github Integrationtest",
            self.alerting.get_prometheus_rules()
            .get("data")
            .get("groups")[0]
            .get("file"),
        )

    def test_get_ruler_rules(self):
        self.assertEqual(
            "Test",
            self.alerting.get_ruler_rules()
            .get("Github Integrationtest")[0]
            .get("name"),
        )

    def test_test_rule(self):
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            datasource_uid="test",
            model={},
            query_type="",
            ref_id="test1",
            relative_time_range={"from": 20, "to": 90},
        )
        data_queries: list = [datasource_rule_query]

        with self.assertRaises(Exception):  # noqa: B017
            self.alerting.test_rule(data_queries)
