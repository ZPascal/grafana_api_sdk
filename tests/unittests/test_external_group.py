from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.external_group import ExternalGroup


class ExternalGroupTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_external_groups(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list([{"orgId": "test"}]))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            list([{"orgId": "test"}]),
            external_group.get_external_groups(1),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            external_group.get_external_groups(0)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_external_groups_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=list())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            external_group.get_external_groups(1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Group added to Team"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            external_group.add_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            external_group.add_external_group(0, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_add_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            external_group.add_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_remove_external_group(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Team Group removed"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            None,
            external_group.remove_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_team_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            external_group.remove_external_group(0, "")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_remove_external_group_no_valid_result(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        external_group: ExternalGroup = ExternalGroup(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            external_group.remove_external_group(
                1, "cn=editors,ou=groups,dc=grafana,dc=org"
            )
