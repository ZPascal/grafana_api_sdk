from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from grafana_api.model import APIModel
from grafana_api.authentication import Authentication


class AuthenticationTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_api_tokens(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": "test"}])

        self.assertEqual(
            list([{"id": "test"}]),
            authentication.get_api_tokens(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_api_tokens_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": None}])

        with self.assertRaises(Exception):
            authentication.get_api_tokens()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_api_token(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            authentication.create_api_token("name", "View"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_api_token_no_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            authentication.create_api_token("", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_api_token_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            authentication.create_api_token("name", "View")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_api_token(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "API key deleted"})

        self.assertEqual(
            None,
            authentication.delete_api_token(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_api_token_no_token_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            authentication.delete_api_token(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_api_token_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        authentication: Authentication = Authentication(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            authentication.delete_api_token(1)
