import os
from unittest import TestCase

from grafana_api.model import (
    APIModel,
)
from grafana_api.other_http import OtherHTTP


class OtherHTTPTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    other_http: OtherHTTP = OtherHTTP(model)

    def test_get_frontend_settings(self):
        self.assertEqual(
            False, self.other_http.get_frontend_settings().get("allowOrgCreate")
        )

    def test_renew_login_session_based_on_remember_cookie(self):
        self.assertIsNone(
            self.other_http.renew_login_session_based_on_remember_cookie()
        )

    def test_get_health_status(self):
        self.assertIsNotNone(self.other_http.get_health_status())
