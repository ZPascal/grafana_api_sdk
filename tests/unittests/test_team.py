from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel, TeamObject
from src.grafana_api.team import Team


class TeamTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"totalCount": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"totalCount": 1}), team.search_team())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_team_query(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"totalCount": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"totalCount": 1}),
            team.search_team(query="Test"),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_search_team_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.search_team()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"id": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"id": 1}), team.get_team_by_id(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.get_team_by_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_by_id_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.get_team_by_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)
        team_object: TeamObject = TeamObject(name="test", email="test", org_id=1)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Team created", "teamId": 1}))

        call_the_api_mock.return_value = mock

        self.assertEqual(1, team.add_team(team_object))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team_no_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.add_team(None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team_add_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)
        team_object: TeamObject = TeamObject(name="test", email="test", org_id=1)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.add_team(team_object)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Team updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, team.update_team(1, "test", "test"))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.update_team(0, None, None)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.update_team(1, "test", "test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Team deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, team.delete_team_by_id(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.delete_team_by_id(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_by_id_delete_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.delete_team_by_id(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_members(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"userId": 1}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(list([{"userId": 1}]), team.get_team_members(1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_members_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.get_team_members(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_members_no_team_members(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.get_team_members(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team_member(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Member added to Team"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, team.add_team_member(1, 1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team_member_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.add_team_member(0, 0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_team_member_add_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.add_team_member(1, 1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_member(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Team Member removed"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, team.delete_team_member(1, 1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_member_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.delete_team_member(0, 0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_team_member_deletion_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.delete_team_member(1, 1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(
            return_value=dict(
                {"theme": "light", "homeDashboardId": "Test", "timezone": "utc"}
            )
        )

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"theme": "light", "homeDashboardId": "Test", "timezone": "utc"}),
            team.get_team_preferences(1),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_preferences_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.get_team_preferences(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_team_preferences_no_preferences_available(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.get_team_preferences(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team_preferences(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Preferences updated"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, team.update_team_preferences(1, 1))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_no_id(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            team.update_team_preferences(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_team_preferences_update_not_possible(self, call_the_api_mock):
        model: APIModel = APIModel(
            host=MagicMock(), username=MagicMock(), password=MagicMock()
        )
        team: Team = Team(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Test"}))

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            team.update_team_preferences(1)
