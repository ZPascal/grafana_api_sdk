import os
from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.alerting_provisioning import AlertingProvisioning


class AlertingNotificationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    Alerting_provisioning: AlertingProvisioning = AlertingProvisioning(model)
