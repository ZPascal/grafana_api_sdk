import os
from unittest import TestCase

from src.grafana_api.model import APIModel
from src.grafana_api.user import CurrentUser
from src.grafana_api.dashboard import Dashboard


class CurrentUserTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        username=os.environ["GRAFANA_USERNAME"],
        password=os.environ["GRAFANA_PASSWORD"],
    )
    current_user: CurrentUser = CurrentUser(model)
    dashboard: Dashboard = Dashboard(model)

    def test_get_user(self):
        self.assertEqual(8, self.current_user.get_user().get("id"))

    def test_get_user_organizations(self):
        self.assertEqual(1, len(self.current_user.get_user_organizations()))

    def test_get_user_teams(self):
        with self.assertRaises(Exception):
            self.current_user.get_user_teams()

    def test_star_a_dashboard(self):
        self.current_user.star_a_dashboard(
            self.dashboard.get_dashboard_by_uid("test1").get("dashboard").get("id")
        )

    def test_unstar_a_dashboard(self):
        self.current_user.unstar_a_dashboard(
            self.dashboard.get_dashboard_by_uid("test1").get("dashboard").get("id")
        )
