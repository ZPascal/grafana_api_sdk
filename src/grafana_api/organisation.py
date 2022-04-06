import json
import logging

from .model import APIModel, APIBasicModel, APIEndpoints, RequestsMethods
from .api import Api


class Organisation:
    """The class includes all necessary methods to access the Grafana organisation API endpoint

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_current_organization(self) -> dict:
        """The method includes a functionality to get the current organization.

        Required Permissions:
            Action: orgs:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current organization
        """

        api_call: dict = (
            Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/").json()
        )

        if api_call == dict() or api_call.get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_all_users_by_the_current_organization(self) -> list:
        """The method includes a functionality to get all users from the current organization.

        Required Permissions:
            Action: org.users:read
            Scope: users:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the users of the current organization
        """

        api_call: list = (
            Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/users").json()
        )

        if api_call == list() or api_call[0].get("orgId") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_all_users_by_the_current_organization_lookup(self) -> list:
        """The method includes a functionality to get the lookup information of all users from the current organization.

        Required Permissions:
            Action: org.users:read
            Scope: users:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the users of the current organization
        """

        api_call: list = (
            Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/users/lookup").json()
        )

        if api_call == list() or api_call[0].get("userId") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def update_organization_user_role_by_user_id(self, user_id: str, role: dict):
        """The method includes a functionality to update the current organization user by the user id.

        Args:
            user_id (str): Specify the id of the user
            role (dict): Specify the role of the user as dict

        Required Permissions:
            Action: org.users.role:update
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0 and role != dict():
            api_call: dict = (
                Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/users/{user_id}",
                                                         RequestsMethods.PATCH,
                                                         json.dumps(role)).json()
            )

            if api_call.get("message") is not "Organization user updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the organization user.")
        else:
            logging.error("There is no user_id or dict defined.")
            raise ValueError

    def delete_organization_user_by_user_id(self, user_id: str):
        """The method includes a functionality to delete the current organization user by the user id.

        Args:
            user_id (str): Specify the id of the user

        Required Permissions:
            Action: org.users:remove
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0:
            api_call: dict = (
                Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/users/{user_id}",
                                                         RequestsMethods.DELETE).json()
            )

            if api_call.get("message") is not "User removed from organization":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully removed the organization user.")
        else:
            logging.error("There is no user_id defined.")
            raise ValueError

    def update_current_organization(self, role_name: dict):
        """The method includes a functionality to update the current organization.

        Args:
            role_name (dict): Specify the role name as dict

        Required Permissions:
            Action: orgs:write
            Scope: N/A

        Raises
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if role_name != dict():
            api_call: dict = (
                Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}",
                                                         RequestsMethods.PUT).json()
            )

            if api_call.get("message") is not "Organization updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the organization.")
        else:
            logging.error("There is no role_name defined.")
            raise ValueError

    def add_new_user_to_current_organization(self, user_role: dict) -> int:
        """The method includes a functionality to add a new user to the current organization.

        Args:
            user_role (dict): Specify the user role attributes as dict

        Required Permissions:
            Action: org.users:add
            Scope: users:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            user_id (int): Returns the id of the created user
        """

        if user_role != dict():
            api_call: dict = (
                Api(self.grafana_api_model).call_the_api(f"{APIEndpoints.ORGANISATION.value}/users",
                                                         RequestsMethods.POST).json()
            )

            if api_call.get("message") is not "User added to organization":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call.get("userId")
        else:
            logging.error("There is no user_role defined.")
            raise ValueError


class OrganisationAdmin:
    """The class includes all necessary methods to access the Grafana organisation admin API endpoint

        Args:
            grafana_api_model (APIBasicModel): Inject a Grafana API basic model object that includes all necessary values and information

        Attributes:
            grafana_api_model (APIBasicModel): This is where we store the basic grafana_api_model
        """

    def __init__(self, grafana_api_model: APIBasicModel):
        self.grafana_api_model = grafana_api_model
