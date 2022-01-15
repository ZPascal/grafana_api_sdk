from unittest import TestCase

from src.grafana_api.model import APIModel, RequestsMethods, APIEndpoints


class APIEndpointsTestCase(TestCase):
    def test_api_endpoints_init(self):
        self.assertEqual("APIEndpoints.DASHBOARDS", str(APIEndpoints.DASHBOARDS))
        self.assertEqual("APIEndpoints.SEARCH", str(APIEndpoints.SEARCH))


class RequestsMethodsTestCase(TestCase):
    def test_requests_methods_init(self):
        self.assertEqual("RequestsMethods.GET", str(RequestsMethods.GET))
        self.assertEqual("RequestsMethods.POST", str(RequestsMethods.POST))
        self.assertEqual("RequestsMethods.DELETE", str(RequestsMethods.DELETE))


class APIModelTestCase(TestCase):
    def test_api_model_init(self):
        model = APIModel(host="test", token="test")

        self.assertEqual("test", model.host)
        self.assertEqual("test", model.token)
