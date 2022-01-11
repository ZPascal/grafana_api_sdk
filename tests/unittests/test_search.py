from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.search import Search


class SearchTestCase(TestCase):

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_search(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        search: Search = Search(grafana_api_model=model)

        call_the_api_mock.return_value = ["test"]

        self.assertEqual(["test"], search.search(search_query=MagicMock()))

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_search_unvalid_empty_list(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        search: Search = Search(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            search.search(search_query=MagicMock())

    @patch("src.grafana_api.utils.Utils.call_the_api")
    def test_search_unvalid_output(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        search: Search = Search(grafana_api_model=model)

        call_the_api_mock.side_effect = Exception

        with self.assertRaises(Exception):
            search.search(search_query=MagicMock())
