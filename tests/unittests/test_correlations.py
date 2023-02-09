from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, CorrelationObject
from grafana_api.correlations import Correlations


class CorrelationsTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_create_correlations(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)
        correlation_object: CorrelationObject = CorrelationObject(
            "test", "test", "test", "test", "test", "test"
        )

        call_the_api_mock.return_value = dict({"message": "test"})

        self.assertEqual(
            dict({"message": "test"}),
            correlations.create_correlations(correlation_object),
        )

    def test_create_correlations_no_source_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)
        correlation_object: CorrelationObject = CorrelationObject(
            "test", "test", "test", "test", "test", ""
        )

        with self.assertRaises(ValueError):
            correlations.create_correlations(correlation_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_correlations_creation_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)
        correlation_object: CorrelationObject = CorrelationObject(
            "test", "test", "test", "test", "test", "test"
        )

        call_the_api_mock.return_value = dict({"status": "error"})

        with self.assertRaises(Exception):
            correlations.create_correlations(correlation_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_correlations(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Correlation deleted"})

        self.assertEqual(None, correlations.delete_correlations("test", "test"))

    def test_delete_correlations_no_source_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        with self.assertRaises(ValueError):
            correlations.delete_correlations("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_correlations_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            correlations.delete_correlations("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_correlations(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        self.assertEqual(
            dict({"message": "test"}),
            correlations.update_correlations("test", "test", "test", "test"),
        )

    def test_update_correlations_no_source_datasource_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        with self.assertRaises(ValueError):
            correlations.update_correlations("", "", "", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_correlations_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        correlations: Correlations = Correlations(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": None})

        with self.assertRaises(Exception):
            correlations.update_correlations("test", "test", "test", "test")
