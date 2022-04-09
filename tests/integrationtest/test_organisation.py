import os
from unittest import TestCase

from src.grafana_api.model import (
    APIModel,
)
from src.grafana_api.organisation import Organisation


class OrganisationTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    organisation: Organisation = Organisation(model)

    def test_get_current_organization(self):
        organisation: dict = self.organisation.get_current_organization()

        self.assertEqual(4, organisation.get("id"))

    def test_get_all_users_by_the_current_organization(self):
        organisation_users: list = (
            self.organisation.get_all_users_by_the_current_organization()
        )

        self.assertEqual(4, organisation_users[0].get("userId"))

    def test_get_all_users_by_the_current_organization_lookup(self):
        organisation_users: list = (
            self.organisation.get_all_users_by_the_current_organization_lookup()
        )

        self.assertEqual(4, organisation_users[0].get("userId"))

    def test_a_update_current_organization(self):
        self.organisation.update_current_organization("Test")
        self.assertEqual(
            "Test", self.organisation.get_current_organization().get("name")
        )

    def test_b_update_current_organization(self):
        self.organisation.update_current_organization("Github")
        self.assertEqual(
            "Github", self.organisation.get_current_organization().get("name")
        )

    def test_a_add_new_user_to_current_organization(self):
        self.organisation.add_new_user_to_current_organization(
            "info@theiotstudio.com", "Viewer"
        )

        organisation_users: list = (
            self.organisation.get_all_users_by_the_current_organization_lookup()
        )
        self.assertEqual("Test", organisation_users[0].get("login"))

    def test_b_update_organization_user_role_by_user_id(self):
        self.organisation.update_organization_user_role_by_user_id(7, "Editor")

        organisation_users: list = (
            self.organisation.get_all_users_by_the_current_organization()
        )
        self.assertEqual(7, organisation_users[0].get("userId"))
        self.assertEqual("Editor", organisation_users[0].get("role"))

    def test_c_delete_organization_user_by_user_id(self):
        self.organisation.delete_organization_user_by_user_id(7)

        organisation_users: list = (
            self.organisation.get_all_users_by_the_current_organization()
        )
        self.assertEqual(2, len(organisation_users))
