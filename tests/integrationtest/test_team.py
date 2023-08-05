import os

from unittest import TestCase

from grafana_api.model import APIModel, TeamObject
from grafana_api.team import Team
from grafana_api.organisation import Organisation


class TeamTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    team: Team = Team(model)

    def test_search_team(self):
        self.assertEqual(
            4, self.team.search_team(query="Test").get("teams")[0].get("id")
        )

    def test_get_team_by_id(self):
        self.assertEqual(4, self.team.get_team_by_id(4).get("id"))

    def test_a_add_team(self):
        team_object: TeamObject = TeamObject(
            name="Test1",
            email="test@test.de",
            org_id=Organisation(self.model).get_current_organization().get("id"),
        )
        self.assertIsNotNone(self.team.add_team(team_object))

        self.assertIsNotNone(
            self.team.search_team(query="Test1").get("teams")[0].get("id")
        )

    def test_b_update_team(self):
        self.assertIsNone(
            self.team.update_team(
                self.team.search_team(query="Test1").get("teams")[0].get("id"),
                "Test2",
                "test2@test.de",
            )
        )

        self.assertIsNotNone(
            self.team.search_team(query="Test2").get("teams")[0].get("id")
        )

    def test_c_delete_team_by_id(self):
        self.assertIsNone(
            self.team.delete_team_by_id(
                self.team.search_team(query="Test2").get("teams")[0].get("id")
            )
        )

        with self.assertRaises(Exception):
            self.assertIsNotNone(
                self.team.search_team(query="Test2").get("teams")[0].get("id")
            )

    def test_get_team_members(self):
        self.assertEqual(1, len(self.team.get_team_members(4)))

    def test_d_add_team_member(self):
        team_id: int = self.__team_creation_util()

        self.assertEqual(1, len(self.team.get_team_members(team_id)))

        self.team.delete_team_by_id(team_id)

    def test_e_delete_team_member(self):
        team_id: int = self.__team_creation_util()

        self.team.delete_team_member(team_id, 8)

        with self.assertRaises(Exception):
            self.team.get_team_members(team_id)

        self.team.delete_team_by_id(team_id)

    def test_get_team_preferences(self):
        self.assertEqual(
            "tests", self.team.get_team_preferences(4).get("homeDashboardUID")
        )

    def test_update_team_preferences(self):
        self.assertIsNone(
            self.team.update_team_preferences(
                4, timezone="utc", home_dashboard_uid="tests"
            )
        )

        self.assertEqual("utc", self.team.get_team_preferences(4).get("timezone"))

    def __team_creation_util(self) -> int:
        self.test_a_add_team()
        team_id: int = self.team.search_team(query="Test1").get("teams")[0].get("id")

        self.team.add_team_member(team_id, 8)

        return team_id
