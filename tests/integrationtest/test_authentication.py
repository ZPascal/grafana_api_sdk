import os
from unittest import TestCase

from grafana_api.model import (
    APIModel,
)
from grafana_api.authentication import Authentication


class AlertingTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    authentication: Authentication = Authentication(model)

    def test_a_get_api_tokens(self):
        self.assertEqual(1, len(self.authentication.get_api_tokens()))

    def test_b_create_api_token(self):
        self.assertIsNotNone(
            self.authentication.create_api_token("Test", "Viewer").get("id")
        )

    def test_c_delete_api_token(self):
        self.assertIsNone(
            self.authentication.delete_api_token(
                self.authentication.get_api_tokens()[1].get("id")
            )
        )
