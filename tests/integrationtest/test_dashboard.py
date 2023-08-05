import os

import json
from unittest import TestCase

import httpx

from grafana_api.model import APIModel
from grafana_api.dashboard import Dashboard
from grafana_api.folder import Folder


class DashboardTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
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
            dashboard_json=json_dashboard.get("dashboard"),
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=True,
        )

        self.assertEqual(
            "test1",
            self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
            )["uid"],
        )
        self.assertEqual(
            72,
            self.folder.get_folder_id_by_dashboard_path(
                dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"]
            ),
        )

    def test_b_get_dashboard(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_expected_result.json"
        ) as file:
            json_dashboard = json.load(file)

        self.assertEqual(
            self.dashboard.get_dashboard_by_uid("tests").get("dashboard"),
            json_dashboard.get("dashboard"),
        )

    def test_c_dashboard_deletion(self):
        self.dashboard.delete_dashboard_by_name_and_path(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
        )

    def test_d_dashboard_creation_general_folder(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard.json"
        ) as file:
            json_dashboard = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard",
            dashboard_json=json_dashboard.get("dashboard"),
            dashboard_path="General",
            overwrite=True,
        )

        self.assertEqual(
            "test1",
            self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_path="General",
                dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
            )["uid"],
        )
        self.assertEqual(
            0, self.folder.get_folder_id_by_dashboard_path(dashboard_path="General")
        )

    def test_e_dashboard_deletion_general_folder(self):
        self.dashboard.delete_dashboard_by_name_and_path(
            dashboard_path="General",
            dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
        )

    def test_wrong_token(self):
        model: APIModel = APIModel(
            host=os.environ["GRAFANA_HOST"],
            token="test",
        )

        dashboard: Dashboard = Dashboard(model)

        with self.assertRaises(httpx.ConnectError):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
                dashboard_name=os.environ["GRAFANA_DASHBOARD_NAME"],
            )

    def test_f_calculate_dashboard_diff_json_mode(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_diff_a.json"
        ) as file:
            json_dashboard_a = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard a",
            dashboard_json=json_dashboard_a.get("dashboard"),
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=False,
        )

        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_diff_b.json"
        ) as file:
            json_dashboard_b = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard b",
            dashboard_json=json_dashboard_b.get("dashboard"),
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=False,
        )

        dashboard_a: dict = self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            dashboard_name="TestA",
        )

        dashboard_b: dict = self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            dashboard_name="TestB",
        )

        self.assertEqual(
            "testA",
            dashboard_a["uid"],
        )
        self.assertEqual(
            "testB",
            dashboard_b["uid"],
        )

        diff_a: dict = dict({"dashboardId": dashboard_a["id"], "version": 1})
        diff_b: dict = dict({"dashboardId": dashboard_b["id"], "version": 1})
        self.assertIsNotNone(self.dashboard.calculate_dashboard_diff(diff_a, diff_b))

        self.dashboard.delete_dashboard_by_name_and_path(
            "TestA", os.environ["GRAFANA_DASHBOARD_PATH"]
        )
        self.dashboard.delete_dashboard_by_name_and_path(
            "TestB", os.environ["GRAFANA_DASHBOARD_PATH"]
        )

    def test_g_calculate_dashboard_diff_basic_mode(self):
        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_diff_a.json"
        ) as file:
            json_dashboard_a = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard a",
            dashboard_json=json_dashboard_a.get("dashboard"),
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=False,
        )

        with open(
            f"{os.getcwd()}{os.sep}tests{os.sep}integrationtest{os.sep}resources{os.sep}dashboard_diff_b.json"
        ) as file:
            json_dashboard_b = json.load(file)

        self.dashboard.create_or_update_dashboard(
            message="Create a new test dashboard b",
            dashboard_json=json_dashboard_b.get("dashboard"),
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            overwrite=False,
        )

        dashboard_a: dict = self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            dashboard_name="TestA",
        )

        dashboard_b: dict = self.dashboard.get_dashboard_uid_and_id_by_name_and_folder(
            dashboard_path=os.environ["GRAFANA_DASHBOARD_PATH"],
            dashboard_name="TestB",
        )

        self.assertEqual(
            "testA",
            dashboard_a["uid"],
        )
        self.assertEqual(
            "testB",
            dashboard_b["uid"],
        )

        diff_a: dict = dict({"dashboardId": dashboard_a["id"], "version": 1})
        diff_b: dict = dict({"dashboardId": dashboard_b["id"], "version": 1})
        self.assertIsNotNone(
            self.dashboard.calculate_dashboard_diff(diff_a, diff_b, "basic")
        )

        self.dashboard.delete_dashboard_by_name_and_path(
            "TestA", os.environ["GRAFANA_DASHBOARD_PATH"]
        )
        self.dashboard.delete_dashboard_by_name_and_path(
            "TestB", os.environ["GRAFANA_DASHBOARD_PATH"]
        )
