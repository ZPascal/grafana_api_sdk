from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.organisation import Organisation, OrganisationAdmin


class OrganisationTestCase(TestCase):
    model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
    organisation: Organisation = Organisation(grafana_api_model=model)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 1}), self.organisation.get_current_organization()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_current_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_current_organization()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_users_by_the_current_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([dict({"orgId": 1})]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([dict({"orgId": 1})]), self.organisation.get_all_users_by_the_current_organization()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_users_by_the_current_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_all_users_by_the_current_organization()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_users_by_the_current_organization_lookup(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([dict({"userId": 1})]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([dict({"userId": 1})]), self.organisation.get_all_users_by_the_current_organization_lookup()
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_users_by_the_current_organization_lookup_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_all_users_by_the_current_organization_lookup()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user_role_by_user_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization user updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.update_organization_user_role_by_user_id(1, "Viewer")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user_role_by_user_id_no_user_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.update_organization_user_role_by_user_id(0, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user_role_by_user_id_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.update_organization_user_role_by_user_id(1, "Viewer")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user_by_user_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "User removed from organization"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.delete_organization_user_by_user_id(1)
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user_by_user_id_no_user_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.delete_organization_user_by_user_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user_by_user_id_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.delete_organization_user_by_user_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.update_current_organization("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_organization_no_role_name(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.update_current_organization("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_current_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.update_current_organization("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_new_user_to_current_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "User added to organization", "userId": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            1, self.organisation.add_new_user_to_current_organization("test", "test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_new_user_to_current_organization_no_role(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.add_new_user_to_current_organization("", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_new_user_to_current_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.add_new_user_to_current_organization("test", "test")


class OrganisationAdminTestCase(TestCase):
    model: APIModel = APIModel(host=MagicMock(), username=MagicMock(), password=MagicMock())
    organisation: OrganisationAdmin = OrganisationAdmin(grafana_api_model=model)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 10}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 10}), self.organisation.get_organization_by_id(1)
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_id_no_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.get_organization_by_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_id_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_organization_by_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_name(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 10}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"id": 10}), self.organisation.get_organization_by_name("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_name_no_name(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.get_organization_by_name("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_by_name_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_organization_by_name("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organizations(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"id": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"id": 1}]), self.organisation.get_organizations())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organizations_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_organizations()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization created", "orgId": 10}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            10, self.organisation.create_organization("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_organization_no_name(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.create_organization("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.create_organization("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.update_organization(1, "test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.update_organization(0, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.update_organization(1, "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.delete_organization(1)
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.delete_organization(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.delete_organization(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_users(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list([dict({"orgId": 1, "userId": 10})]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([dict({"orgId": 1, "userId": 10})]), self.organisation.get_organization_users(1)
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_users_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.get_organization_users(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_organization_users_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.get_organization_users(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_organization_user(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "User added to organization", "userId": 10}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            10, self.organisation.add_organization_user(1, "test", "test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_organization_user_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.add_organization_user(0, "", "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_organization_user_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.add_organization_user(1, "test", "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Organization user updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.update_organization_user(1, 10, "test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.update_organization_user(0, 0, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_organization_user_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.update_organization_user(1, 10, "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "User removed from organization"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None, self.organisation.delete_organization_user(1, 10)
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user_no_org_id(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            self.organisation.delete_organization_user(0, 0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_organization_user_error_response(self, call_the_api_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            self.organisation.delete_organization_user(1, 10)