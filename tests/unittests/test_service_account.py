from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from grafana_api.model import APIModel
from grafana_api.service_account import ServiceAccount


class ServiceAccountTestCase(TestCase):
    model: APIModel = APIModel(
        host=MagicMock(), username=MagicMock(), password=MagicMock()
    )
    service_account: ServiceAccount = ServiceAccount(grafana_api_model=model)

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"totalCount": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"totalCount": 2}),
            self.service_account.search_service_account(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account_specify_query(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"totalCount": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"totalCount": 2}),
            self.service_account.search_service_account(query="test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account_no_valid_result(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.search_service_account()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 2}),
            self.service_account.create_service_account("test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_no_name(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.create_service_account("", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_no_valid_result(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.create_service_account("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 2}),
            self.service_account.get_service_account_by_id(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.get_service_account_by_id(0),

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id_no_valid_result(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.get_service_account_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 2}),
            self.service_account.update_service_account(1, "test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.update_service_account(0, "", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_no_valid_result(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.update_service_account(1, "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_token_by_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 2}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"id": 2}]),
            self.service_account.get_service_account_token_by_id(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_token_by_id_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 2}]))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.get_service_account_token_by_id(0),

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_token_by_id_no_valid_result(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.get_service_account_token_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 2}),
            self.service_account.create_service_account_token_by_id(1, "test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.create_service_account_token_by_id(0, "", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id_no_valid_result(
        self, call_the_api_mock
    ):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.create_service_account_token_by_id(1, "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "API key deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            self.service_account.delete_service_account_token_by_id(1, 1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 2}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.service_account.delete_service_account_token_by_id(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id_no_valid_result(
        self, call_the_api_mock
    ):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.service_account.delete_service_account_token_by_id(1, 1)
