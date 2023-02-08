import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class ExternalGroup:
    """The class includes all necessary methods to access the Grafana external group API endpoints.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_external_groups(
        self,
        team_id: int,
    ) -> list:
        """The method includes a functionality to get the corresponding external groups specified by the team id

        Args:
            team_id (int): Specify the team id

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        if team_id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.EXTERNAL_GROUPS.value}/{team_id}/groups",
            )

            if api_call == list() or api_call[0].get("orgId") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no team_id defined.")
            raise ValueError

    def add_external_group(
        self,
        team_id: int,
        group_id: str,
    ):
        """The method includes a functionality to add the corresponding external groups specified by the team id and group id

        Args:
            team_id (int): Specify the team id
            group_id (str): Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        if team_id != 0 and len(group_id) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.EXTERNAL_GROUPS.value}/{team_id}/groups",
                RequestsMethods.POST,
                json.dumps(dict({"groupId": group_id})),
            )

            if api_call.get("message") != "Group added to Team":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully added the group to the team.")
        else:
            logging.error("There is no team_id or group_id defined.")
            raise ValueError

    def remove_external_group(
        self,
        team_id: int,
        group_id: str,
    ):
        """The method includes a functionality to remove the corresponding external groups specified by the team id and group id

        Args:
            team_id (int): Specify the team id
            group_id (str): Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the external groups
        """
        if team_id != 0 and len(group_id) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.EXTERNAL_GROUPS.value}/{team_id}/groups/{group_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Team Group removed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully removed the group from the team.")
        else:
            logging.error("There is no team_id or group_id defined.")
            raise ValueError
