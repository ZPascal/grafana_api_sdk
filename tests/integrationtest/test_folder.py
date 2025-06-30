import os

from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.folder import Folder


class FolderTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    folder: Folder = Folder(model)

    def test_get_folders(self):
        self.assertEqual(
            [{"id": 72, "uid": "6U_QdWJnz", "title": "Github Integrationtest"}],
            self.folder.get_folders(),
        )

    def test_get_folder_by_uids(self):
        self.assertEqual(
            "Github Integrationtest",
            self.folder.get_folder_by_uid("6U_QdWJnz").get("title"),
        )

    def test_get_folder_by_id(self):
        self.assertEqual(
            "Github Integrationtest",
            self.folder.get_folder_by_id(72).get("title"),
        )

    def test_a_create_folder(self):
        self.folder.create_folder("test1")

        self.assertEqual("test1", self.folder.get_folders()[1].get("title"))

    def test_b_subfolder(self):
        parent_uid = self.folder.get_folders()[1].get("uid")

        subfolder: dict = self.folder.create_folder("test2", parent_uid=parent_uid)

        self.assertEqual(
            "test2", self.folder.get_folder_by_uid(subfolder["uid"]).get("title")
        )

    def test_c_update_folder(self):
        self.folder.update_folder(
            "test2", self.folder.get_folders()[1].get("uid"), version=1
        )

        self.assertEqual("test2", self.folder.get_folders()[1].get("title"))

    def test_d_move_folder(self):
        parent_uid = self.folder.get_folders()[1].get("uid")

        folder_uid_a = self.folder.create_folder("test11", parent_uid=parent_uid)["uid"]
        folder_uid_b = self.folder.create_folder("test12")["uid"]

        self.assertEqual("test12", self.folder.get_folder_by_uid(folder_uid_b)["title"])

        moved_folder: dict = self.folder.move_folder(
            folder_uid_a, parent_uid=folder_uid_b
        )

        self.assertEqual("test12", moved_folder["parents"][0]["title"])
        self.folder.delete_folder(moved_folder["parents"][0]["uid"])

    def test_e_delete_folder(self):
        self.folder.delete_folder(self.folder.get_folders()[1].get("uid"))

        self.assertEqual(1, len(self.folder.get_folders()))

    def test_get_folder_permissions(self):
        self.assertEqual(
            1,
            self.folder.get_folder_permissions("6U_QdWJnz")[0]["permission"],
        )

    def test_f_update_folder_permissions(self):
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

    def test_get_folder_id_by_dashboard_path_general_folder(self):
        self.assertEqual(
            0, self.folder.get_folder_id_by_dashboard_path("General")
        )

    def test_get_all_folder_ids_uids_and_names(self):
        self.assertEqual(
            list([{"id": 72, "uid": "6U_QdWJnz", "title": "Github Integrationtest"}]),
            self.folder.get_all_folder_ids_uids_and_names(),
        )
