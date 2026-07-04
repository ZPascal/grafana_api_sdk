from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from grafana_api.model import (
    APIModel,
    GlobalUser,
)
from grafana_api.admin import Admin


class AdminTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_settings(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"DEFAULT": "test"}

        self.assertEqual(
            {"DEFAULT": "test"},
            admin.get_settings(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_settings_no_settings_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):
            admin.get_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_settings(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Settings updated"}

        self.assertEqual(
            None,
            admin.update_settings({"test": "test"}, {"test": "test"}),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_settings_update_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Settings updated"}

        self.assertEqual(
            None,
            admin.update_settings({"test": "test"}, None),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_settings_removals_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Settings updated"}

        self.assertEqual(
            None,
            admin.update_settings(None, {"test": "test"}),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_settings_no_update_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            admin.update_settings(None, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_settings_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.update_settings({"test": "test"})

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_stats(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"orgs": "test"}

        self.assertEqual(
            {"orgs": "test"},
            admin.get_stats(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_stats_no_stats_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):
            admin.get_stats()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_preview_report(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"version": "test"}

        self.assertEqual(
            {"version": "test"},
            admin.get_preview_report(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_preview_report_no_report_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(Exception):
            admin.get_preview_report()

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_global_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 10, "message": "User created"}

        user: GlobalUser = GlobalUser(
            name="test", email="test", login="test", password="test", org_id=1
        )

        self.assertEqual(
            10,
            admin.create_global_user(user),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_global_users_no_org_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"id": 10, "message": "User created"}

        user: GlobalUser = GlobalUser(
            name="test", email="test", login="test", password="test"
        )

        self.assertEqual(
            10,
            admin.create_global_user(user),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_global_users_no_user_object(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            admin.create_global_user(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_global_users_creation_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        user: GlobalUser = GlobalUser(
            name="test", email="test", login="test", password="test", org_id=1
        )

        with self.assertRaises(Exception):
            admin.create_global_user(user)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_password(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "User password updated"}

        self.assertEqual(
            None,
            admin.update_user_password(10, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_password_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            admin.update_user_password(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_password_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.update_user_password(10, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "User permissions updated"}

        self.assertEqual(
            None,
            admin.update_user_permissions(10, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_permissions_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            admin.update_user_permissions(0, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_permissions_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.update_user_permissions(10, True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_global_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "User deleted"}

        self.assertEqual(
            None,
            admin.delete_global_user(10),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_global_user_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {}

        with self.assertRaises(ValueError):
            admin.delete_global_user(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_global_user_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.delete_global_user(10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_pause_all_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"state": "Paused"}

        self.assertEqual(
            None,
            admin.pause_all_alerts(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_pause_all_alerts_pause_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"state": "Test"}

        with self.assertRaises(Exception):
            admin.pause_all_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_unpause_all_alerts(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"state": "Unpaused"}

        self.assertEqual(
            None,
            admin.unpause_all_alerts(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_unpause_all_alerts_unpause_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"state": "Test"}

        with self.assertRaises(Exception):
            admin.unpause_all_alerts()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_auth_token(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = [{"id": 1}]

        self.assertEqual(
            [{"id": 1}],
            admin.get_user_auth_token(10),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_auth_token_user_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(ValueError):
            admin.get_user_auth_token(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_auth_token_user_token_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(Exception):
            admin.get_user_auth_token(10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_user_auth_token(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "User auth token revoked"}

        self.assertEqual(
            None,
            admin.revoke_user_auth_token(10, 1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_user_auth_token_user_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(ValueError):
            admin.revoke_user_auth_token(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_user_auth_token_revoke_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.revoke_user_auth_token(10, 10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_logout_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "User auth token revoked"}

        self.assertEqual(
            None,
            admin.logout_user(10),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_logout_user_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = []

        with self.assertRaises(ValueError):
            admin.logout_user(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_logout_user_logout_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.logout_user(10)

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_dashboards_provisioning_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Dashboards config reloaded"}

        self.assertEqual(
            None,
            admin.reload_dashboards_provisioning_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_dashboards_provisioning_configuration_reload_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_dashboards_provisioning_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_datasources_provisioning_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Datasources config reloaded"}

        self.assertEqual(
            None,
            admin.reload_datasources_provisioning_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_datasources_provisioning_configuration_reload_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_datasources_provisioning_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_plugins_provisioning_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Plugins config reloaded"}

        self.assertEqual(
            None,
            admin.reload_plugins_provisioning_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_plugins_provisioning_configuration_reload_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_plugins_provisioning_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_notifications_provisioning_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Notifications config reloaded"}

        self.assertEqual(
            None,
            admin.reload_notifications_provisioning_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_notifications_provisioning_configuration_reload_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_notifications_provisioning_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_access_controls_provisioning_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Accesscontrol config reloaded"}

        self.assertEqual(
            None,
            admin.reload_access_controls_provisioning_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_access_controls_provisioning_configuration_reload_not_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_access_controls_provisioning_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_ldap_configuration(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "LDAP config reloaded"}

        self.assertEqual(
            None,
            admin.reload_ldap_configuration(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reload_ldap_configuration_reload_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        call_the_api_mock.return_value = {"message": "Test"}

        with self.assertRaises(Exception):
            admin.reload_ldap_configuration()

    @patch("grafana_api.api.Api.call_the_api")
    def test_rotate_data_encryption_keys(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        mock: Mock = Mock()
        mock.status_code = 204

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            admin.rotate_data_encryption_keys(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_rotate_data_encryption_keys_rotate_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        admin: Admin = Admin(grafana_api_model=model)

        mock: Mock = Mock()
        mock.status_code = 400

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            admin.rotate_data_encryption_keys()
