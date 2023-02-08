from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel, UserObject
from grafana_api.user import User, CurrentUser


class UserTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_search_users(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), user.search_users())

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_users_query(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(
            list([{"id": 1}]),
            user.search_users(query="Test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_users_no_users(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            user.search_users()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), user.get_user_by_id(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            user.get_user_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_id_no_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            user.get_user_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_username_or_email(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), user.get_user_by_username_or_email("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_username_or_email_no_username_or_email(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            user.get_user_by_username_or_email("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_by_username_or_email_no_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            user.get_user_by_username_or_email("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)
        user_object: UserObject = UserObject(
            email="test", name="test", login="test", theme="test"
        )

        call_the_api_mock.return_value = dict({"message": "User updated"})

        self.assertEqual(None, user.update_user(1, user_object))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            user.update_user("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_user_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)
        user_object: UserObject = UserObject(
            email="test", name="test", login="test", theme="test"
        )

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            user.update_user(1, user_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_organizations(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"orgId": 1}])

        self.assertEqual(list([{"orgId": 1}]), user.get_user_organizations(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_organizations_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            user.get_user_organizations(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_organizations_no_orgs(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            user.get_user_organizations(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_teams(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), user.get_user_teams(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_teams_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            user.get_user_teams(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_teams_no_teams(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            user.get_user_teams(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_specific_user_context(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Active organization changed"})

        self.assertEqual(None, user.switch_specific_user_context(1, 1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_specific_user_context_no_userid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            user.switch_specific_user_context(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_specific_user_context_switch_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        user: User = User(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            user.switch_specific_user_context(1, 1)


class CurrentUserTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), current_user.get_user())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_no_user(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            current_user.get_user()

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_password(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "User password changed"})

        self.assertEqual(None, current_user.update_password("test", "test", "test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_password_no_old_password(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            current_user.update_password("", "", "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_password_password_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            current_user.update_password("test", "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_current_user_context(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Active organization changed"})

        self.assertEqual(None, current_user.switch_current_user_context(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_current_user_context_no_org_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            current_user.switch_current_user_context(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_switch_current_user_context_switch_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            current_user.switch_current_user_context(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_organizations(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"orgId": 1}])

        self.assertEqual(list([{"orgId": 1}]), current_user.get_user_organizations())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_organizations_no_orgs(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            current_user.get_user_organizations()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_teams(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), current_user.get_user_teams())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_user_teams_no_teams(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            current_user.get_user_teams()

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_a_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Dashboard starred!"})

        self.assertEqual(None, current_user.star_a_dashboard(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_a_dashboard_no_dashboard_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            current_user.star_a_dashboard(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_star_a_dashboard_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            current_user.star_a_dashboard(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_a_dashboard(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Dashboard unstarred"})

        self.assertEqual(None, current_user.unstar_a_dashboard(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_a_dashboard_no_dashboard_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            current_user.unstar_a_dashboard(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_unstar_a_dashboard_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            current_user.unstar_a_dashboard(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_auth_tokens(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), current_user.get_auth_tokens())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_auth_tokens_no_tokens(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            current_user.get_auth_tokens()

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_auth_token(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "User auth token revoked"})

        self.assertEqual(None, current_user.revoke_auth_token(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_auth_token_no_auth_token_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            current_user.revoke_auth_token(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_revoke_auth_token_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        current_user: CurrentUser = CurrentUser(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            current_user.revoke_auth_token(1)
