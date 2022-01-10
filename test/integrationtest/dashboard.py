import os
import json
from unittest import TestCase, main

from src.grafana_api.model import APIModel
from src.grafana_api.dashboard import Dashboard


class DashboardTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        message="Create a new test dashboard",
        dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
        dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
    )
    dashboard: Dashboard = Dashboard(model)

    def test_dashboard_creation(self):
        with open(f"{os.getcwd()}{os.sep}resources{os.sep}dashboard.json") as file:
            json_dashboard = json.load(file)

        self.dashboard.create_or_update_dashboard(
            dashboard_json=json_dashboard, overwrite=True
        )

        self.assertEqual("tests", self.dashboard.get_dashboard_uid_by_name_and_folder())
        self.assertEqual(30, self.dashboard.get_folder_id_by_dashboard_path())

    def test_dashboard_deletion(self):
        self.dashboard.delete_dashboard_by_name_and_path()

        self.assertEqual(None, self.dashboard.get_dashboard_uid_by_name_and_folder())


if __name__ == "__main__":
    main()
