import logging
from typing import Union
import asyncio

from httpx import AsyncClient, Client, BasicAuth, Response

import json

from .model import APIModel, APIEndpoints
from .api import Api


class OtherHTTP:
    """The class includes all necessary methods to access other Grafana API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_frontend_settings(self) -> dict:
        """The method includes a functionality to get the frontend settings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding frontend settings
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.FRONTEND.value}/settings"
        )

        if api_call == dict():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def renew_login_session_based_on_remember_cookie(self):
        """The method includes a functionality to renew the login session based on the remember cookie

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """
        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.LOGIN.value}/ping"
        )

        if api_call.get("message") != "Logged in":
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully destroyed the dashboard snapshot.")

    def get_health_status(self) -> dict:
        """The method includes a functionality to get the health information

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the health information
        """

        http = Api(self.grafana_api_model).create_the_http_api_client()

        http_result = self._basic_get_call_without_token_auth(
            http, f"{self.grafana_api_model.host}/api/health"
        )

        api_call: dict = json.loads(http_result.text)

        if api_call == dict() or api_call.get("commit") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_metrics(
        self, basic_auth_username: str = None, basic_auth_password: str = None
    ) -> str:
        """The method includes a functionality to get the Grafana metrics information

        Args:
            basic_auth_username (str): Specify the optional basic auth username
            basic_auth_password (str): Specify the optional basic auth password

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the metrics information
        """

        http = Api(self.grafana_api_model).create_the_http_api_client()

        basic_auth = None
        if basic_auth_username is not None and basic_auth_password is not None:
            basic_auth = BasicAuth(basic_auth_username, basic_auth_password)

        api_call: str = self._basic_get_call_without_token_auth(
            http, f"{self.grafana_api_model.host}/metrics", basic_auth
        ).text

        if len(api_call) == 0 or api_call is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_plugin_metrics(
        self,
        plugin_id: str,
        basic_auth_username: str = None,
        basic_auth_password: str = None,
    ) -> str:
        """The method includes a functionality to get the Grafana plugin metrics information

        Args:
            plugin_id (str): Specify the plugin id
            basic_auth_username (str): Specify the optional basic auth username
            basic_auth_password (str): Specify the optional basic auth password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the metrics information
        """

        http = Api(self.grafana_api_model).create_the_http_api_client()

        basic_auth = None
        if basic_auth_username is not None and basic_auth_password is not None:
            basic_auth = BasicAuth(basic_auth_username, basic_auth_password)

        if len(plugin_id) != 0:
            url: str = f"{self.grafana_api_model.host}/metrics/plugins/{plugin_id}"
            api_call: str = self._basic_get_call_without_token_auth(
                http, url, basic_auth
            ).text

            if len(api_call) == 0 or api_call is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no plugin_id defined.")
            raise ValueError

    def _basic_get_call_without_token_auth(
        self, http: Union[Client, AsyncClient], url: str, basic_auth: BasicAuth = None
    ) -> Response:
        """The method includes a functionality to perform a basic GET call to an endpoint with optional BasicAuth

        Args:
            http (Union[Client, AsyncClient]): Specify the used client
            url (str): Specify the url of the performed api call
            basic_auth (BasicAuth): Specify the optional basic auth credentials (Default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (Response): Returns the corresponding result of the api call
        """

        try:
            if self.grafana_api_model.http2_support:

                async def _execute_async_http_requests():
                    async with http:
                        return await http.request("GET", url, auth=basic_auth)

                return asyncio.run(_execute_async_http_requests())
            else:
                return http.request("GET", url, auth=basic_auth)
        except Exception as e:
            raise e
