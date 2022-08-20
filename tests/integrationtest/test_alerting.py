import os
from unittest import TestCase

from src.grafana_api.model import (
    APIModel,
    AlertmanagerConfig,
    AlertmanagerReceivers,
    DatasourceRuleQuery,
)
from src.grafana_api.alerting import Alerting


class AlertingTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    alerting: Alerting = Alerting(model)

    def test_a_create_or_update_alertmanager_config(self):
        alertmanager_config: AlertmanagerConfig = AlertmanagerConfig(
            global_config=None,
            inhibit_rules=None,
            mute_time_intervals=None,
            receivers=[
                {
                    "name": "grafana-default-email-1",
                    "grafana_managed_receiver_configs": [
                        {
                            "uid": None,
                            "name": "email receiver 1",
                            "type": "email",
                            "disableResolveMessage": False,
                            "settings": {"addresses": "<example@email.com>"},
                            "secureFields": {},
                        }
                    ],
                }
            ],
            route={"receiver": "grafana-default-email-1"},
            templates=None,
        )
        self.alerting.create_or_update_alertmanager_config(alertmanager_config)

    def test_b_get_alertmanager_config(self):
        self.assertEqual(
            "grafana-default-email-1",
            self.alerting.get_alertmanager_config()
            .get("alertmanager_config")
            .get("route")
            .get("receiver"),
        )

    def test_c_delete_alertmanager_config(self):
        self.alerting.delete_alertmanager_config()

        result: dict = {
            "template_files": None,
            "alertmanager_config": {
                "route": { "group_by": ["grafana_folder", "alertname"], "receiver": "grafana-default-email"},
                "templates": None,
                "receivers": [
                    {
                        "name": "grafana-default-email",
                        "grafana_managed_receiver_configs": [
                            {
                                "uid": "",
                                "name": "email receiver",
                                "type": "email",
                                "disableResolveMessage": False,
                                "settings": {"addresses": "<example@email.com>"},
                                "secureFields": {},
                            }
                        ],
                    }
                ],
            },
        }
        self.assertEqual(result, self.alerting.get_alertmanager_config())

    def test_test_alertmanager_receivers(self):
        grafana_managed_receiver_configs: list = [
            {
                "uid": None,
                "name": "email receiver",
                "type": "email",
                "disableResolveMessage": False,
                "settings": {"addresses": "info@theiotstudio.com"},
                "secureFields": {},
            }
        ]

        alertmangager_receivers: AlertmanagerReceivers = AlertmanagerReceivers(
            name="Test",
            email_configs=None,
            grafana_managed_receiver_configs=grafana_managed_receiver_configs,
            opsgenie_configs=None,
            pagerduty_configs=None,
            pushover_configs=None,
            slack_configs=None,
            sns_configs=None,
            victorops_configs=None,
            webhook_configs=None,
            wechat_configs=None,
        )
        self.assertEqual(
            None,
            self.alerting.test_alertmanager_receivers(
                alert=dict(
                    {"annotations": {"test": "test"}, "labels": {"test": "test"}}
                ),
                receivers=list([alertmangager_receivers]),
            ),
        )

    def test_get_prometheus_alerts(self):
        result: dict = {
            "status": "success",
            "data": {
                "alerts": [
                    {
                        "labels": {"alertname": "Test", "grafana_folder": "Github Integrationtest"},
                        "annotations": {},
                        "state": "Normal",
                        "activeAt": "0001-01-01T00:00:00Z",
                        "value": "",
                    }
                ]
            },
        }
        self.assertEqual(result, self.alerting.get_prometheus_alerts())

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
            model=dict(),
            query_type="",
            ref_id="test1",
            relative_time_range=dict({"from": 20, "to": 90}),
        )
        data_queries: list = list([datasource_rule_query])

        with self.assertRaises(Exception):
            self.alerting.test_rule(data_queries)

    def test_test_recipient_rule(self):
        datasource_rule_query: DatasourceRuleQuery = DatasourceRuleQuery(
            datasource_uid="test",
            model=dict(),
            query_type="",
            ref_id="test1",
            relative_time_range=dict({"from": 20, "to": 90}),
        )
        data_queries: list = list([datasource_rule_query])

        with self.assertRaises(Exception):
            self.alerting.test_recipient_rule(
                expr="test", condition="test", data_query=data_queries
            )
