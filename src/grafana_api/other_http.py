import logging

import requests

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

        api_call: dict = (
            Api(self.grafana_api_model)
            .call_the_api(f"{APIEndpoints.FRONTEND.value}/settings")
            .json()
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

        api_call: dict = (
            Api(self.grafana_api_model)
            .call_the_api(f"{APIEndpoints.LOGIN.value}/ping")
            .json()
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

        api_call: dict = requests.get(f"{self.grafana_api_model.host}/api/health").json()

        if api_call == dict() or api_call.get("commit") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_metrics(self) -> str:
        """The method includes a functionality to get the Grafana metrics information

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the metrics information
        """

        api_call: str = requests.get(f"{self.grafana_api_model.host}/metrics").text

        if len(api_call) == 0 or api_call is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call
