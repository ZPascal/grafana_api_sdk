from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.dashboard import Dashboard


class DashboardTestCase(TestCase):
    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
    def test_create_or_update_dashboard(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"status": "success"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            dashboard.create_or_update_dashboard(
                dashboard_path="test",
                dashboard_json=dict({"test": "test"}),
                message="test",
            ),
        )

    def test_create_or_update_dashboard_no_dashboard_path_defined(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.create_or_update_dashboard(
                dashboard_path="", dashboard_json=dict({"test": "test"}), message="test"
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
    def test_create_or_update_dashboard_update_not_possible(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"status": "error"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.create_or_update_dashboard(
                dashboard_path="test",
                dashboard_json=dict({"test": "test"}),
                message="test",
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch(
        "src.grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = dict(
            {"uid": "test", "id": 10}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Dashboard test deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            ),
        )

    def test_delete_dashboard_by_name_and_path_no_dashboard_name(
        self,
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="", dashboard_path="test"
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch(
        "src.grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path_deletion_list_empty(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = dict()
        call_the_api_mock.return_value = dict({"message": "error"})
        with self.assertRaises(ValueError):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch(
        "src.grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path_deletion_not_possible(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = dict(
            {"uid": "test", "id": 10}
        )

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "error"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    @patch("src.grafana_api.folder.Folder.get_folder_id_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder(
        self, folder_id_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_id_by_dashboard_path_mock.return_value = 1

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"uid": "test", "id": 10}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"uid": "test", "id": 10}),
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            ),
        )

    def test_get_dashboard_uid_and_id_by_name_and_folder_bo_dashboard_name_defined(
        self,
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="", dashboard_path="test"
            )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"dashboard": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"dashboard": "test"}), dashboard.get_dashboard_by_uid(uid="test")
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_by_uid_no_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_by_uid(uid="test")

    def test_get_dashboard_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_by_uid(uid="")

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_home(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"dashboard": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"dashboard": "test"}), dashboard.get_dashboard_home())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_home_no_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_home()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_tags(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"term": "test", "count": 4}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"term": "test", "count": 4}]), dashboard.get_dashboard_tags()
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_tags_no_tags(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_tags()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"role": "test", "count": 4}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"role": "test", "count": 4}]),
            dashboard.get_dashboard_permissions(1),
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_permissions_empty_list(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_permissions(1)

    def test_get_dashboard_permissions_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_permissions(0)

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_update_dashboard_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict({"message": "Dashboard permissions updated"})
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, dashboard.update_dashboard_permissions(1, {"test": "test"})
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_update_dashboard_permissions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Error"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.update_dashboard_permissions(1, {"test": "test"})

    def test_update_dashboard_permissions_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.update_dashboard_permissions(0, MagicMock())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_versions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": "test"}]), dashboard.get_dashboard_versions(1))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_versions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_versions(1)

    def test_get_dashboard_versions_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_versions(0)

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_version(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"id": "test"}), dashboard.get_dashboard_version(1, 10))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_dashboard_version_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.get_dashboard_version(1, MagicMock())

    def test_get_dashboard_version_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_version(0, MagicMock())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_restore_dashboard_version(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"status": "success"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, dashboard.restore_dashboard_version(1, dict({"version": 1}))
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_restore_dashboard_version_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"status": "error"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            dashboard.restore_dashboard_version(1, dict({"version": 1}))

    def test_restore_dashboard_version_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.restore_dashboard_version(0, MagicMock())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_calculate_dashboard_diff(self, call_the_api_non_json_output_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_non_json_output_mock.return_value.status_code = 200
        call_the_api_non_json_output_mock.return_value.text = "test"
        self.assertEqual(
            "test",
            dashboard.calculate_dashboard_diff(
                dict({"dashboardId": 1, "version": 1}),
                dict({"dashboardId": 2, "version": 1}),
            ),
        )

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_calculate_dashboard_diff_error_response(
        self, call_the_api_non_json_output_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_non_json_output_mock.status_code.return_value = 400
        with self.assertRaises(Exception):
            dashboard.calculate_dashboard_diff(
                dict({"dashboardId": 1, "version": 1}),
                dict({"dashboardId": 2, "version": 1}),
            )

    def test_calculate_dashboard_diff_no_dashboard_id_and_version_base(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.calculate_dashboard_diff({}, MagicMock())

    def test_calculate_dashboard_diff_no_valid_diff_type(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.calculate_dashboard_diff({}, MagicMock(), "test")
