from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel, DatasourceQuery
from src.grafana_api.datasource import Datasource


class DatasourceTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual([{"id": 1}], datasource.get_all_datasources())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_datasources_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_all_datasources()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual({"id": 1}, datasource.get_datasource_by_id(1))

    def test_get_datasource_by_id_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_datasource_by_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual({"id": 1}, datasource.get_datasource_by_uid("test"))

    def test_get_datasource_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_uid("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_datasource_by_uid("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual({"id": 1}, datasource.get_datasource_by_name("test"))

    def test_get_datasource_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_by_name("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name_no_datasource_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_datasource_by_name("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(1, datasource.get_datasource_id_by_name("test"))

    def test_get_datasource_id_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_id_by_name("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name_no_id_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_datasource_id_by_name("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Datasource added"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.create_datasource(dict({"test": "test"})))

    def test_create_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.create_datasource(dict())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_datasource_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.create_datasource(dict({"test": "test"}))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Datasource updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.update_datasource(1, dict({"test": "test"})))

    def test_update_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.update_datasource(1, dict())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_datasource_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.update_datasource(1, dict({"test": "test"}))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Data source deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.delete_datasource_by_id(1))

    def test_delete_datasource_by_id_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Data source deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.delete_datasource_by_uid("test"))

    def test_delete_datasource_by_uid_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_uid("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_uid_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_uid("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Data source deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.delete_datasource_by_name("test"))

    def test_delete_datasource_by_name_no_name(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_by_name("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.delete_datasource_by_name("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"results": dict({"test": "test"})}))

        call_the_api_mock.return_value = mock

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

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_no_query_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        datasource_query: DatasourceQuery = DatasourceQuery(1, "test")
        datasource_queries: list = list()
        datasource_queries.append(datasource_query)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.query_datasource_by_id("1234", "1234", datasource_queries)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict({"message": "Datasource permissions enabled"})
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.enable_datasource_permissions(1))

    def test_enable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.enable_datasource_permissions(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions_enable_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.enable_datasource_permissions(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict({"message": "Datasource permissions disabled"})
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.disable_datasource_permissions(1))

    def test_disable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.disable_datasource_permissions(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions_disable_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.disable_datasource_permissions(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"datasourceId": "Test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"datasourceId": "Test"}), datasource.get_datasource_permissions(1)
        )

    def test_get_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_permissions(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_no_datasource_permissions_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.get_datasource_permissions(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Datasource permission added"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, datasource.add_datasource_permissions(1, dict({"test": "test"}))
        )

    def test_add_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.add_datasource_permissions(0, dict())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions_permission_add_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.add_datasource_permissions(1, dict({"test": "test"}))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict({"message": "Datasource permission removed"})
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(None, datasource.delete_datasource_permissions(1, 1))

    def test_delete_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.delete_datasource_permissions(0, 1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            datasource.delete_datasource_permissions(1, 1)
