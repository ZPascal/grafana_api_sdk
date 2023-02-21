from unittest import TestCase

from grafana_api.model import (
    APIModel,
    RequestsMethods,
    APIEndpoints,
    DatasourceQuery,
)


class APIEndpointsTestCase(TestCase):
    def test_api_endpoints_init(self):
        self.assertEqual("APIEndpoints.DASHBOARDS", str(APIEndpoints.DASHBOARDS))
        self.assertEqual("APIEndpoints.SEARCH", str(APIEndpoints.SEARCH))


class RequestsMethodsTestCase(TestCase):
    def test_requests_methods_init(self):
        self.assertEqual("RequestsMethods.GET", str(RequestsMethods.GET))
        self.assertEqual("RequestsMethods.PUT", str(RequestsMethods.PUT))
        self.assertEqual("RequestsMethods.POST", str(RequestsMethods.POST))
        self.assertEqual("RequestsMethods.PATCH", str(RequestsMethods.PATCH))
        self.assertEqual("RequestsMethods.DELETE", str(RequestsMethods.DELETE))


class APIModelTestCase(TestCase):
    def test_api_model_init(self):
        model = APIModel(host="test", token="test")

        self.assertEqual("test", model.host)
        self.assertEqual("test", model.token)

    def test_api_model_init_basic_auth(self):
        model = APIModel(host="test", username="test", password="test")

        self.assertEqual("test", model.host)
        self.assertEqual("test", model.username)
        self.assertEqual("test", model.password)


class DatasourceQueryTestCase(TestCase):
    def test_datasource_query_init(self):
        datasource_query = DatasourceQuery(datasource_id=1, raw_sql="TEST")

        self.assertEqual(1, datasource_query.datasource_id)
        self.assertEqual("TEST", datasource_query.raw_sql)
        self.assertEqual("A", datasource_query.ref_id)
        self.assertEqual(1000, datasource_query.interval_ms)
        self.assertEqual(100, datasource_query.max_data_points)
        self.assertEqual("time_series", datasource_query.output_format)
