from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel
from grafana_api.external_group import ExternalGroup


class ExternalGroupTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"orgId": "test"}])

        self.assertEqual(
            list([{"orgId": "test"}]),
            external_group.get_external_groups(1),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(ValueError):
            external_group.get_external_groups(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            external_group.get_external_groups(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Group added to Team"})

        self.assertEqual(
            None,
            external_group.add_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            external_group.add_external_group(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            external_group.add_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            )

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Team Group removed"})

        self.assertEqual(
            None,
            external_group.remove_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            ),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            external_group.remove_external_group(0, "")

    @patch("grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            external_group.remove_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            )
