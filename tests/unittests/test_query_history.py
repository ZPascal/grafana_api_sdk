from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, QueryObject, QueryDatasourceObject
from grafana_api.query_history import QueryHistory


class QueryHistoryTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_add_query_to_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        query_datasource: QueryDatasourceObject = QueryDatasourceObject("test", "test")
        query: QueryObject = QueryObject("test", "test", "test", query_datasource)

        call_the_api_mock.return_value = dict({"result": "test"})

        self.assertEqual(
            dict({"result": "test"}),
            query_history.add_query_to_history("test", [query]),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_query_to_history_no_datasource_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.add_query_to_history("", [])

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_query_to_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        query_datasource: QueryDatasourceObject = QueryDatasourceObject("test", "test")
        query: QueryObject = QueryObject("test", "test", "test", query_datasource)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            query_history.add_query_to_history("test", [query])

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_query_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"result": "test"})

        self.assertEqual(
            dict({"result": "test"}),
            query_history.search_query_history(["test", "test"], "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_query_history_no_datasource_uids(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.search_query_history([], "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_query_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            query_history.search_query_history(["test"], "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_query_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Query deleted"})

        self.assertEqual(None, query_history.delete_query_history("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_query_history_no_datasource_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.delete_query_history("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_query_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            query_history.delete_query_history("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_query_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"result": "test"})

        self.assertEqual(
            dict({"result": "test"}), query_history.update_query_history("test", "test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_query_history_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.update_query_history("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_query_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            query_history.update_query_history("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_query_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"result": "test"})

        self.assertEqual(
            dict({"result": "test"}), query_history.star_query_history("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_query_history_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.star_query_history("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_query_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            query_history.star_query_history("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_query_history(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"result": "test"})

        self.assertEqual(
            dict({"result": "test"}), query_history.unstar_query_history("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_query_history_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            query_history.unstar_query_history("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_query_history_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        query_history: QueryHistory = QueryHistory(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            query_history.unstar_query_history("test")
