from unittest import TestCase, main
from unittest.mock import MagicMock, patch, Mock

from requests.exceptions import MissingSchema

from src.grafana_api.model import APIModel, RequestsMethods
from src.grafana_api.dashboard import Dashboard


class DashboardTestCase(TestCase):
    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_folder_id_by_dashboard_path")
    def test_create_or_update_dashboard(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1
        call_the_api_mock.return_value = dict({"status": "success"})
        self.assertEqual(
            None,
            dashboard.create_or_update_dashboard(dashboard_json=dict({"test": "test"})),
        )

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_folder_id_by_dashboard_path")
    def test_create_or_update_dashboard_update_not_possible(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1
        call_the_api_mock.return_value = dict({"status": "error"})
        with self.assertRaises(Exception):
            dashboard.create_or_update_dashboard(dashboard_json=dict({"test": "test"}))

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_dashboard_uid_by_name_and_folder")
    def test_delete_dashboard_by_name_and_path(
        self, dashboard_uid_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_by_name_and_folder_mock.return_value = "test"
        call_the_api_mock.return_value = dict({"message": "Dashboard None deleted"})
        self.assertEqual(None, dashboard.delete_dashboard_by_name_and_path())

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_dashboard_uid_by_name_and_folder")
    def test_delete_dashboard_by_name_and_path_deletion_list_empty(
        self, dashboard_uid_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_by_name_and_folder_mock.return_value = ""
        call_the_api_mock.return_value = dict({"message": "error"})
        self.assertEqual(None, dashboard.delete_dashboard_by_name_and_path())

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_dashboard_uid_by_name_and_folder")
    def test_delete_dashboard_by_name_and_path_deletion_not_possible(
        self, dashboard_uid_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_by_name_and_folder_mock.return_value = "test"
        call_the_api_mock.return_value = dict({"message": "error"})
        with self.assertRaises(Exception):
            dashboard.delete_dashboard_by_name_and_path()

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_folder_id_by_dashboard_path")
    def test_get_dashboard_uid_by_name_and_folder(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1
        call_the_api_mock.return_value = [{"uid": 10}]
        self.assertEqual(10, dashboard.get_dashboard_uid_by_name_and_folder())

    @patch("src.grafana_api.dashboard.Dashboard.get_all_folder_ids_and_names")
    def test_get_folder_id_by_dashboard_path(self, all_folder_ids_and_names_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        all_folder_ids_and_names_mock.return_value = [{"title": None, "id": 12}]
        self.assertEqual(12, dashboard.get_folder_id_by_dashboard_path())

    @patch("src.grafana_api.dashboard.Dashboard.get_all_folder_ids_and_names")
    def test_get_folder_id_by_dashboard_path_no_title_match(
        self, all_folder_ids_and_names_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        all_folder_ids_and_names_mock.return_value = [{"title": "test", "id": "xty13y"}]
        with self.assertRaises(Exception):
            dashboard.get_folder_id_by_dashboard_path()

    @patch("src.grafana_api.dashboard.Dashboard._Dashboard__call_the_api")
    def test_get_all_folder_ids_and_names(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"title": "test", "id": 12, "test": "test"}]
        self.assertEqual(
            [{"title": "test", "id": 12}], dashboard.get_all_folder_ids_and_names()
        )

    def test_call_the_api_non_method(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(Exception):
            dashboard._Dashboard__call_the_api(api_call=MagicMock(), method=None)

    @patch("requests.get")
    def test_call_the_api_get_valid(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        get_mock.return_value = mock

        self.assertEqual(
            "success",
            dashboard._Dashboard__call_the_api(api_call=MagicMock())["status"],
        )

    def test_call_the_api_get_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(), method=RequestsMethods.GET
            )

    @patch("requests.post")
    def test_call_the_api_post_valid(self, post_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        post_mock.return_value = mock

        self.assertEqual(
            "success",
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                dashboard_json_complete=MagicMock(),
            )["status"],
        )

    def test_call_the_api_post_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                dashboard_json_complete=MagicMock(),
            )

    def test_call_the_api_post_no_data(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(Exception):
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(), method=RequestsMethods.POST
            )

    @patch("requests.delete")
    def test_call_the_api_delete_valid(self, delete_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"message": "Deletion successful"})

        delete_mock.return_value = mock

        self.assertEqual(
            "Deletion successful",
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(), method=RequestsMethods.DELETE
            )["message"],
        )

    def test_call_the_api_delete_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(Exception):
            dashboard._Dashboard__call_the_api(
                api_call=MagicMock(), method=RequestsMethods.DELETE
            )


if __name__ == "__main__":
    main()
