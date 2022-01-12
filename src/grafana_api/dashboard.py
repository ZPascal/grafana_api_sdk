import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .folder import Folder
from .utils import Utils


# https://grafana.com/docs/grafana/latest/http_api/dashboard_versions/
# GET /api/dashboards/id/:dashboardId/versions 12.01
# GET /api/dashboards/id/:dashboardId/versions/:id 12.01
# POST /api/dashboards/id/:dashboardId/restore 12.01
# POST /api/dashboards/calculate-diff 12.01
class Dashboard:
    """The class includes all necessary methods to access the Grafana dashboard API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def create_or_update_dashboard(self, dashboard_json: dict, overwrite: bool = False):
        """The method includes a functionality to create the specified dashboard

        Keyword arguments:
        dashboard_json -> Specify the inserted dashboard as dict
        overwrite -> Should the already existing dashboard be overwritten
        """

        folder_id: int = Folder(
            self.grafana_api_model
        ).get_folder_id_by_dashboard_path()

        dashboard_json_complete: dict = {
            "dashboard": dashboard_json,
            "folderId": folder_id,
            "message": self.grafana_api_model.message,
            "overwrite": overwrite,
        }

        api_call: dict = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.DASHBOARDS.value}/db",
            RequestsMethods.POST,
            json.dumps(dashboard_json_complete),
        )

        status: str = api_call["status"]

        if status != "success":
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully deployed the dashboard.")

    def delete_dashboard_by_name_and_path(self):
        """The method includes a functionality to delete the specified dashboard inside the model"""

        dashboard_uid: str = self.get_dashboard_uid_by_name_and_folder()

        if len(dashboard_uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/uid/{dashboard_uid}",
                RequestsMethods.DELETE,
            )

            message: str = api_call["message"]

            if f"Dashboard {self.grafana_api_model.dashboard_name} deleted" != message:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the dashboard.")
        else:
            logging.info("Nothing to delete. There is no dashboard available.")
            raise ValueError

    def get_dashboard_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get the dashboard from the specified uid

        Keyword arguments:
        uid -> Specify the uid of the dashboard
        """

        if len(uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/uid/{uid}"
            )

            if api_call.get("dashboard") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid defined.")
            raise ValueError

    def get_dashboard_home(self) -> dict:
        """The method includes a functionality to get the home dashboard"""

        api_call: dict = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.DASHBOARDS.value}/home"
        )

        if api_call.get("dashboard") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_dashboard_tags(self) -> list:
        """The method includes a functionality to get the all tags of all dashboards"""

        api_call: list = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.DASHBOARDS.value}/tags"
        )

        if api_call == list() or api_call[0].get("term") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_dashboard_uid_by_name_and_folder(self) -> str:
        """The method includes a functionality to extract the dashboard uid specified inside the model"""

        folder_id: int = Folder(
            self.grafana_api_model
        ).get_folder_id_by_dashboard_path()

        search_query: str = f"{APIEndpoints.SEARCH.value}?folderIds={folder_id}&query={self.grafana_api_model.dashboard_name}"
        dashboard_meta: list = Utils(self.grafana_api_model).call_the_api(search_query)

        return dashboard_meta[0]["uid"]

    def get_dashboard_permissions(self, uid: str):
        """The method includes a functionality to extract the dashboard uid specified inside the model

        Keyword arguments:
        uid -> Specify the uid of the dashboard
        """

        if len(uid) != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{uid}/permissions"
            )

            if api_call == list() or api_call[0].get("role") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid defined.")
            raise ValueError

    def update_dashboard_permissions(self, uid: str, permission_json: dict):
        """The method includes a functionality to extract the dashboard uid specified inside the model

        Keyword arguments:
        uid -> Specify the uid of the dashboard
        permission_json -> Specify the inserted permissions as dict
        """

        if len(uid) != 0 and len(permission_json) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{uid}/permissions",
                RequestsMethods.POST,
                json.dumps(permission_json),
            )

            status: str = api_call["message"]

            if status != "Dashboard permissions updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully modified the dashboard permissions.")
        else:
            logging.info("There is no dashboard uid or permission json defined.")
            raise ValueError
