import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    UserObject,
)
from .api import Api


class User:
    """The class includes all necessary methods to access the Grafana user API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_users(
        self,
        results_per_page: int = 1000,
        pages: int = 1,
        query: str = None,
    ) -> list:
        """The method includes a functionality to get all Grafana system users specified by the optional query and paging functionality

        Required Permissions:
            Action: users:read
            Scope: global.users:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            pages (int): Specify the pages as integer (default 1)
            query (str): Specify the query (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Grafana users
        """

        api_request_url: str = (
            f"{APIEndpoints.USERS.value}/search?perpage={results_per_page}&page={pages}"
        )

        if query is not None and len(query) != 0:
            api_request_url: str = f"{api_request_url}&query={query}"

        api_call: list = Api(self.grafana_api_model).call_the_api(
            api_request_url,
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_user_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a specific user by the id

        Required Permissions:
            Action: users:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/{id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def get_user_by_username_or_email(self, username_or_email: str) -> dict:
        """The method includes a functionality to get a specific user by the username_or_email

        Required Permissions:
            Action: users:read
            Scope: global.users:*

        Args:
            username_or_email (str): Specify the username_or_email of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """

        if len(username_or_email) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/lookup?loginOrEmail={username_or_email}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no username_or_email defined.")
            raise ValueError

    def update_user(self, id: int, user: UserObject):
        """The method includes a functionality to update the specified user

        Required Permissions:
            Action: users:write
            Scope: users:*

        Args:
            id (int): Specify the id of the user
            user (UserObject): Specify the used UserObject

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and user is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/{id}",
                RequestsMethods.PUT,
                json.dumps(
                    dict(
                        {
                            "email": user.email,
                            "name": user.name,
                            "login": user.login,
                            "theme": user.theme,
                        }
                    )
                ),
            )

            if api_call.get("message") != "User updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully modified the user.")
        else:
            logging.error("There is no id or user defined.")
            raise ValueError

    def get_user_organizations(self, id: int) -> list:
        """The method includes a functionality to get the specified user organizations

        Required Permissions:
            Action: users:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of the user bound organizations
        """

        if id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/{id}/orgs",
            )

            if api_call == list() or api_call[0].get("orgId") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def get_user_teams(self, id: int) -> list:
        """The method includes a functionality to get the specified user teams

        Required Permissions:
            Action: users.teams:read
            Scope: users:*

        Args:
            id (int): Specify the id of the user

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of the user bound teams
        """

        if id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/{id}/teams",
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def switch_specific_user_context(self, user_id: int, org_id: int):
        """The method includes a functionality to switch the user context to the given organization

        Args:
            user_id (int): Specify the user_id
            org_id (int): Specify the org_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0 and org_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USERS.value}/{user_id}/using/{org_id}",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "Active organization changed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated active organization.")
        else:
            logging.error("There is no user_id or org_id defined.")
            raise ValueError


class CurrentUser:
    """The class includes all necessary methods to access the Grafana current user API endpoints. Be aware that all functionalities inside the class maybe only working with basic authentication (username and password)

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_user(self) -> dict:
        """The method includes a functionality to get the current user

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the user information
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.USER.value}",
        )

        if api_call == dict() or api_call.get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def update_password(
        self, old_password: str, new_password: str, confirm_new_password: str
    ):
        """The method includes a functionality to update the current user password

        Args:
            old_password (str): Specify the old_password
            new_password (str): Specify the new_password
            confirm_new_password (str): Specify the confirm_new_password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            len(old_password) != 0
            and len(new_password) != 0
            and len(confirm_new_password) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USER.value}/password",
                RequestsMethods.PUT,
                json.dumps(
                    dict(
                        {
                            "oldPassword": old_password,
                            "newPassword": new_password,
                            "confirmNew": confirm_new_password,
                        }
                    )
                ),
            )

            if api_call.get("message") != "User password changed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the user password.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def switch_current_user_context(self, org_id: int):
        """The method includes a functionality to switch the current user context to the given organization

        Args:
            org_id (int): Specify the organization id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if org_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USER.value}/using/{org_id}",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "Active organization changed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated active organization.")
        else:
            logging.error("There is no org_id defined.")
            raise ValueError

    def get_user_organizations(self) -> list:
        """The method includes a functionality to get the current user organizations

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of organizations
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.USER.value}/orgs",
        )

        if api_call == list() or api_call[0].get("orgId") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_user_teams(self) -> list:
        """The method includes a functionality to get the current user teams

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of teams
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.USER.value}/teams",
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def star_a_dashboard(self, dashboard_id: int):
        """The method includes a functionality to star a dashboard for the current user

        Args:
            dashboard_id (int): Specify the dashboard id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if dashboard_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USER.value}/stars/dashboard/{dashboard_id}",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "Dashboard starred!":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully starred the corresponding dashboard.")
        else:
            logging.error("There is no org_id defined.")
            raise ValueError

    def unstar_a_dashboard(self, dashboard_id: int):
        """The method includes a functionality to unstar a dashboard for the current user

        Args:
            dashboard_id (int): Specify the dashboard id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if dashboard_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USER.value}/stars/dashboard/{dashboard_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Dashboard unstarred":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully unstarred the corresponding dashboard.")
        else:
            logging.error("There is no org_id defined.")
            raise ValueError

    def get_auth_tokens(self) -> list:
        """The method includes a functionality to get the auth tokens for the current user

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of auth tokens of the current user
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.USER.value}/auth-tokens",
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def revoke_auth_token(self, auth_token_id: int):
        """The method includes a functionality to revoke a specified auth token of the current user

        Args:
            auth_token_id (int): Specify the auth_token_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if auth_token_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.USER.value}/revoke-auth-token",
                RequestsMethods.POST,
                json.dumps(dict({"authTokenId": auth_token_id})),
            )

            if api_call.get("message") != "User auth token revoked":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully revoked the corresponding token.")
        else:
            logging.error("There is no auth_token_id defined.")
            raise ValueError
