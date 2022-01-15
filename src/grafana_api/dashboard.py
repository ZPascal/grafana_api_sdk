import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .folder import Folder
from .utils import Utils


class Dashboard:
    """The class includes all necessary methods to access the Grafana dashboard API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def create_or_update_dashboard(
        self,
        dashboard_path: str,
        dashboard_json: dict,
        message: str,
        overwrite: bool = False,
    ):
        """The method includes a functionality to create the specified dashboard

        Keyword arguments:
        dashboard_path -> Specify the dashboard path in which the dashboard is to be placed
        dashboard_json -> Specify the inserted dashboard as dict
        message -> Specify the message that should be injected as commit message inside the dashboard
        overwrite -> Should the already existing dashboard be overwritten
        """

        if len(dashboard_path) != 0 and dashboard_json != dict() and len(message) != 0:
            folder_id: int = Folder(
                self.grafana_api_model
            ).get_folder_id_by_dashboard_path(dashboard_path)

            dashboard_json_complete: dict = {
                "dashboard": dashboard_json,
                "folderId": folder_id,
                "message": message,
                "overwrite": overwrite,
            }

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/db",
                RequestsMethods.POST,
                json.dumps(dashboard_json_complete),
            )

            if api_call.get("status") != "success":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deployed the dashboard.")
        else:
            logging.info(
                "There is no dashboard_path or dashboard_json or message defined."
            )
            raise ValueError

    def delete_dashboard_by_name_and_path(
        self, dashboard_name: str, dashboard_path: str
    ):
        """The method includes a functionality to delete the specified dashboard inside the model

        dashboard_name -> Specify the dashboard name of the deleted dashboard
        dashboard_path -> Specify the dashboard path of the deleted dashboard
        """

        if len(dashboard_name) != 0 and len(dashboard_path) != 0:
            dashboard_uid: dict = self.get_dashboard_uid_and_id_by_name_and_folder(
                dashboard_name, dashboard_path
            )

            if len(dashboard_uid) != 0:
                api_call: dict = Utils(self.grafana_api_model).call_the_api(
                    f"{APIEndpoints.DASHBOARDS.value}/uid/{dashboard_uid.get('uid')}",
                    RequestsMethods.DELETE,
                )

                if f"Dashboard {dashboard_name} deleted" != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully destroyed the dashboard.")
            else:
                logging.info("Nothing to delete. There is no dashboard available.")
                raise ValueError
        else:
            logging.info("There is no dashboard_name or dashboard_path defined.")
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

    def get_dashboard_uid_and_id_by_name_and_folder(
        self, dashboard_name: str, dashboard_path: str
    ) -> dict:
        """The method includes a functionality to extract the dashboard uid specified inside the model

        dashboard_name -> Specify the dashboard name of the dashboard
        dashboard_path -> Specify the dashboard path of the dashboard
        """

        if len(dashboard_name) != 0 and len(dashboard_path) != 0:
            folder_id: int = Folder(
                self.grafana_api_model
            ).get_folder_id_by_dashboard_path(dashboard_path)

            search_query: str = f"{APIEndpoints.SEARCH.value}?folderIds={folder_id}&query={dashboard_name}"
            dashboard_meta: list = Utils(self.grafana_api_model).call_the_api(
                search_query
            )

            return dict(
                {"uid": dashboard_meta[0]["uid"], "id": dashboard_meta[0]["id"]}
            )
        else:
            logging.info("There is no dashboard_name or dashboard_path defined.")
            raise ValueError

    def get_dashboard_permissions(self, id: int) -> list:
        """The method includes a functionality to extract the dashboard permissions based on the specified id

        Keyword arguments:
        id -> Specify the id of the dashboard
        """

        if id != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{id}/permissions"
            )

            if api_call == list() or api_call[0].get("role") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid defined.")
            raise ValueError

    def update_dashboard_permissions(self, id: int, permission_json: dict):
        """The method includes a functionality to update the dashboard permissions based on the specified id
            and the permission json document

        Keyword arguments:
        id -> Specify the id of the dashboard
        permission_json -> Specify the inserted permissions as dict
        """

        if id != 0 and len(permission_json) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{id}/permissions",
                RequestsMethods.POST,
                json.dumps(permission_json),
            )

            if api_call.get("message") != "Dashboard permissions updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully modified the dashboard permissions.")
        else:
            logging.info("There is no dashboard uid or permission json defined.")
            raise ValueError

    def get_dashboard_versions(self, id: int) -> list:
        """The method includes a functionality to extract the versions of a dashboard based on the specified id

        Keyword arguments:
        id -> Specify the id of the dashboard
        """

        if id != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{id}/versions",
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid defined.")
            raise ValueError

    def get_dashboard_version(self, id: int, version_id: int) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        id -> Specify the id of the dashboard
        version_id -> Specify the version_id of a dashboard
        """

        if id != 0 and version_id != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{id}/versions/{version_id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid or version_id defined.")
            raise ValueError

    def restore_dashboard_version(self, id: int, version: dict):
        """The method includes a functionality to restore a specified version of a dashboard based on the specified \
        dashboard uid and a version as dict of the dashboard

        Keyword arguments:
        uid -> Specify the id of the dashboard
        version -> Specify the version_id of a dashboard
        """

        if id != 0 and version != dict():
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DASHBOARDS.value}/id/{id}/restore",
                RequestsMethods.POST,
                json.dumps(version),
            )

            if (
                api_call.get("status") != "success"
                or api_call.get("message") is not None
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully restored the dashboard.")
        else:
            logging.info("There is no dashboard uid or version_id defined.")
            raise ValueError

    def calculate_dashboard_diff(
        self,
        dashboard_id_and_version_base: dict,
        dashboard_id_and_version_new: dict,
        diff_type: str = "json",
    ) -> str:
        """The method includes a functionality to calculate the diff of specified versions of a dashboard based on the \
        specified dashboard uid and the selected version of the base dashboard and the new dashboard and the diff \
        type (basic or json)

        Keyword arguments:
        dashboard_id_and_version_base -> Specify the version and id of the base dashboard
        dashboard_id_and_version_new -> Specify the version and id of the new dashboard
        diff_type -> Specify the diff type (basic or json the default is json)
        """
        possible_diff_types: list = list(["basic", "json"])

        if diff_type.lower() in possible_diff_types:
            if (
                dashboard_id_and_version_base != dict()
                and dashboard_id_and_version_new != 0
            ):
                diff_object: dict = dict()
                diff_object.update(dashboard_id_and_version_base)
                diff_object.update(dashboard_id_and_version_new)
                diff_object.update({"diffType": diff_type.lower()})

                api_call: any = Utils(
                    self.grafana_api_model
                ).call_the_api_non_json_output(
                    f"{APIEndpoints.DASHBOARDS.value}/calculate-diff",
                    RequestsMethods.POST,
                    json.dumps(diff_object),
                )

                if api_call.status_code != 200:
                    logging.error(f"Check the error: {api_call.text}.")
                    raise Exception
                else:
                    return api_call.text
            else:
                logging.info(
                    "There is no dashboard_uid_and_version_base or dashboard_uid_and_version_new defined."
                )
                raise ValueError
        else:
            logging.info(
                f"The diff_type: {diff_type.lower()} is not valid. Please specify a valid value."
            )
            raise ValueError
