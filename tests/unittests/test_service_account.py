from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.service_account import ServiceAccount


class ServiceAccountTestCase(TestCase):
    model: APIModel = APIModel(
        host=MagicMock(), username=MagicMock(), password=MagicMock()
    )
    service_account: ServiceAccount = ServiceAccount(grafana_api_model=model)

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account(self, call_the_api_mock):
        call_the_api_mock.return_value = {"totalCount": 2}

        self.assertEqual(
            {"totalCount": 2},
            self.service_account.search_service_account(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account_specify_query(self, call_the_api_mock):
        call_the_api_mock.return_value = {"totalCount": 2}

        self.assertEqual(
            {"totalCount": 2},
            self.service_account.search_service_account(query="test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_service_account_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.search_service_account()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        self.assertEqual(
            {"id": 2},
            self.service_account.create_service_account("test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_no_name(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.create_service_account("", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.create_service_account("test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        self.assertEqual(
            {"id": 2},
            self.service_account.get_service_account_by_id(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.get_service_account_by_id(0),

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_by_id_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.get_service_account_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        self.assertEqual(
            {"id": 2},
            self.service_account.update_service_account(1, "test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.update_service_account(0, "", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.update_service_account(1, "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(ValueError):
            self.service_account.delete_service_account(0),

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = {"status": 400}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.delete_service_account(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "Service account deleted"}

        self.assertEqual(
            None,
            self.service_account.delete_service_account(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_tokens_by_id(self, call_the_api_mock):
        call_the_api_mock.return_value = [{"id": 2}]

        self.assertEqual(
            [{"id": 2}],
            self.service_account.get_service_account_tokens_by_id(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_tokens_by_id_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = [{"id": 2}]

        with self.assertRaises(ValueError):
            self.service_account.get_service_account_tokens_by_id(0),

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_tokens_by_id_no_valid_result(self, call_the_api_mock):
        call_the_api_mock.return_value = [{"id": None}]

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.get_service_account_tokens_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        self.assertEqual(
            {"id": 2},
            self.service_account.create_service_account_token_by_id(1, "test", "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.create_service_account_token_by_id(0, "", ""),

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_service_account_token_by_id_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.create_service_account_token_by_id(1, "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "Service account token deleted"}

        self.assertEqual(
            None,
            self.service_account.delete_service_account_token_by_id(1, 1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.delete_service_account_token_by_id(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_service_account_token_by_id_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.delete_service_account_token_by_id(1, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_migrate_api_keys_to_service_accounts(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "API keys migrated to service accounts"}

        self.assertEqual(
            None,
            self.service_account.migrate_api_keys_to_service_accounts(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_migrate_api_keys_to_service_accounts_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.migrate_api_keys_to_service_accounts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_migrate_api_key_to_service_account(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "Service accounts migrated"}

        self.assertEqual(
            None,
            self.service_account.migrate_api_key_to_service_account(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_migrate_api_key_to_service_account_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(ValueError):
            self.service_account.migrate_api_key_to_service_account(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_migrate_api_key_to_service_account_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.migrate_api_key_to_service_account(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_migration_status(self, call_the_api_mock):
        call_the_api_mock.return_value = {"migrated": True}

        self.assertEqual(
            True,
            self.service_account.get_service_account_migration_status(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_migration_status_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"migrated": None}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.get_service_account_migration_status()

    @patch("grafana_api.api.Api.call_the_api")
    def test_hide_the_api_keys_tab(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "API keys hidden"}

        self.assertEqual(
            None,
            self.service_account.hide_the_api_keys_tab(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_hide_the_api_keys_tab_internal_error(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.hide_the_api_keys_tab()

    @patch("grafana_api.api.Api.call_the_api")
    def test_revert_service_account_token_api_key(self, call_the_api_mock):
        call_the_api_mock.return_value = {"message": "reverted service account to API key"}

        self.assertEqual(
            None,
            self.service_account.revert_service_account_token_to_api_key(1, 1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_revert_service_account_token_api_key_no_id(self, call_the_api_mock):
        call_the_api_mock.return_value = {"id": 2}

        with self.assertRaises(ValueError):
            self.service_account.revert_service_account_token_to_api_key(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_revert_service_account_token_api_key_no_valid_result(
        self, call_the_api_mock
    ):
        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):  # noqa: B017
            self.service_account.revert_service_account_token_to_api_key(1, 1)
