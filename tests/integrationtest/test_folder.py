import os
from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.folder import Folder


class FolderTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    folder: Folder = Folder(model)

    def test_get_folders(self):
        self.assertEqual(
            [{"id": 72, "uid": "6U_QdWJnz", "title": "Github Integrationtest"}],
            self.folder.get_folders(),
        )

    def test_get_folder_by_uids(self):
        self.assertEqual(
            {
                "canAdmin": True,
                "canDelete": True,
                "canEdit": True,
                "canSave": True,
                "created": "2022-01-10T00:24:58+01:00",
                "createdBy": "webmaster@theiotstudio.com",
                "hasAcl": True,
                "id": 72,
                "title": "Github Integrationtest",
                "uid": "6U_QdWJnz",
                "updated": "2022-01-10T00:24:58+01:00",
                "updatedBy": "webmaster@theiotstudio.com",
                "url": "/dashboards/f/6U_QdWJnz/github-integrationtest",
                "version": 1,
            },
            self.folder.get_folder_by_uid("6U_QdWJnz"),
        )

    def test_get_folder_by_id(self):
        self.assertEqual(
            {
                "canAdmin": True,
                "canDelete": True,
                "canEdit": True,
                "canSave": True,
                "created": "2022-01-10T00:24:58+01:00",
                "createdBy": "webmaster@theiotstudio.com",
                "hasAcl": True,
                "id": 72,
                "title": "Github Integrationtest",
                "uid": "6U_QdWJnz",
                "updated": "2022-01-10T00:24:58+01:00",
                "updatedBy": "webmaster@theiotstudio.com",
                "url": "/dashboards/f/6U_QdWJnz/github-integrationtest",
                "version": 1,
            },
            self.folder.get_folder_by_id(72),
        )

    def test_a_create_folder(self):
        self.folder.create_folder("test1")

        self.assertEqual("test1", self.folder.get_folders()[1].get("title"))

    def test_b_update_folder(self):
        self.folder.update_folder(
            "test2", self.folder.get_folders()[1].get("uid"), version=1
        )

        self.assertEqual("test2", self.folder.get_folders()[1].get("title"))

    def test_c_delete_folder(self):
        self.folder.delete_folder(self.folder.get_folders()[1].get("uid"))

        self.assertEqual(1, len(self.folder.get_folders()))

    def test_get_folder_permissions(self):
        self.assertEqual(
            [
                {
                    "created": "2022-06-14T21:32:34+02:00",
                    "folderId": 72,
                    "inherited": False,
                    "isFolder": True,
                    "permission": 1,
                    "permissionName": "View",
                    "role": "Viewer",
                    "slug": "github-integrationtest",
                    "team": "",
                    "teamAvatarUrl": "",
                    "teamEmail": "",
                    "teamId": 0,
                    "title": "Github Integrationtest",
                    "uid": "6U_QdWJnz",
                    "updated": "2022-06-14T21:32:34+02:00",
                    "url": "/dashboards/f/6U_QdWJnz/github-integrationtest",
                    "userAvatarUrl": "",
                    "userEmail": "",
                    "userId": 0,
                    "userLogin": "",
                }
            ],
            self.folder.get_folder_permissions("6U_QdWJnz"),
        )

    def test_d_update_folder_permissions(self):
        permission_dict: dict = dict({"items": [{"role": "Viewer", "permission": 2}]})

        self.folder.update_folder_permissions("6U_QdWJnz", permission_dict)

        self.assertEqual(
            2, self.folder.get_folder_permissions("6U_QdWJnz")[0].get("permission")
        )

        permission_dict: dict = dict({"items": [{"role": "Viewer", "permission": 1}]})

        self.folder.update_folder_permissions("6U_QdWJnz", permission_dict)

        self.assertEqual(
            1, self.folder.get_folder_permissions("6U_QdWJnz")[0].get("permission")
        )

    def test_get_folder_id_by_dashboard_path(self):
        self.assertEqual(
            72, self.folder.get_folder_id_by_dashboard_path("Github Integrationtest")
        )

    def test_get_all_folder_ids_and_names(self):
        self.assertEqual(
            list([{"id": 72, "title": "Github Integrationtest"}]),
            self.folder.get_all_folder_ids_and_names(),
        )
