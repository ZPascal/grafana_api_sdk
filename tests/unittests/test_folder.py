from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.folder import Folder


class FolderTestCase(TestCase):
    @patch("src.grafana_api.folder.Folder.get_all_folder_ids_and_names")
    def test_get_folder_id_by_dashboard_path(self, all_folder_ids_and_names_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_and_names_mock.return_value = [{"title": None, "id": 12}]
        self.assertEqual(12, folder.get_folder_id_by_dashboard_path())

    @patch("src.grafana_api.folder.Folder.get_all_folder_ids_and_names")
    def test_get_folder_id_by_dashboard_path_no_title_match(
        self, all_folder_ids_and_names_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        folder: Folder = Folder(grafana_api_model=model)

        all_folder_ids_and_names_mock.return_value = [{"title": "test", "id": "xty13y"}]
        with self.assertRaises(Exception):
            folder.get_folder_id_by_dashboard_path()

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_get_all_folder_ids_and_names(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        folder: Folder = Folder(grafana_api_model=model)

        call_the_api_mock.return_value = [{"title": "test", "id": 12, "test": "test"}]
        self.assertEqual(
            [{"title": "test", "id": 12}], folder.get_all_folder_ids_and_names()
        )
