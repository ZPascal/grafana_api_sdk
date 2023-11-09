import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    TeamObject,
)
from .api import Api


class Team:
    """The class includes all necessary methods to access the Grafana team API endpoints. Be aware that all functionalities inside the class only working with the corresponding access rights, please check the following page for details: https://grafana.com/docs/grafana/latest/http_api/team/#team-api & https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/#team-sync-api

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_team(
        self, results_per_page: int = 1000, pages: int = 1, query: str = None
    ) -> dict:
        """The method includes a functionality to get the organization teams specified by the optional pagination functionality

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            pages (int): Specify the pages as integer (default 1)
            query (str): Specify the query (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization teams
        """

        api_request_url: str = (
            f"{APIEndpoints.TEAMS.value}/search?perpage={results_per_page}&page={pages}"
        )

        if query is not None and len(query) != 0:
            api_request_url: str = f"{api_request_url}&query={query}"

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            api_request_url,
        )

        if api_call == dict() or api_call.get("totalCount") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_team_by_id(self, id: int) -> dict:
        """The method includes a functionality to get the organization team specified by the id

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            id (int): Specify the id of the team

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization team
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def add_team(self, team: TeamObject) -> int:
        """The method includes a functionality to add an organization team specified by the TeamObject

        Required Permissions:
            Action: teams:create
            Scope: N/A

        Args:
            team (TeamObject): Specify the team

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
             team_id (int): Returns the team id
        """

        if team is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}",
                RequestsMethods.POST,
                json.dumps(dict({"name": team.name, "email": team.name})),
            )

            if api_call.get("message") != "Team created":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return int(api_call.get("teamId"))
        else:
            logging.error("There is no team defined.")
            raise ValueError

    def update_team(self, id: int, name: str, email: str):
        """The method includes a functionality to update an organization team specified by the team_id, name and email

        Required Permissions:
            Action: teams:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            name (str): Specify the team name
            email (str): Specify the team email

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and len(name) != 0 and len(email) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}",
                RequestsMethods.PUT,
                json.dumps(dict({"name": name, "email": email})),
            )

            if api_call.get("message") != "Team updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the team.")
        else:
            logging.error("There is no id, name or email defined.")
            raise ValueError

    def delete_team_by_id(self, id: int):
        """The method includes a functionality to delete an organization team specified by the team_id

        Required Permissions:
            Action: teams:delete
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Team deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the team.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def get_team_members(self, id: int) -> list:
        """The method includes a functionality to get all organization team users specified by the team_id

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization team members
        """

        if id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/members",
            )

            if api_call == list() or api_call[0].get("userId") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def add_team_member(self, id: int, user_id: int):
        """The method includes a functionality to add an organization team user specified by the team_id and the user_id

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            user_id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and user_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/members",
                RequestsMethods.POST,
                json.dumps(dict({"userId": user_id})),
            )

            if api_call.get("message") != "Member added to Team":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully added a team member.")
        else:
            logging.error("There is no id or user_id defined.")
            raise ValueError

    def delete_team_member(self, id: int, user_id: int):
        """The method includes a functionality to delete an organization team user specified by the team_id and the user_id

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            user_id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and user_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/members/{user_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Team Member removed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully removed a team member.")
        else:
            logging.error("There is no id or user_id defined.")
            raise ValueError

    def get_team_preferences(self, id: int) -> dict:
        """The method includes a functionality to get the organization team preferences specified by the team_id

        Required Permissions:
            Action: teams:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization team preferences
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/preferences",
            )

            if isinstance(api_call, dict) is False or api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def update_team_preferences(
        self,
        id: int,
        theme: str = None,
        timezone: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
    ):
        """The method includes a functionality to update the organization team preferences specified by the team_id, theme, timezone and home_dashboard_id or home_dashboard_uid

        Required Permissions:
            Action: teams:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            theme (str): Specify the team theme e.g. light or dark (default Grafana None)
            timezone (str): Specify the team timezone e.g. utc or browser (default Grafana None)
            home_dashboard_id (int): Specify the home team dashboard by id (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and (
            theme is not None
            or (home_dashboard_id != 0 or home_dashboard_uid is not None)
            or timezone is not None
        ):
            team_preferences: dict = dict()

            if theme is not None:
                team_preferences.update(dict({"theme": theme}))

            if home_dashboard_id != 0 and isinstance(home_dashboard_id, int):
                team_preferences.update(dict({"homeDashboardId": home_dashboard_id}))
            else:
                team_preferences.update({"homeDashboardUID": home_dashboard_uid})

            if timezone is not None:
                team_preferences.update(dict({"timezone": timezone}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/preferences",
                RequestsMethods.PUT,
                json.dumps(team_preferences),
            )

            if api_call.get("message") != "Preferences updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the team preferences.")
        else:
            logging.error(
                "There is no id, theme, home_dashboard_id or timezone defined."
            )
            raise ValueError

    def get_external_groups(
        self,
        id: int,
    ) -> list:
        """The method includes a functionality to get the team groups specified by the team_id. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:read
            Scope: teams:*

        Args:
            id (int): Specify the team id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization team groups
        """

        if id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/groups",
            )

            if isinstance(api_call, list) is False or api_call == list():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no team_id defined.")
            raise ValueError

    def add_external_group(
        self,
        id: int,
        team_group: str,
    ):
        """The method includes a functionality to add a group to the team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            team_group (str): Specify the team group

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and team_group is not None and len(team_group) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/groups",
                RequestsMethods.POST,
                json.dumps(dict({"groupId": team_group})),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            external_group_status_dict: dict = dict(
                {
                    400: "Group is already added to this team.",
                    401: "Unauthorized.",
                    403: "Permission denied.",
                    404: "Team not found.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Group added to Team":
                logging.info("You successfully added the team group.")
            elif 400 <= status_code <= 404:
                logging.error(external_group_status_dict.get(status_code))
                raise Exception
        else:
            logging.error("There is no id or team group defined.")
            raise ValueError

    def remove_external_group(
        self,
        id: int,
        team_group: str,
    ):
        """The method includes a functionality to remove a group from a team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

        Required Permissions:
            Action: teams.permissions:write
            Scope: teams:*

        Args:
            id (int): Specify the team id
            team_group (str): Specify the team group

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and team_group is not None and len(team_group) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.TEAMS.value}/{id}/groups??groupId={team_group.encode('UTF-8')}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            external_group_status_dict: dict = dict(
                {
                    401: "Unauthorized.",
                    403: "Permission denied.",
                    404: "Team not found/Group not found.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Team Group removed":
                logging.info("You successfully removed the team group.")
            elif 400 <= status_code <= 404:
                logging.error(external_group_status_dict.get(status_code))
                raise Exception
        else:
            logging.error("There is no id or team group defined.")
            raise ValueError
