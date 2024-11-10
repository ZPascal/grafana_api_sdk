import os

from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.service_account import ServiceAccount


class ServiceAccountTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    service_account: ServiceAccount = ServiceAccount(grafana_api_model=model)

    def test_lifecycle_service_account(self):
        service_account: dict = self.service_account.create_service_account(
            "Test", "Admin"
        )

        self.assertEqual("Test", service_account.get("name"))

        self.assertEqual(
            service_account.get("role"),
            self.service_account.get_service_account_by_id(
                service_account.get("id")
            ).get("role"),
        )
        self.service_account.update_service_account(
            service_account.get("id"), "Test1", "Viewer"
        )
        self.assertEqual(
            "Viewer",
            self.service_account.get_service_account_by_id(
                service_account.get("id")
            ).get("role"),
        )

        self.assertEqual(
            2, len(self.service_account.search_service_account().get("serviceAccounts"))
        )

        service_account_token: dict = (
            self.service_account.create_service_account_token_by_id(
                service_account.get("id"), "Test-Token", "Admin"
            )
        )
        self.assertEqual("Test-Token", service_account_token.get("name"))
        self.assertEqual(
            "Test-Token",
            self.service_account.get_service_account_tokens_by_id(
                service_account.get("id")
            )[0].get("name"),
        )
        self.service_account.delete_service_account_token_by_id(
            service_account.get("id"), service_account_token.get("id")
        )
        self.assertEqual(
            list(),
            self.service_account.get_service_account_tokens_by_id(
                service_account.get("id")
            ),
        )
        self.service_account.migrate_api_keys_to_service_accounts()
        self.assertEqual(
            2, len(self.service_account.search_service_account().get("serviceAccounts"))
        )

        # TODO Add the APi token functionality

        self.service_account.delete_service_account(service_account.get("id"))
        self.assertEqual(
            1, len(self.service_account.search_service_account().get("serviceAccounts"))
        )
