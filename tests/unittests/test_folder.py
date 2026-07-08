from unittest import TestCase
from unittest.mock import MagicMock, patch

import httpx

from grafana_api.model import APIModel
from grafana_api.folder import Folder


class FolderTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folders(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [{"id": 12, "uid": "test-uid", "title": None}],
            [],
        ]

        self.assertEqual([{"id": 0, "uid": "", "title": "General"}, {"id": 12, "uid": "test-uid", "title": None}], folder.get_folders())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folders_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folders()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": None, "id": 12}

        self.assertEqual(
            {"title": None, "id": 12}, folder.get_folder_by_uid("xty13y")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_uid_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            folder.get_folder_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folder_by_uid("xty13y")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": None, "id": 12}

        self.assertEqual({"title": None, "id": 12}, folder.get_folder_by_id(12))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            folder.get_folder_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_by_id_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folder_by_id(10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_folder(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": None, "id": 12}

        self.assertEqual({"title": None, "id": 12}, folder.create_folder("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_folder_specified_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": None, "id": 12, "uid": "test"}

        self.assertEqual(
            {"title": None, "id": 12, "uid": "test"},
            folder.create_folder("test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_folder_parent_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": None, "id": 12, "parent_uid": "test"}

        self.assertEqual(
            {"title": None, "id": 12, "parent_uid": "test"},
            folder.create_folder("test", parent_uid="test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_folder_no_title(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            folder.create_folder(MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_folder_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            folder.create_folder("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": "test1", "id": 12}

        self.assertEqual(
            {"title": "test1", "id": 12},
            folder.update_folder("test", "test1", 10),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": "test", "id": 12}

        self.assertEqual(
            {"title": "test", "id": 12},
            folder.update_folder("test", uid="test", overwrite=True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_overwrite_true(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": "test", "id": 12}

        self.assertEqual(
            {"title": "test", "id": 12},
            folder.update_folder("test", "test", overwrite=True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_no_title(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            folder.update_folder(MagicMock(), MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            folder.update_folder("test", "test", 10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_move_folder(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": "test1", "id": 12}

        self.assertEqual(
            {"title": "test1", "id": 12},
            folder.move_folder("test"),
        )

    def test_move_folder_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        with self.assertRaises(ValueError):
            folder.move_folder("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_move_folder_parent_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"title": "test", "id": 12}

        self.assertEqual(
            {"title": "test", "id": 12},
            folder.move_folder("test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_move_folder_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            folder.move_folder("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_folder(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 200

        self.assertEqual(None, folder.delete_folder("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_folder_right_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Folder deleted"}

        self.assertEqual(None, folder.delete_folder("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_folder_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value.status_code = 404

        with self.assertRaises(ValueError):
            folder.delete_folder("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_folder_error_response_wrong_object(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = httpx.Response(404)

        with self.assertRaises(Exception):  # noqa: B017
            folder.delete_folder("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_folder_error_response_wrong_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            folder.delete_folder("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = [{"folderId": "test"}]

        self.assertEqual(
            [{"folderId": "test"}], folder.get_folder_permissions("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_permissions_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = []
        with self.assertRaises(ValueError):
            folder.get_folder_permissions("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folder_permissions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = [{"test": "test"}]

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folder_permissions("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Dashboard permissions updated"}

        self.assertEqual(
            None, folder.update_folder_permissions("test", {"test": "test"})
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_permissions_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {}
        with self.assertRaises(ValueError):
            folder.update_folder_permissions("", {})

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_folder_permissions_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "test"}

        with self.assertRaises(Exception):  # noqa: B017
            folder.update_folder_permissions("test", {"test": "test"})

    @patch("grafana_api.folder.Folder.get_all_folder_ids_uids_and_names")
    def test_get_folder_id_by_dashboard_path(self, all_folder_ids_uids_and_names_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_uids_and_names_mock.return_value = [{"id": 12, "uid": "test-uid", "title": "test"}]
        self.assertEqual(
            12, folder.get_folder_id_by_dashboard_path(dashboard_path="test")
        )

    def test_get_folder_id_by_dashboard_path_general_path(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        self.assertEqual(
            0, folder.get_folder_id_by_dashboard_path(dashboard_path="General")
        )

    def test_get_folder_id_by_dashboard_path_no_dashboard_path_defined(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        with self.assertRaises(ValueError):
            folder.get_folder_id_by_dashboard_path(dashboard_path="")

    @patch("grafana_api.folder.Folder.get_all_folder_ids_uids_and_names")
    def test_get_folder_id_by_dashboard_path_no_title_match(
        self, all_folder_ids_uids_and_names_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_uids_and_names_mock.return_value = [{"title": None, "id": "xty13y", "uid": "test-uid"}]
        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folder_id_by_dashboard_path(dashboard_path="test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_folder_ids_uids_and_names(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [{"id": 12, "uid": "test-uid", "title": "test"}],
            []
        ]

        self.assertEqual(
            [
                {"id": 0, "uid": "", "title": "General"},
                {"id": 12, "uid": "test-uid", "title": "test"}
            ], folder.get_all_folder_ids_uids_and_names()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_folder_ids_uids_and_names_fallback_endpoint(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [],
            [{"id": 12, "uid": "test-uid", "title": "test"}],
            []
        ]

        self.assertEqual(
            [
                {"id": 0, "uid": "", "title": "General"},
                {"id": 12, "uid": "test-uid", "title": "test"}
            ], folder.get_all_folder_ids_uids_and_names()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_folder_ids_uids_and_names_shared_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [
                {"id": -1, "uid": "sharedwithme", "title": "Shared with me"},
                {"id": 12, "uid": "test-uid", "title": "test"},
            ],
            [],
            []
        ]

        self.assertEqual(
            [
                {"id": 0, "uid": "", "title": "General"},
                {"id": -1, "uid": "sharedwithme", "title": "Shared with me"},
                {"id": 12, "uid": "test-uid", "title": "test"}
            ], folder.get_all_folder_ids_uids_and_names()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_folder_ids_uids_and_names_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "error"}

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_all_folder_ids_uids_and_names()

    @patch("grafana_api.folder.Folder.get_all_folder_ids_uids_and_names")
    def test_get_folder_uid_by_dashboard_path(self, all_folder_ids_uids_and_names_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_uids_and_names_mock.return_value = [
            {"id": 12, "uid": "test-uid", "title": "test"}
        ]

        self.assertEqual("test-uid", folder.get_folder_uid_by_dashboard_path("test"))

    @patch("grafana_api.folder.Folder.get_all_folder_ids_uids_and_names")
    def test_get_folder_uid_by_dashboard_path_general_path(self, all_folder_ids_uids_and_names_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_uids_and_names_mock.return_value = [
            {"title": "General", "id": 0, "uid": ""}
        ]

        self.assertEqual("", folder.get_folder_uid_by_dashboard_path("General"))

    def test_get_folder_uid_by_dashboard_path_no_dashboard_path_defined(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        with self.assertRaises(ValueError):
            folder.get_folder_uid_by_dashboard_path("")

    @patch("grafana_api.folder.Folder.get_all_folder_ids_uids_and_names")
    def test_get_folder_uid_by_dashboard_path_no_title_match(
        self, all_folder_ids_uids_and_names_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_uids_and_names_mock.return_value = [
            {"title": "different", "id": 12, "uid": "test-uid"}
        ]

        with self.assertRaises(Exception):  # noqa: B017
            folder.get_folder_uid_by_dashboard_path("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folders_with_nested_folders(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [{"id": 1, "uid": "root-uid", "title": "Root"}],
        ]

        result = folder.get_folders()

        self.assertEqual(
            [
                {"id": 0, "uid": "", "title": "General"},
                {"id": 1, "uid": "root-uid", "title": "Root"},
            ],
            result,
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_nested_folders(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [],  # No children
        ]
        self.assertEqual([], folder._get_nested_folders("parent-uid"))

        call_the_api_mock.reset_mock()
        call_the_api_mock.side_effect = [
            [{"id": 2, "uid": "child-1", "title": "Child 1"}],
            [],
        ]
        self.assertEqual(
            [{"id": 2, "uid": "child-1", "title": "Child 1"}],
            folder._get_nested_folders("parent-uid"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_nested_folders_with_siblings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [
                {"id": 2, "uid": "child-1", "title": "Child 1"},
                {"id": 3, "uid": "child-2", "title": "Child 2"},
            ],
            [],
            [],
        ]
        result = folder._get_nested_folders("parent-uid")
        self.assertEqual(
            [
                {"id": 2, "uid": "child-1", "title": "Child 1"},
                {"id": 3, "uid": "child-2", "title": "Child 2"},
            ],
            result,
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_nested_folders_recursive(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [{"id": 2, "uid": "child-1", "title": "Child 1"}],
            [{"id": 3, "uid": "grandchild-1", "title": "Grandchild 1"}],
            [],
        ]
        result = folder._get_nested_folders("parent-uid")
        self.assertEqual(
            [
                {"id": 2, "uid": "child-1", "title": "Child 1"},
                {"id": 3, "uid": "grandchild-1", "title": "Grandchild 1"},
            ],
            result,
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_nested_folders_complex(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [
                {"id": 2, "uid": "child-1", "title": "Child 1"},
                {"id": 3, "uid": "child-2", "title": "Child 2"},
            ],
            [{"id": 4, "uid": "grandchild-1", "title": "Grandchild 1"}],
            [],
            [
                {"id": 5, "uid": "grandchild-2", "title": "Grandchild 2"},
                {"id": 6, "uid": "grandchild-3", "title": "Grandchild 3"},
            ],
            [],
            [],
        ]
        result = folder._get_nested_folders("parent-uid")
        self.assertEqual(
            [
                {"id": 2, "uid": "child-1", "title": "Child 1"},
                {"id": 3, "uid": "child-2", "title": "Child 2"},
                {"id": 4, "uid": "grandchild-1", "title": "Grandchild 1"},
                {"id": 5, "uid": "grandchild-2", "title": "Grandchild 2"},
                {"id": 6, "uid": "grandchild-3", "title": "Grandchild 3"},
            ],
            result,
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_folders_nested_folders_enabled(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.side_effect = [
            [{"id": 1, "uid": "root", "title": "Root"}],
            [{"id": 2, "uid": "child", "title": "Child"}],
            [],
        ]
        result = folder.get_folders(nested_folders=True)
        self.assertEqual(
            [
                {"id": 0, "uid": "", "title": "General"},
                {"id": 1, "uid": "root", "title": "Root"},
                {"id": 2, "uid": "child", "title": "Child"},
            ],
            result,
        )
