import json
from httpx import Response
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
)
from .api import Api


class Licensing:
    """The class includes all necessary methods to access the Grafana licensing API endpoints. Be aware that the functionality is a Grafana ENTERPRISE v7.4+ feature

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def check_license_availability(self):
        """The method includes a functionality to checks if a valid license is available

        Required Permissions:
            Action: licensing:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (bool): Returns the result if the license is available or not
        """

        api_call: Response = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.LICENSING.value}/check",
        )

        if api_call.status_code != 200:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return json.loads(str(api_call.text))

    def manually_force_license_refresh(self):
        """The method includes a functionality to manually ask license issuer for a new token

        Required Permissions:
            Action: licensing:update
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of license refresh call
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.LICENSING.value}/token/renew",
            RequestsMethods.POST,
            json.dumps({}),
        )

        if api_call == dict() or api_call.get("jti") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def remove_license_from_database(self):
        """The method includes a functionality to removes the license stored in the Grafana database

        Required Permissions:
            Action: licensing:delete
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of license refresh call
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.LICENSING.value}/token",
            RequestsMethods.DELETE,
            response_status_code=True,
        )

        if api_call.get("status") != 200:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info(
                "You successfully removed the corresponding license from the database."
            )
