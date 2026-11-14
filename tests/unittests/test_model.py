from unittest import TestCase

from grafana_api.model import (
    APIModel,
    RequestsMethods,
    APIEndpoints,
    DatasourceQuery,
    DatasourcePermission,
    Route,
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


class DatasourcePermissionTestCase(TestCase):
    def test_datasource_permission_init_value_error(self):
        with self.assertRaises(ValueError):
            DatasourcePermission("")


class RouteTestCase(TestCase):
    def test_route_init_receiver_only(self):
        route = Route(receiver="test")

        self.assertEqual("test", route.receiver)
        self.assertIsNone(route.continue_parameter)
        self.assertIsNone(route.group_by_str)
        self.assertIsNone(route.provenance)
        self.assertIsNone(route.object_matchers)
        self.assertIsNone(route.routes)

    def test_route_init_without_receiver(self):
        self.assertIsNone(Route().receiver)

    def test_route_init_positional_order(self):
        route = Route(False, ["test1"], "test2", "test3")

        self.assertFalse(route.continue_parameter)
        self.assertEqual(["test1"], route.group_by_str)
        self.assertEqual("test2", route.receiver)
        self.assertEqual("test3", route.provenance)
