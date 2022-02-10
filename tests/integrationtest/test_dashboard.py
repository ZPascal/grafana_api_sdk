import os
import json
from unittest import TestCase, main

import requests.exceptions

from src.grafana_api.model import APIModel
from src.grafana_api.dashboard import Dashboard
from src.grafana_api.folder import Folder


class DashboardTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    dashboard: Dashboard = Dashboard(model)
    folder: Folder = Folder(model)

    def test_a_dashboard_creation(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard.json"
        ) as file:
            json_dashboard = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard",
            dashboard_json=json_dashboard,
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=True,
        )

        self.assertEqual(
            "tests", self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"])["uid"]
        )
        self.assertEqual(72, self.folder.get_folder_id_by_dashboard_path(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"]))

    def test_b_get_dashboard(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_expected_result.json"
        ) as file:
            json_dashboard = json.load(file)

        self.assertEqual(json_dashboard, self.dashboard.get_dashboard_by_uid("tests"))

    def test_c_dashboard_deletion(self):
        self.dashboard.delete_dashboard_by_name_and_path(dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                                                         dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"])

    def test_d_dashboard_creation_general_folder(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard.json"
        ) as file:
            json_dashboard = json.load(file)

        json_dashboard["uid"] = "test_general_folder"

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard",
            dashboard_json=json_dashboard,
            dashboard_path="General",
            overwrite=True,
        )

        self.assertEqual(
            "test_general_folder", self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_path="General",
                dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"])["uid"]
        )
        self.assertEqual(72, self.folder.get_folder_id_by_dashboard_path(
            dashboard_path="General"))

    def test_e_dashboard_deletion_general_folder(self):
        self.dashboard.delete_dashboard_by_name_and_path(dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                                                         dashboard_name="General")

    def test_wrong_token(self):
        self.model.token = "test"

        with self.assertRaises(requests.exceptions.ConnectionError):
            self.dashboard.delete_dashboard_by_name_and_path(dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                                                             dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"])


if __name__ == "__main__":
    main()
