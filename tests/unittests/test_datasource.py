import warnings
from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.api import Api
from grafana_api.model import (
    APIModel,
    DatasourceQuery,
    DatasourceCache,
    DatasourcePermission,
)
from grafana_api.datasource import (
    Datasource,
    DatasourcePermissions,
    DatasourceLegacyPermissions,
    DatasourceQueryResourceCaching,
    DatasourceLabelBasedAccessControl,
)


class DatasourceTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = [{"id": 1}]

        self.assertEqual([{"id": 1}], datasource.get_all_datasources())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_datasources_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_all_datasources()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id_fallback_scan_exception(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.side_effect = [{}, Exception("test")]

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_id_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Datasource added"}

        self.assertEqual(None, datasource.create_datasource({"test": "test"}))

    def test_create_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.create_datasource({})

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_datasource_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.create_datasource({"test": "test"})

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_use_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Datasource updated"}

        self.assertEqual(None, datasource.update_datasource({"test": "test"}, datasource_id=1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_use_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Datasource updated"}

        self.assertEqual(None, datasource.update_datasource({"test": "test"}, datasource_uid="test"))

    def test_update_datasource_no_data_source(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.update_datasource({}, datasource_id=1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.update_datasource({"test": "test"}, datasource_id=1)

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.datasource.Datasource.get_datasource_by_id")
    def test_update_datasource_fallback_id_empty(
        self, get_datasource_by_id_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}
        get_datasource_by_id_mock.return_value = {"uid": ""}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.update_datasource({"test": "test"}, datasource_id=1)

    @patch("grafana_api.api.Api.call_the_api")
    @patch("grafana_api.datasource.Datasource.get_datasource_by_id")
    def test_update_datasource_fallback_by_id_not_updated(
        self, get_datasource_by_id_mock, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.side_effect = [{}, {"message": "not updated"}]
        get_datasource_by_id_mock.return_value = {"uid": "uid-1"}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.update_datasource({"test": "test"}, datasource_id=1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Data source deleted"}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.delete_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id_fallback_by_uid(
        self,
        call_the_api_mock,
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Data source deleted"}

        self.assertIsNone(datasource.delete_datasource_by_id(1))

    @patch("grafana_api.datasource.Datasource.get_datasource_by_id")
    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id_fallback_uid_empty(
        self, call_the_api_mock, get_datasource_by_id_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}
        get_datasource_by_id_mock.return_value = {"uid": ""}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.delete_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Data source deleted"}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.delete_datasource_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Data source deleted"}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.delete_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"test": "test"}}

        datasource_query: DatasourceQuery = DatasourceQuery("test", datasource_id=1)
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        self.assertEqual(
            {"test": "test"},
            datasource.query_datasource_by_id("1234", "1234", datasource_queries),
        )

    def test_query_datasource_by_id_no_time(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.query_datasource_by_id("", "", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_no_value_datasource_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"test": "test"}}

        datasource_query: DatasourceQuery = DatasourceQuery("test", datasource_id=0)
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        with self.assertRaises(ValueError):
            datasource.query_datasource_by_id("1234", "1234", datasource_queries)

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_no_query_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        datasource_query: DatasourceQuery = DatasourceQuery("test", datasource_id=1)
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.query_datasource_by_id("1234", "1234", datasource_queries)

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"test": "test"}}

        datasource_query: DatasourceQuery = DatasourceQuery("test", datasource_uid="test")
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        self.assertEqual(
            {"test": "test"},
            datasource.query_datasource_by_uid("1234", "1234", datasource_queries),
        )

    def test_query_datasource_by_uid_no_time(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.query_datasource_by_uid("", "", MagicMock())

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_uid_no_value_datasource_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"test": "test"}}

        datasource_query: DatasourceQuery = DatasourceQuery("test")
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        with self.assertRaises(ValueError):
            datasource.query_datasource_by_uid("1234", "1234", datasource_queries)

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_uid_no_query_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        datasource_query: DatasourceQuery = DatasourceQuery("test", datasource_uid="test")
        datasource_queries: list = []
        datasource_queries.append(datasource_query)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.query_datasource_by_uid("1234", "1234", datasource_queries)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_health_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {
            "status": "OK",
            "message": "Data source is working",
        }

        self.assertEqual(
            {"status": "OK", "message": "Data source is working"},
            datasource.get_datasource_health_by_uid("test"),
        )

    def test_get_datasource_health_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_health_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_health_by_uid_not_healthy(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"status": "ERROR", "message": "failed"}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_health_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_health_by_uid_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_health_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"data": ["a"]}

        self.assertEqual(
            {"data": ["a"]},
            datasource.get_datasource_resource_by_uid("test", "/labels"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_nested_path_and_query(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = ["a"]

        self.assertEqual(
            ["a"],
            datasource.get_datasource_resource_by_uid(
                "test", "api/v1/label/job/values?start=1"
            ),
        )

    def test_get_datasource_resource_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("", "labels")

    def test_get_datasource_resource_by_uid_no_resource_path(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("test", "")

    def test_get_datasource_resource_by_uid_only_slash_as_resource_path(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("test", "/")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_path_traversal_parent_directory(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("test", "..")

        call_the_api_mock.assert_not_called()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_path_traversal_leading_parent_directory(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("test", "../../dashboards")

        call_the_api_mock.assert_not_called()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_path_traversal_inner_parent_directory(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertRaises(ValueError):
            datasource.get_datasource_resource_by_uid("test", "labels/../../../org")

        call_the_api_mock.assert_not_called()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_empty_dict_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        self.assertEqual(
            {}, datasource.get_datasource_resource_by_uid("test", "labels")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_empty_list_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = []

        self.assertEqual(
            [], datasource.get_datasource_resource_by_uid("test", "labels")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_text_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = "test"

        self.assertEqual(
            "test", datasource.get_datasource_resource_by_uid("test", "labels")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_number_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = 1

        self.assertEqual(
            1, datasource.get_datasource_resource_by_uid("test", "labels")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_uid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"A": {"status": 200}}}

        self.assertEqual(
            {"A": {"status": 200}},
            datasource.query_datasource_by_uid(
                "now-1h", "now", [DatasourceQuery("SELECT 1", datasource_uid="test")]
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"results": {"A": {"status": 200}}}

        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                {"A": {"status": 200}},
                datasource.query_datasource_by_id(
                    "now-1h", "now", [DatasourceQuery("SELECT 1", datasource_id=1)]
                ),
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "bad request data"}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.query_datasource_by_uid(
                "now-1h", "now", [DatasourceQuery("SELECT 1", datasource_uid="test")]
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_id_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.get_datasource_by_id is deprecated"):
            datasource.get_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.get_datasource_by_name is deprecated"):
            datasource.get_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_id_by_name_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.get_datasource_id_by_name is deprecated"):
            datasource.get_datasource_id_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_id_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.delete_datasource_by_id is deprecated"):
            datasource.delete_datasource_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_by_name_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.delete_datasource_by_name is deprecated"):
            datasource.delete_datasource_by_name("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_query_datasource_by_id_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with self.assertWarnsRegex(DeprecationWarning, "^Datasource.query_datasource_by_id is deprecated"):
            datasource.query_datasource_by_id(
                "now-1h", "now", [DatasourceQuery("A", datasource_id=1)]
            )

    def test_get_datasource_by_id_warning_says_the_endpoint_was_removed(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertWarnsRegex(DeprecationWarning, "endpoint was removed"):
            with self.assertRaises(ValueError):
                datasource.get_datasource_by_id(0)

    def test_delete_datasource_by_id_warning_says_the_endpoint_was_removed(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertWarnsRegex(DeprecationWarning, "endpoint was removed"):
            with self.assertRaises(ValueError):
                datasource.delete_datasource_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_name_warning_does_not_say_removed(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "message": "Data source deleted", "results": {"A": 1}}

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            datasource.get_datasource_by_name("test")

        self.assertNotIn("removed", str(caught[0].message))

    def test_deprecated_methods_keep_their_name(self):
        self.assertEqual("get_datasource_by_id", Datasource.get_datasource_by_id.__name__)

    def test_removed_method_docstring_says_removed(self):
        self.assertIn("REMOVED", Datasource.get_datasource_by_id.__doc__)

    def test_deprecated_method_docstring_says_deprecated(self):
        self.assertIn("DEPRECATED", Datasource.get_datasource_by_name.__doc__)

    def test_deprecation_warning_points_to_the_caller(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        with self.assertWarns(DeprecationWarning) as context:
            with self.assertRaises(ValueError):
                datasource.get_datasource_by_id(0)

        self.assertEqual(__file__, context.filename)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_by_uid_does_not_warn(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "status": "OK"}

        with warnings.catch_warnings():
            warnings.simplefilter("error")

            datasource.get_datasource_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_health_by_uid_does_not_warn(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "status": "OK"}

        with warnings.catch_warnings():
            warnings.simplefilter("error")

            datasource.get_datasource_health_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_resource_by_uid_does_not_warn(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: Datasource = Datasource(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 1, "status": "OK"}

        with warnings.catch_warnings():
            warnings.simplefilter("error")

            datasource.get_datasource_resource_by_uid("test", "labels")


class DatasourcePermissionsTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "test": "test"}

        self.assertEqual(
            {"status": 200, "test": "test"},
            datasource_permissions.get_datasource_permissions_by_uid("test"),
        )

    def test_get_datasource_permissions_by_uid_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            datasource_permissions.get_datasource_permissions_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_by_uid_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 401}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.get_datasource_permissions_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_by_uid_general_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 600}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.get_datasource_permissions_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_add(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission updated"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission("edit")
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_remove(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission removed"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission(None)
            ),
        )

    def test_update_datasource_user_access_by_uid_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            datasource_permissions.update_datasource_user_access_by_uid(
                "", 0, DatasourcePermission(None)
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_permission_denied(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission("edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 401}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission("edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_general_error(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 600}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission("edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_add(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission updated"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission("edit")
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_remove(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission removed"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission(None)
            ),
        )

    def test_update_datasource_team_access_by_uid_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            datasource_permissions.update_datasource_team_access_by_uid(
                "", 0, DatasourcePermission(None)
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_permission_denied(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission("Edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 401}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission("Edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_general_error(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 600}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission("Edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_add(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission updated"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "test", DatasourcePermission("admin")
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_remove(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 200, "message": "Permission removed"}

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "test", DatasourcePermission(None)
            ),
        )

    def test_update_datasource_basic_role_access_by_uid_no_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        with self.assertRaises(ValueError):
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "", "", DatasourcePermission(None)
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_permission_denied(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "test", DatasourcePermission("edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 401}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "test", DatasourcePermission("edit")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_general_error(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"status": 600}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "test", DatasourcePermission("query")
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_by_uid_with_ds_type(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = [{"status": 200}]

        self.assertEqual(
            [{"status": 200}],
            datasource_permissions.get_datasource_permissions_by_uid(
                "test", ds_type="prometheus"
            ),
        )

    @patch("grafana_api.api.Api._execute_the_api_call")
    def test_get_datasource_permissions_by_uid_real_response(
        self, execute_the_api_call_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        response: MagicMock = MagicMock()
        response.text = '[{"id": 1, "permission": "Query"}]'
        response.status_code = 200

        execute_the_api_call_mock.side_effect = (
            lambda http, method, api_url, response_status_code, json_complete: Api._check_the_api_call_response(
                response, response_status_code
            )
        )

        self.assertEqual(
            [{"id": 1, "permission": "Query", "status": 200}],
            datasource_permissions.get_datasource_permissions_by_uid("test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_user_access_by_uid_with_ds_type(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {
            "status": 200,
            "message": "Permission updated",
        }

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_user_access_by_uid(
                "test", 1, DatasourcePermission("Edit"), ds_type="loki"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_team_access_by_uid_with_ds_type(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {
            "status": 200,
            "message": "Permission updated",
        }

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_team_access_by_uid(
                "test", 1, DatasourcePermission("Edit"), ds_type="loki"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_datasource_basic_role_access_by_uid_with_ds_type(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_permissions: DatasourcePermissions = DatasourcePermissions(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {
            "status": 200,
            "message": "Permission updated",
        }

        self.assertEqual(
            None,
            datasource_permissions.update_datasource_basic_role_access_by_uid(
                "test", "Viewer", DatasourcePermission("Query"), ds_type="loki"
            ),
        )

class DatasourceLegacyPermissionsTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permissions enabled"}

        self.assertEqual(
            None, datasource_legacy_permissions.enable_datasource_permissions(1)
        )

    def test_enable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        with self.assertRaises(ValueError):
            datasource_legacy_permissions.enable_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions_enable_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_legacy_permissions.enable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permissions disabled"}

        self.assertEqual(
            None, datasource_legacy_permissions.disable_datasource_permissions(1)
        )

    def test_disable_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        with self.assertRaises(ValueError):
            datasource_legacy_permissions.disable_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions_disable_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_legacy_permissions.disable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"datasourceId": "Test"}

        self.assertEqual(
            {"datasourceId": "Test"},
            datasource_legacy_permissions.get_datasource_permissions(1),
        )

    def test_get_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        with self.assertRaises(ValueError):
            datasource_legacy_permissions.get_datasource_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_no_datasource_permissions_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_legacy_permissions.get_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permission added"}

        self.assertEqual(
            None,
            datasource_legacy_permissions.add_datasource_permissions(
                1, {"test": "test"}
            ),
        )

    def test_add_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        with self.assertRaises(ValueError):
            datasource_legacy_permissions.add_datasource_permissions(0, {})

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions_permission_add_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_legacy_permissions.add_datasource_permissions(
                1, {"test": "test"}
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permission removed"}

        self.assertEqual(
            None, datasource_legacy_permissions.delete_datasource_permissions(1, 1)
        )

    def test_delete_datasource_permissions_no_datasource_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        with self.assertRaises(ValueError):
            datasource_legacy_permissions.delete_datasource_permissions(0, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource_legacy_permissions.delete_datasource_permissions(1, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_permissions_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permissions enabled"}

        with self.assertWarnsRegex(DeprecationWarning, "^DatasourceLegacyPermissions.enable_datasource_permissions is deprecated"):
            datasource_legacy_permissions.enable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_permissions_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permissions disabled"}

        with self.assertWarnsRegex(DeprecationWarning, "^DatasourceLegacyPermissions.disable_datasource_permissions is deprecated"):
            datasource_legacy_permissions.disable_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_permissions_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"datasourceId": 1}

        with self.assertWarnsRegex(DeprecationWarning, "^DatasourceLegacyPermissions.get_datasource_permissions is deprecated"):
            datasource_legacy_permissions.get_datasource_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_datasource_permissions_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permission added"}

        with self.assertWarnsRegex(DeprecationWarning, "^DatasourceLegacyPermissions.add_datasource_permissions is deprecated"):
            datasource_legacy_permissions.add_datasource_permissions(1, {"test": "test"})

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_datasource_permissions_is_deprecated(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource_legacy_permissions: DatasourceLegacyPermissions = (
            DatasourceLegacyPermissions(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"message": "Datasource permission removed"}

        with self.assertWarnsRegex(DeprecationWarning, "^DatasourceLegacyPermissions.delete_datasource_permissions is deprecated"):
            datasource_legacy_permissions.delete_datasource_permissions(1, 1)


class DatasourceQueryResourceCachingTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"dataSourceID": 1}

        self.assertEqual({"dataSourceID": 1}, datasource.get_datasource_cache("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            datasource.get_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"dataSourceID": 1}

        self.assertEqual(
            {"dataSourceID": 1}, datasource.enable_datasource_cache("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            datasource.enable_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_enable_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.enable_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"dataSourceID": 1}

        self.assertEqual(
            {"dataSourceID": 1}, datasource.disable_datasource_cache("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            datasource.disable_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_disable_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.disable_datasource_cache("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {"dataSourceID": 1}

        self.assertEqual({"dataSourceID": 1}, datasource.clean_datasource_cache("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache_no_datasources(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            datasource.clean_datasource_cache("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_clean_datasource_cache_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceQueryResourceCaching = DatasourceQueryResourceCaching(
            grafana_api_model=model
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
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

        call_the_api_mock.return_value = {"dataSourceID": 2}

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

        call_the_api_mock.return_value = {}

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

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.update_datasource_cache("test", datasource_cache)


class DatasourceLabelBasedAccessControlTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_lbac_rules_for_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = [{"id": 1}]

        self.assertEqual([{"id": 1}], datasource.get_lbac_rules_for_datasource("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_lbac_rules_for_datasource_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = None

        with self.assertRaises(ValueError):
            datasource.get_lbac_rules_for_datasource("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_lbac_rules_for_datasource_no_valid_rules(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = None

        with self.assertRaises(Exception):  # noqa: B017
            datasource.get_lbac_rules_for_datasource("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_lbac_rules_for_datasource(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {"dataSourceID": 1}

        self.assertEqual(
            {"dataSourceID": 1}, datasource.update_lbac_rules_for_datasource("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_lbac_rules_for_datasource_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = None

        with self.assertRaises(ValueError):
            datasource.update_lbac_rules_for_datasource("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_lbac_rules_for_datasource_no_update_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        datasource: DatasourceLabelBasedAccessControl = (
            DatasourceLabelBasedAccessControl(grafana_api_model=model)
        )

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            datasource.update_lbac_rules_for_datasource("test")
