from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, CustomRole, RolePermission
from grafana_api.rbac import RBAC


class RBACTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_status(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "enabled": True})

        self.assertEqual(
            True,
            rbac.get_status(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_status_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.get_status()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_status_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.get_status()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_roles(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 200, "test": "test"}])

        self.assertEqual(
            list([{"status": 200, "test": "test"}]),
            rbac.get_all_roles(include_hidden_roles=True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_roles_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_all_roles()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_roles_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_all_roles()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_role(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.get_role(uid="test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_role_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.get_role(uid="")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_role_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.get_role(uid="test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_role_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.get_role(uid="test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.create_role(custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_basic_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.create_role(custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_basic_permission_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test", permissions=list([RolePermission(action="test")])
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.create_role(custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_non_valid_permission_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test", permissions=list([RolePermission(action=None)])
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        with self.assertRaises(ValueError):
            rbac.create_role(custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_no_role_definition(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.create_role(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.create_role(custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_role_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.create_role(custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.update_role("test", custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_basic_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.update_role("test", custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_basic_permission_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test", permissions=list([RolePermission(action="test")])
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            rbac.update_role("test", custom_role),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_non_valid_permission_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test", permissions=list([RolePermission(action=None)])
        )

        call_the_api_mock.return_value = dict({"status": 200, "test": "test"})

        with self.assertRaises(ValueError):
            rbac.update_role("test", custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_no_role_definition(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.update_role(None, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.update_role("test", custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_role_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)
        custom_role: CustomRole = CustomRole(
            name="Test",
            uid="test",
            version=1,
            description="test",
            display_name="test",
            group="test",
            permissions=list([RolePermission(action="test", scope="test")]),
        )

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.update_role("test", custom_role)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_role(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role deleted"}
        )

        self.assertEqual(
            None,
            rbac.delete_role("test", True, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_role_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "test"})

        with self.assertRaises(Exception):
            rbac.delete_role("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_role_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.delete_role("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_role_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.delete_role("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_role_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.delete_role("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_roles(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list(
            [{"status": 200, "test": "test"}, {"test"}]
        )

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test"}]),
            rbac.get_user_assigned_roles(1, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_roles_no_user_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(ValueError):
            rbac.get_user_assigned_roles(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_roles_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_user_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_roles_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_user_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list(
            [{"status": 200, "test": "test"}, {"test"}]
        )

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test"}]),
            rbac.get_user_assigned_permissions(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_permissions_no_user_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(ValueError):
            rbac.get_user_assigned_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_permissions_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_user_assigned_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_assigned_permissions_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_user_assigned_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_user_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role added to the user."}
        )

        self.assertEqual(
            None,
            rbac.add_user_role_assignment(1, "test", True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_user_role_assignment_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.add_user_role_assignment(1, "test", True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_user_role_assignment_no_user_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.add_user_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_user_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.add_user_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_user_role_assignment_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.add_user_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_user_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role removed from user."}
        )

        self.assertEqual(
            None,
            rbac.remove_user_role_assignment(1, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_user_role_assignment_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.remove_user_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_user_role_assignment_no_user_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.remove_user_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_user_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.remove_user_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_user_role_assignment_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.remove_user_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_role_assignments(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "User roles have been updated."}
        )

        self.assertEqual(
            None,
            rbac.update_user_role_assignments(1, list(["test", "test"]), True, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_role_assignments_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.update_user_role_assignments(1, list(["test", "test"]))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_role_assignments_no_user_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.update_user_role_assignments(0, list())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_role_assignments_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.update_user_role_assignments(1, list(["test", "test"]))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_role_assignments_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.update_user_role_assignments(1, list(["test", "test"]))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_roles(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list(
            [{"status": 200, "test": "test"}, {"test"}]
        )

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test"}]),
            rbac.get_service_account_assigned_roles(1, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_roles_no_service_account_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(ValueError):
            rbac.get_service_account_assigned_roles(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_roles_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_service_account_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_roles_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_service_account_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_permissions(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list(
            [{"status": 200, "test": "test"}, {"test"}]
        )

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test"}]),
            rbac.get_service_account_assigned_permissions(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_permissions_no_service_account_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(ValueError):
            rbac.get_service_account_assigned_permissions(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_permissions_no_result(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_service_account_assigned_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_service_account_assigned_permissions_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_service_account_assigned_permissions(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_service_account_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role added to the user."}
        )

        self.assertEqual(
            None,
            rbac.add_service_account_role_assignment(1, "test", True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_service_account_role_assignment_wrong_error_message(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.add_service_account_role_assignment(1, "test", True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_service_account_role_assignment_no_service_account_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.add_service_account_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_service_account_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.add_service_account_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_service_account_role_assignment_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.add_service_account_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_service_account_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role removed from user."}
        )

        self.assertEqual(
            None,
            rbac.remove_service_account_role_assignment(1, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_service_account_role_assignment_wrong_error_message(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.remove_service_account_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_service_account_role_assignment_no_service_account_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.remove_service_account_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_service_account_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.remove_service_account_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_service_account_role_assignment_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.remove_service_account_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_role_assignments(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "User roles have been updated."}
        )

        self.assertEqual(
            None,
            rbac.update_service_account_role_assignments(
                1, ["test", "test"], True, True
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_role_assignments_wrong_error_message(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.update_service_account_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_role_assignments_no_service_account_id(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.update_service_account_role_assignments(0, [])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_role_assignments_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.update_service_account_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_service_account_role_assignments_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.update_service_account_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_assigned_roles(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list(
            [{"status": 200, "test": "test"}, {"test"}]
        )

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test"}]),
            rbac.get_team_assigned_roles(1, True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_assigned_roles_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(ValueError):
            rbac.get_team_assigned_roles(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_assigned_roles_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 404}])

        with self.assertRaises(Exception):
            rbac.get_team_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_assigned_roles_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 501}])

        with self.assertRaises(Exception):
            rbac.get_team_assigned_roles(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role added to the team."}
        )

        self.assertEqual(
            None,
            rbac.add_team_role_assignment(1, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_role_assignment_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.add_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_role_assignment_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.add_team_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.add_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_role_assignment_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.add_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_team_role_assignment(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Role removed from team."}
        )

        self.assertEqual(
            None,
            rbac.remove_team_role_assignment(1, "test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_team_role_assignment_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.remove_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_team_role_assignment_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.remove_team_role_assignment(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_team_role_assignment_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.remove_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_team_role_assignment_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.remove_team_role_assignment(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_role_assignments(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Team roles have been updated."}
        )

        self.assertEqual(
            None,
            rbac.update_team_role_assignments(1, "test", True),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_role_assignments_wrong_error_message(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.update_team_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_role_assignments_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(ValueError):
            rbac.update_team_role_assignments(0, [])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_role_assignments_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.update_team_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_role_assignments_no_result_advanced(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.update_team_role_assignments(1, ["test", "test"])

    @patch("grafana_api.api.Api.call_the_api")
    def test_reset_basic_roles_to_their_default(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Reset performed"}
        )

        self.assertEqual(
            None,
            rbac.reset_basic_roles_to_their_default(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_reset_basic_roles_to_their_default_wrong_error_message(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "message": "Test"})

        with self.assertRaises(Exception):
            rbac.reset_basic_roles_to_their_default()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reset_basic_roles_to_their_default_no_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            rbac.reset_basic_roles_to_their_default()

    @patch("grafana_api.api.Api.call_the_api")
    def test_reset_basic_roles_to_their_default_no_result_advanced(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        rbac: RBAC = RBAC(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 501})

        with self.assertRaises(Exception):
            rbac.reset_basic_roles_to_their_default()
