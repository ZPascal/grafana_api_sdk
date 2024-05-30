from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, SSOSetting
from grafana_api.sso_settings import SSOSettings


class SSOSettingsTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = list([
            {
                "id": "1",
                "provider": "github",
                "settings": {
                    "apiUrl": "https://api.github.com/user",
                    "clientId": "my_github_client",
                    "clientSecret": "*********",
                    "enabled": True,
                    "scopes": "user:email,read:org"
                },
                "source": "system",
                "status": 200,
            }
        ])

        self.assertEqual(
            list([
                {
                    "id": "1",
                    "provider": "github",
                    "settings": {
                        "apiUrl": "https://api.github.com/user",
                        "clientId": "my_github_client",
                        "clientSecret": "*********",
                        "enabled": True,
                        "scopes": "user:email,read:org"
                    },
                    "source": "system",
                    "status": 200,
                }
            ]),
            sso_settings.get_sso_settings(),
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings_bad_request(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = list([
            {
                "status": 400,
            }
        ])

        with self.assertRaises(Exception):
            sso_settings.get_sso_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = list([
            {
                "status": 500,
            }
        ])

        with self.assertRaises(Exception):
            sso_settings.get_sso_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings_by_provider(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
                "id": "1",
                "provider": "github",
                "settings": {
                    "apiUrl": "https://api.github.com/user",
                    "clientId": "my_github_client",
                    "clientSecret": "*********",
                    "enabled": True,
                    "scopes": "user:email,read:org"
                },
                "source": "system",
                "status": 200,
            })

        self.assertEqual(
                dict({
                    "id": "1",
                    "provider": "github",
                    "settings": {
                        "apiUrl": "https://api.github.com/user",
                        "clientId": "my_github_client",
                        "clientSecret": "*********",
                        "enabled": True,
                        "scopes": "user:email,read:org"
                    },
                    "source": "system",
                    "status": 200,
                }),
            sso_settings.get_sso_settings_by_provider("github"),
        )

    def test_get_sso_settings_by_provider_no_provider(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        with self.assertRaises(ValueError):
            sso_settings.get_sso_settings_by_provider("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings_by_provider_bad_request(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
                "status": 400,
            }
        )

        with self.assertRaises(Exception):
            sso_settings.get_sso_settings_by_provider("github")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_sso_settings_by_provider_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {
                "status": 500,
            }
        )

        with self.assertRaises(Exception):
            sso_settings.get_sso_settings_by_provider("github")

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_sso_settings(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
            "status": 204,
        })

        sso_setting: SSOSetting = SSOSetting("https://api.github.com/user",
                                             "client_id",
                                             "client_secret",
                                             True,
                                             "user:email,read:org")
        self.assertEqual(
            None,
            sso_settings.update_sso_settings("github", sso_setting),
        )

    def test_update_sso_settings_no_provider(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        with self.assertRaises(ValueError):
            sso_settings.update_sso_settings("", None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_sso_settings_bad_request(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
            "status": 400,
        }
        )

        sso_setting: SSOSetting = SSOSetting("https://api.github.com/user",
                                             "client_id",
                                             "client_secret",
                                             True,
                                             "user:email,read:org")
        with self.assertRaises(Exception):
            sso_settings.update_sso_settings("github", sso_setting)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_sso_settings_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {
                "status": 500,
            }
        )

        sso_setting: SSOSetting = SSOSetting("https://api.github.com/user",
                                             "client_id",
                                             "client_secret",
                                             True,
                                             "user:email,read:org")
        with self.assertRaises(Exception):
            sso_settings.update_sso_settings("github", sso_setting)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_sso_settings(
            self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
            "status": 204,
        })

        self.assertEqual(
            None,
            sso_settings.delete_sso_settings("github"),
        )

    def test_delete_sso_settings_no_provider(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        with self.assertRaises(ValueError):
            sso_settings.delete_sso_settings("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_sso_settings_bad_request(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict({
            "status": 400,
        }
        )

        with self.assertRaises(Exception):
            sso_settings.delete_sso_settings("github")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_sso_settings_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        sso_settings: SSOSettings = SSOSettings(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {
                "status": 500,
            }
        )

        with self.assertRaises(Exception):
            sso_settings.delete_sso_settings("github")
