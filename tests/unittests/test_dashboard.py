import json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.dashboard import Dashboard


class DashboardTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_create_or_update_dashboard(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = {"status": "success"}

        self.assertEqual(
            None,
            dashboard.create_or_update_dashboard(
                dashboard_path="test",
                dashboard_json={"test": "test"},
                message="test",
            ),
        )

    def test_create_or_update_dashboard_no_dashboard_path_defined(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.create_or_update_dashboard(
                dashboard_path="", dashboard_json={"test": "test"}, message="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_create_or_update_dashboard_update_not_possible(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = {"status": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.create_or_update_dashboard(
                dashboard_path="test",
                dashboard_json={"test": "test"},
                message="test",
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_create_or_update_dashboard_general_folder_omits_folder_uid(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = None
        call_the_api_mock.return_value = {"status": "success"}

        dashboard.create_or_update_dashboard(
            dashboard_path="General",
            dashboard_json={"test": "test"},
            message="test",
        )

        payload = json.loads(call_the_api_mock.call_args[0][2])
        self.assertNotIn("folderUid", payload)

    @patch("grafana_api.api.Api.call_the_api")
    @patch(
        "grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = {"uid": "test", "id": 10}

        call_the_api_mock.return_value = {"message": "Dashboard test deleted"}

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

    @patch("grafana_api.api.Api.call_the_api")
    @patch(
        "grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path_deletion_list_empty(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = {}
        call_the_api_mock.return_value = {"message": "error"}
        with self.assertRaises(ValueError):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch(
        "grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path_dashboard_uid_id_is_none(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = None
        call_the_api_mock.return_value = {"message": "error"}
        with self.assertRaises(TypeError):
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch(
        "grafana_api.dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"
    )
    def test_delete_dashboard_by_name_and_path_deletion_not_possible(
        self, dashboard_uid_and_id_by_name_and_folder_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        dashboard_uid_and_id_by_name_and_folder_mock.return_value = {"uid": "test", "id": 10}

        call_the_api_mock.return_value = {"message": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.delete_dashboard_by_name_and_path(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = [{"uid": "test", "title": "test", "id": 10}]

        self.assertEqual(
            {"uid": "test", "id": 10},
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder_no_id_inside_dashboard_meta_object(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = [{"uid": "test", "title": "test"}]

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder_no_title_inside_dashboard_meta_object(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = [{"uid": "test", "id": 1}]

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder_no_matched_title_inside_dashboard_meta_object(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = [{"uid": "test", "title": "test123", "id": 1}]

        self.assertEqual(
            None,
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder_empty_result(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = "test-uid"
        call_the_api_mock.return_value = []

        self.assertEqual(
            None,
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="test"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.folder.Folder.get_folder_uid_by_dashboard_path")
    def test_get_dashboard_uid_and_id_by_name_and_folder_general_folder_query(
        self, folder_uid_by_dashboard_path_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        folder_uid_by_dashboard_path_mock.return_value = None
        call_the_api_mock.return_value = []

        self.assertEqual(
            None,
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="test", dashboard_path="General"
            ),
        )
        self.assertEqual(
            "/api/search?query=test",
            call_the_api_mock.call_args[0][0],
        )

    def test_get_dashboard_uid_and_id_by_name_and_folder_no_dashboard_name_defined(
        self,
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name="", dashboard_path="test"
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"dashboard": "test"}

        self.assertEqual(
            {"dashboard": "test"}, dashboard.get_dashboard_by_uid(uid="test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_by_uid_no_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_by_uid(uid="test")

    def test_get_dashboard_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_by_uid(uid="")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_home(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"dashboard": "test"}

        self.assertEqual({"dashboard": "test"}, dashboard.get_dashboard_home())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_home_no_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_home()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_tags(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"term": "test", "count": 4}]

        self.assertEqual(
            [{"term": "test", "count": 4}], dashboard.get_dashboard_tags()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_tags_no_tags(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_tags()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"role": "test", "count": 4}]

        self.assertEqual(
            [{"role": "test", "count": 4}],
            dashboard.get_dashboard_permissions(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_permissions_empty_list(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_permissions(1)

    def test_get_dashboard_permissions_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_permissions_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"role": "test", "count": 4}]

        self.assertEqual(
            [{"role": "test", "count": 4}],
            dashboard.get_dashboard_permissions_by_uid("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_permissions_by_uid_empty_list(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_permissions_by_uid("test")

    def test_get_dashboard_permissions_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_permissions_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_dashboard_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Dashboard permissions updated"}

        self.assertEqual(
            None, dashboard.update_dashboard_permissions(1, {"test": "test"})
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_dashboard_permissions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.update_dashboard_permissions(1, {"test": "test"})

    def test_update_dashboard_permissions_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.update_dashboard_permissions(0, MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_dashboard_permissions_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Dashboard permissions updated"}

        self.assertEqual(
            None,
            dashboard.update_dashboard_permissions_by_uid("test", {"test": "test"}),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_dashboard_permissions_by_uid_error_response(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.update_dashboard_permissions_by_uid("test", {"test": "test"})

    def test_update_dashboard_permissions_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.update_dashboard_permissions_by_uid("", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_versions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"id": "test"}]

        self.assertEqual([{"id": "test"}], dashboard.get_dashboard_versions(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_versions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_versions(1)

    def test_get_dashboard_versions_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_versions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_versions_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = [{"uid": "test"}]

        self.assertEqual(
            [{"uid": "test"}], dashboard.get_dashboard_versions_by_uid("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_versions_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_versions_by_uid("test")

    def test_get_dashboard_versions_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_versions_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_version(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": "test"}

        self.assertEqual({"id": "test"}, dashboard.get_dashboard_version(1, 10))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_version_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_version(1, MagicMock())

    def test_get_dashboard_version_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_version(0, MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_gget_dashboard_version_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"uid": "test"}

        self.assertEqual(
            {"uid": "test"}, dashboard.get_dashboard_version_by_uid("test", 10)
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_dashboard_version_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_dashboard_version_by_uid("test", MagicMock())

    def test_get_dashboard_version_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.get_dashboard_version_by_uid("", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_restore_dashboard_version(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": "success"}

        self.assertEqual(
            None, dashboard.restore_dashboard_version(1, {"version": 1})
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_restore_dashboard_version_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.restore_dashboard_version(1, {"version": 1})

    def test_restore_dashboard_version_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.restore_dashboard_version(0, MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_restore_dashboard_version_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": "success"}

        self.assertEqual(
            None,
            dashboard.restore_dashboard_version_by_uid("test", {"version": 1}),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_restore_dashboard_version_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            dashboard.restore_dashboard_version_by_uid("test", {"version": 1})

    def test_restore_dashboard_version_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        with self.assertRaises(ValueError):
            dashboard.restore_dashboard_version_by_uid("", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_calculate_dashboard_diff(self, call_the_api_non_json_output_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_non_json_output_mock.return_value.status_code = 200
        call_the_api_non_json_output_mock.return_value.text = "test"
        self.assertEqual(
            "test",
            dashboard.calculate_dashboard_diff(
                {"dashboardId": 1, "version": 1},
                {"dashboardId": 2, "version": 1},
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_calculate_dashboard_diff_error_response(
        self, call_the_api_non_json_output_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_non_json_output_mock.status_code.return_value = 400
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.calculate_dashboard_diff(
                {"dashboardId": 1, "version": 1},
                {"dashboardId": 2, "version": 1},
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

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboards(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        self.assertEqual(
            {"test": "test"},
            dashboard.get_public_dashboards(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboards_defined_perpage(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        self.assertEqual(
            {"test": "test"},
            dashboard.get_public_dashboards(per_page=1000),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboards_defined_page(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        self.assertEqual(
            {"test": "test"},
            dashboard.get_public_dashboards(page=1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboards_defined_perpage_and_page(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        self.assertEqual(
            {"test": "test"},
            dashboard.get_public_dashboards(per_page=1000, page=1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboards_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_public_dashboards()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboard_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        self.assertEqual(
            {"test": "test"},
            dashboard.get_public_dashboard_by_uid("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboard_by_uid_missing_value(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        with self.assertRaises(ValueError):
            dashboard.get_public_dashboard_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_public_dashboard_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {}
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.get_public_dashboard_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        self.assertEqual(
            {"status": 200, "test": "test"},
            dashboard.create_public_dashboard("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard_missing_value(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        with self.assertRaises(ValueError):
            dashboard.create_public_dashboard("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 400}
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.create_public_dashboard("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 500}
        self.assertEqual(None, dashboard.create_public_dashboard("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard_with_none_default(self, call_the_api_mock):
        from grafana_api.model import PublicDashboard

        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        self.assertEqual(
            {"status": 200, "test": "test"},
            dashboard.create_public_dashboard("test", None),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_public_dashboard_with_explicit_object(self, call_the_api_mock):
        from grafana_api.model import PublicDashboard

        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)
        public_dashboard = PublicDashboard(
            uid="test-uid",
            access_token="test-token",
            time_selection_enabled=True,
            is_enabled=True,
            annotations_enabled=True,
            share="public",
        )

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        self.assertEqual(
            {"status": 200, "test": "test"},
            dashboard.create_public_dashboard("test", public_dashboard),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_public_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        self.assertEqual(
            {"status": 200, "test": "test"},
            dashboard.update_public_dashboard(
                "test", "test", True, True, True, "public"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_public_dashboard_missing_value(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        with self.assertRaises(ValueError):
            dashboard.update_public_dashboard("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_public_dashboard_missing_value_public_dashboard(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        with self.assertRaises(ValueError):
            dashboard.update_public_dashboard("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_public_dashboard_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 400}
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.update_public_dashboard("test", "test", True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_public_dashboard_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 500}
        self.assertEqual(None, dashboard.update_public_dashboard("test", "test", True))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_public_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 200, "test": "test"}
        self.assertEqual(
            None,
            dashboard.delete_public_dashboard("test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_public_dashboard_missing_value(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"test": "test"}
        with self.assertRaises(ValueError):
            dashboard.delete_public_dashboard("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_public_dashboard_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 401}
        with self.assertRaises(Exception):  # noqa: B017
            dashboard.delete_public_dashboard("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_public_dashboard_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        dashboard: Dashboard = Dashboard(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": 500}
        self.assertEqual(None, dashboard.delete_public_dashboard("test", "test"))
