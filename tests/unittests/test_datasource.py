from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, DatasourceQuery, DatasourceCache
from grafana_api.datasource import Datasource, DatasourceQueryResourceCaching


class DatasourceTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual([{"id": 1}], datasource.get_all_datasources())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_datasources_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            datasource.get_all_datasources()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual({"id": 1}, datasource.get_datasource_by_id(1))

    def test_get_datasource_by_id_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual({"id": 1}, datasource.get_datasource_by_uid("test"))

    def test_get_datasource_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual({"id": 1}, datasource.get_datasource_by_name("test"))

    def test_get_datasource_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_name("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(1, datasource.get_datasource_id_by_name("test"))

    def test_get_datasource_id_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_id_by_name("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name_no_id_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_id_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Datasource added"})

        self.assertEqual(None, datasource.create_datasource(dict({"test": "test"})))

    def test_create_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.create_datasource(dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_datasource_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.create_datasource(dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Datasource updated"})

        self.assertEqual(None, datasource.update_datasource(1, dict({"test": "test"})))

    def test_update_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.update_datasource(1, dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.update_datasource(1, dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Data source deleted"})

        self.assertEqual(None, datasource.delete_datasource_by_id(1))

    def test_delete_datasource_by_id_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Data source deleted"})

        self.assertEqual(None, datasource.delete_datasource_by_uid("test"))

    def test_delete_datasource_by_uid_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_uid_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Data source deleted"})

        self.assertEqual(None, datasource.delete_datasource_by_name("test"))

    def test_delete_datasource_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_name("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"results": dict({"test": "test"})})

        datasource_query: DatasourceQuery = DatasourceQuery(1, "test")
        datasource_queries: list = list()
        datasource_queries.append(datasource_query)

        self.assertEqual(
            dict({"test": "test"}),
            datasource.query_datasource_by_id("1234", "1234", datasource_queries),
        )

    def test_query_datasource_by_id_no_time(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.query_datasource_by_id("", "", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_no_query_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        datasource_query: DatasourceQuery = DatasourceQuery(1, "test")
        datasource_queries: list = list()
        datasource_queries.append(datasource_query)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.query_datasource_by_id("1234", "1234", datasource_queries)

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "Datasource permissions enabled"}
        )

        self.assertEqual(None, datasource.enable_datasource_permissions(1))

    def test_enable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.enable_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions_enable_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.enable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "Datasource permissions disabled"}
        )

        self.assertEqual(None, datasource.disable_datasource_permissions(1))

    def test_disable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.disable_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions_disable_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.disable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"datasourceId": "Test"})

        self.assertEqual(
            dict({"datasourceId": "Test"}), datasource.get_datasource_permissions(1)
        )

    def test_get_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_no_datasource_permissions_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "Datasource permission added"}
        )

        self.assertEqual(
            None, datasource.add_datasource_permissions(1, dict({"test": "test"}))
        )

    def test_add_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.add_datasource_permissions(0, dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions_permission_add_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.add_datasource_permissions(1, dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "Datasource permission removed"}
        )

        self.assertEqual(None, datasource.delete_datasource_permissions(1, 1))

    def test_delete_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_permissions(0, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.delete_datasource_permissions(1, 1)


class DatasourceQueryResourceCachingTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"dataSourceID": 1})

        self.assertEqual({"dataSourceID": 1}, datasource.get_datasource_cache("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            datasource.get_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.get_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"dataSourceID": 1})

        self.assertEqual(
            {"dataSourceID": 1}, datasource.enable_datasource_cache("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            datasource.enable_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.enable_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"dataSourceID": 1})

        self.assertEqual(
            {"dataSourceID": 1}, datasource.disable_datasource_cache("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            datasource.disable_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.disable_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict({"dataSourceID": 1})

        self.assertEqual({"dataSourceID": 1}, datasource.clean_datasource_cache("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            datasource.clean_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.clean_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )
        datasource_cache: DatasourceCache = DatasourceCache(
            1, "test1", True, False, 12, 14
        )

        call_the_api_mock.return_value = dict({"dataSourceID": 2})

        self.assertEqual(
            {"dataSourceID": 2},
            datasource.update_datasource_cache("test", datasource_cache),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_cache_no_valid_datasource_cache_object(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )
        datasource_cache: DatasourceCache = DatasourceCache(
            0, "test1", True, False, 12, 14
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            datasource.update_datasource_cache("test", datasource_cache)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )
        datasource_cache: DatasourceCache = DatasourceCache(
            1, "test1", True, False, 12, 14
        )

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            datasource.update_datasource_cache("test", datasource_cache)
