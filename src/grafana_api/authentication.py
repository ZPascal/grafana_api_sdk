import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Authentication:
    """The class includes all necessary methods to access the Grafana authentication API endpoints.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_api_tokens(
        self,
        org_id_header: int = None,
    ) -> list:
        """The method includes a functionality to get the corresponding api tokens of the organisation

        Args:
            org_id_header (int): Specify the org id as header to execute call for that specific organisation

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the result of the API token call
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.AUTHENTICATION.value,
            org_id_header=org_id_header,
        )

        if api_call != list() and api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def create_api_token(
        self,
        name: str,
        role: str,
        seconds_to_live: int = 0,
        org_id_header: int = None,
    ) -> dict:
        """The method includes a functionality to create a corresponding api tokens of the organisation specified by the name and role

        Args:
            name (str): Specify the token name
            role (str): Specify the access level/Grafana Role for the token. Can be one of the following values: Viewer, Editor or Admin
            seconds_to_live (int): Specify the seconds of the token expiration in seconds. If it is a positive number an expiration date for the key is set. If it is null, zero or is omitted completely (unless api_key_max_seconds_to_live configuration option is set) the key will never expire (default 0)
            org_id_header (int): Specify the org id as header to execute call for that specific organisation

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the API token object
        """

        if len(name) != 0 and len(role) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.AUTHENTICATION.value,
                RequestsMethods.POST,
                json.dumps(
                    dict(
                        {
                            "name": name,
                            "role": role,
                            "secondsToLive": seconds_to_live,
                        }
                    )
                ),
                org_id_header=org_id_header,
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no name or role defined.")
            raise ValueError

    def delete_api_token(
        self,
        token_id: int,
        org_id_header: int = None,
    ):
        """The method includes a functionality to delete a corresponding api token specified by the token id

        Args:
            token_id (int): Specify the token id
            org_id_header (int): Specify the org id as header to execute call for that specific organisation

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if token_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.AUTHENTICATION.value}/{token_id}",
                RequestsMethods.DELETE,
                org_id_header=org_id_header,
            )

            if api_call.get("message") != "API key deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the token.")
        else:
            logging.error("There is no token_id defined.")
            raise ValueError
