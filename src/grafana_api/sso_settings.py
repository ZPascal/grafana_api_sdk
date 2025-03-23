import json
import logging
from typing import Union

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    SSOSetting,
)
from .api import Api


class SSOSettings:
    """The class includes all necessary methods to access the Grafana sso settings API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_sso_settings(self) -> list:
        """The method includes a functionality to get the SSO settings for all providers

        Required Permissions:
            Action: settings:read
            Scope: settings:auth.{provider}:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the all SSO settings
        """

        api_call: Union[list, dict] = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SSO_SETTINGS.value}",
            response_status_code=True,
        )

        status_code: int = (
            api_call[0].get("status")
            if isinstance(api_call, list)
            else api_call.get("status")
        )

        sso_settings_status_dict: dict = dict(
            {
                400: "Bad request.",
                401: "Unauthorized.",
                403: "Access Denied.",
            }
        )

        if status_code == 200:
            return api_call
        elif 400 <= status_code <= 403:
            logging.error(sso_settings_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def get_sso_settings_by_provider(self, provider: str) -> dict:
        """The method includes a functionality to get the SSO settings for the specified provider

        Args:
            provider (str): Specify the provider

        Required Permissions:
            Action: settings:read
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding provider SSO settings
        """

        if len(provider) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SSO_SETTINGS.value}/{provider}",
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            sso_settings_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                    404: "SSO Settings not found.",
                }
            )

            if status_code == 200:
                return api_call
            elif 400 <= status_code <= 404:
                logging.error(sso_settings_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no provider defined.")
            raise ValueError

    def update_sso_settings(self, provider: str, sso_setting: SSOSetting):
        """The method includes a functionality to update the SSO settings specified by the provider

         Args:
            provider (str): Specify the provider
            sso_setting (SSOSetting): Specify the SSO setting

        Required Permissions:
            Action: settings:write
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            len(provider) != 0
            and sso_setting is not None
            and len(sso_setting.api_url) != 0
            and len(sso_setting.client_id) != 0
            and len(sso_setting.client_secret) != 0
            and sso_setting.enabled is not None
            and len(sso_setting.scopes) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SSO_SETTINGS.value}/{provider}",
                RequestsMethods.PUT,
                json.dumps(
                    dict(
                        {
                            "settings": {
                                "apiUrl": sso_setting.api_url,
                                "clientId": sso_setting.client_id,
                                "clientSecret": sso_setting.client_secret,
                                "enabled": sso_setting.enabled,
                                "scopes": sso_setting.scopes,
                            }
                        }
                    )
                ),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            sso_settings_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                }
            )

            if status_code == 204:
                logging.info(
                    "You successfully updated the corresponding provider SSO setting."
                )
            elif 400 <= status_code <= 403:
                logging.error(sso_settings_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no provider or sso_settings object defined.")
            raise ValueError

    def delete_sso_settings(self, provider: str):
        """The method includes a functionality to delete the SSO settings specified by the provider

         Args:
            provider (str): Specify the provider

        Required Permissions:
            Action: settings:write
            Scope: settings:auth.{provider}:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(provider) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SSO_SETTINGS.value}/{provider}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            sso_settings_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                    404: "SSO Settings not found.",
                }
            )

            if status_code == 204:
                logging.info(
                    "You successfully deleted the corresponding provider SSO settings."
                )
            elif 400 <= status_code <= 404:
                logging.error(sso_settings_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no provider defined.")
            raise ValueError
