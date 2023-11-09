from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, TeamObject
from grafana_api.team import Team


class TeamTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_search_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"totalCount": 1})

        self.assertEqual(dict({"totalCount": 1}), team.search_team())

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_team_query(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"totalCount": 1})

        self.assertEqual(
            dict({"totalCount": 1}),
            team.search_team(query="Test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_search_team_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            team.search_team()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(dict({"id": 1}), team.get_team_by_id(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.get_team_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_by_id_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            team.get_team_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)
        team_object: TeamObject = TeamObject(name="test", email="test", org_id=1)

        call_the_api_mock.return_value = dict({"message": "Team created", "teamId": 1})

        self.assertEqual(1, team.add_team(team_object))

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.add_team(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_add_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)
        team_object: TeamObject = TeamObject(name="test", email="test", org_id=1)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.add_team(team_object)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Team updated"})

        self.assertEqual(None, team.update_team(1, "test", "test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.update_team(0, None, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.update_team(1, "test", "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Team deleted"})

        self.assertEqual(None, team.delete_team_by_id(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.delete_team_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.delete_team_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_members(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"userId": 1}])

        self.assertEqual(list([{"userId": 1}]), team.get_team_members(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_members_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            team.get_team_members(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_members_no_team_members(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            team.get_team_members(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_member(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Member added to Team"})

        self.assertEqual(None, team.add_team_member(1, 1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_member_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.add_team_member(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_team_member_add_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.add_team_member(1, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_member(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Team Member removed"})

        self.assertEqual(None, team.delete_team_member(1, 1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_member_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.delete_team_member(0, 0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_team_member_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.delete_team_member(1, 1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"theme": "light", "homeDashboardId": "Test", "timezone": "utc"}
        )

        self.assertEqual(
            dict({"theme": "light", "homeDashboardId": "Test", "timezone": "utc"}),
            team.get_team_preferences(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_preferences_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.get_team_preferences(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_team_preferences_no_preferences_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            team.get_team_preferences(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Preferences updated"})

        self.assertEqual(None, team.update_team_preferences(1, home_dashboard_id=1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_home_dashboard_uid(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Preferences updated"})

        self.assertEqual(
            None,
            team.update_team_preferences(1, home_dashboard_uid="test", timezone="test"),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_only_theme_update(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Preferences updated"})

        self.assertEqual(
            None,
            team.update_team_preferences(
                1, home_dashboard_uid="test", home_dashboard_id=0, theme="test"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            team.update_team_preferences(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test"})

        with self.assertRaises(Exception):
            team.update_team_preferences(1, home_dashboard_uid="test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = list(["test"])

        self.assertEqual(list(["test"]), team.get_external_groups(1))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        with self.assertRaises(ValueError):
            team.get_external_groups(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            team.get_external_groups(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Group added to Team"}
        )

        self.assertEqual(None, team.add_external_group(1, "test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        with self.assertRaises(ValueError):
            team.add_external_group(0, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 401})

        with self.assertRaises(Exception):
            team.add_external_group(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group_error(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 500})

        self.assertEqual(None, team.add_external_group(1, "test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Team Group removed"}
        )

        self.assertEqual(None, team.remove_external_group(1, "test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        with self.assertRaises(ValueError):
            team.remove_external_group(0, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 401})

        with self.assertRaises(Exception):
            team.remove_external_group(1, "test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group_error(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 500})

        self.assertEqual(None, team.remove_external_group(1, "test"))
