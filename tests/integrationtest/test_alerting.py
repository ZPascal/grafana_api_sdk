import os
from unittest import TestCase

from src.grafana_api.model import APIModel
from src.grafana_api.alerting import Alerting


class AlertingTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    alerting: Alerting = Alerting(model)

    def test_get_alertmanager_alerts(self):
        pass
