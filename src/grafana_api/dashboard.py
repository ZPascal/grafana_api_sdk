import json
import logging
import requests

from grafana_api.model import APIModel, APIEndpoints, RequestsMethods


# https://grafana.com/docs/grafana/latest/http_api/dashboard/
class Dashboard:
    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model
        self.logging = logging.Logger

    def create_or_update_dashboard(self, dashboard_json: dict, overwrite: bool = False):
        folder_id: int = self.get_folder_id_by_dashboard_path()

        dashboard_json_complete: dict = {
            "dashboard": dashboard_json,
            "folderId": folder_id,
            "message": self.grafana_api_model.message,
            "overwrite": overwrite,
        }

        api_call: dict = Dashboard.__call_the_api(
            self,
            f"{APIEndpoints.DASHBOARDS.value}/db",
            RequestsMethods.POST,
            json.dumps(dashboard_json_complete),
        )

        print(api_call)

        status: str = api_call["status"]

        if status != "success":
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully deployed the dashboard.")

    def delete_dashboard_by_name_and_path(self):
        dashboard_uids: str = self.get_dashboard_uid_by_name_and_folder()

        if len(dashboard_uids) != 0:
            for dashboard_uid in dashboard_uids:
                api_call: dict = Dashboard.__call_the_api(
                    self,
                    f"{APIEndpoints.DASHBOARDS.value}/uid/{dashboard_uid}",
                    RequestsMethods.DELETE,
                )

                message: str = api_call["message"]

                if (
                    f"Dashboard {self.grafana_api_model.dashboard_name} deleted"
                    != message
                ):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully destroyed the dashboard.")
        else:
            logging.info("Nothing to delete. There is no dashboard available.")

    def get_dashboard_uid_by_name_and_folder(self) -> str:
        folder_id: int = self.get_folder_id_by_dashboard_path()

        search_query: str = f"{APIEndpoints.SEARCH.value}?folderIds={folder_id}&query={self.grafana_api_model.dashboard_name}"
        dashboard_meta: list = Dashboard.__call_the_api(self, search_query)

        return dashboard_meta[0]["uid"]

    def get_folder_id_by_dashboard_path(self) -> int:
        folders: list = self.get_all_folder_ids_and_names()
        folder_id: int = 0

        for f in folders:
            if self.grafana_api_model.dashboard_path == f["title"]:
                folder_id = f["id"]

        if folder_id == 0:
            logging.error(
                f"There's no folder_id for the dashboard named {self.grafana_api_model.dashboard_path} available."
            )
            raise Exception

        return folder_id

    def get_all_folder_ids_and_names(self) -> list:
        folders_raw: list = Dashboard.__call_the_api(
            self, f"{APIEndpoints.SEARCH.value}?folderIds=0"
        )
        folders_raw_len: int = len(folders_raw)
        folders: list = list()

        print(folders_raw)

        for i in range(0, folders_raw_len):
            folders.append(
                {"title": folders_raw[i]["title"], "id": folders_raw[i]["id"]}
            )

        return folders

    def __call_the_api(
        self,
        api_call: str,
        method: RequestsMethods = RequestsMethods.GET,
        dashboard_json_complete: str = None,
    ) -> any:
        api_url: str = f"{self.grafana_api_model.host}{api_call}"

        print(api_url)
        print(dashboard_json_complete)

        headers: dict = {
            "Authorization": f"Bearer {self.grafana_api_model.token}",
            "Content-Type": "application/json",
        }
        try:
            if method.value == RequestsMethods.GET.value:
                return requests.get(api_url, headers=headers).json()
            elif method.value == RequestsMethods.POST.value:
                if dashboard_json_complete is not None:
                    return requests.post(
                        api_url, data=dashboard_json_complete, headers=headers
                    ).json()
                else:
                    logging.error("Please define the dashboard_json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return requests.delete(api_url, headers=headers).json()
        except Exception as e:
            logging.error(f"Please a define valid method and check the error: {e}.")
            raise e
