from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.dashboard import Dashboard


class DashboardTestCase(TestCase):
    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
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

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
    def test_create_or_update_dashboard_update_not_possible(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1
        call_the_api_mock.return_value = dict({"status": "error"})
        with self.assertRaises(Exception):
            dashboard.create_or_update_dashboard(dashboard_json=dict({"test": "test"}))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_dashboard_uid_by_name_and_folder")
    def test_delete_dashboard_by_name_and_path(
        self, dashboard_uid_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_by_name_and_folder_mock.return_value = "test"
        call_the_api_mock.return_value = dict({"message": "Dashboard None deleted"})
        self.assertEqual(None, dashboard.delete_dashboard_by_name_and_path())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.dashboard.Dashboard.get_dashboard_uid_by_name_and_folder")
    def test_delete_dashboard_by_name_and_path_deletion_list_empty(
        self, dashboard_uid_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_by_name_and_folder_mock.return_value = ""
        call_the_api_mock.return_value = dict({"message": "error"})
        with self.assertRaises(ValueError):
            dashboard.delete_dashboard_by_name_and_path()

    @patch("src.grafana_api.utils.Utils.call_the_api")
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

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
    def test_get_dashboard_uid_by_name_and_folder(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1
        call_the_api_mock.return_value = [{"uid": 10}]
        self.assertEqual(10, dashboard.get_dashboard_uid_by_name_and_folder())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_by_uid(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"dashboard": "test"})
        self.assertEqual(dict({"dashboard": "test"}), dashboard.get_dashboard_by_uid(uid="test"))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_by_uid_no_dashboard(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict()
        with self.assertRaises(Exception):
            dashboard.get_dashboard_by_uid(uid="test")

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_by_uid_no_uid(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"dashboard": "test"})
        with self.assertRaises(ValueError):
            dashboard.get_dashboard_by_uid(uid="")

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_home(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"dashboard": "test"})
        self.assertEqual(dict({"dashboard": "test"}), dashboard.get_dashboard_home())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_home_no_dashboard(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict()
        with self.assertRaises(Exception):
            dashboard.get_dashboard_home()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_tags(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"term": "test", "count": 4}])
        self.assertEqual(list([{"term": "test", "count": 4}]), dashboard.get_dashboard_tags())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_tags_no_tags(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list()
        with self.assertRaises(Exception):
            dashboard.get_dashboard_tags()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_permissions(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"role": "test", "count": 4}])
        self.assertEqual(list([{"role": "test", "count": 4}]), dashboard.get_dashboard_permissions("test"))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_permissions_empty_list(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list()
        with self.assertRaises(Exception):
            dashboard.get_dashboard_permissions("test")

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_permissions_no_uid(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list()
        with self.assertRaises(ValueError):
            dashboard.get_dashboard_permissions("")

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_update_dashboard_permissions(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Dashboard permissions updated"})
        self.assertEqual(None, dashboard.update_dashboard_permissions("test", {"test": "test"}))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_update_dashboard_permissions_error_response(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Error"})
        with self.assertRaises(Exception):
            dashboard.update_dashboard_permissions("test", {"test": "test"})

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_update_dashboard_permissions_no_uid(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = list()
        with self.assertRaises(ValueError):
            dashboard.update_dashboard_permissions("", MagicMock())


if __name__ == "__main__":
    main()
