import sys
import json
import logging
import requests


class GrafanaAPIModel:

    def __init__(self, host: str = None, token: str = None, message: str = None, dashboard_path: str = None,
                 dashboard_name: str = None):
        self.host = host
        self.token = token
        self.message = message
        self.dashboard_path = dashboard_path
        self.dashboard_name = dashboard_name


# https://grafana.com/docs/grafana/latest/http_api/dashboard/
class GrafanaAPI:

    def __init__(self, grafana_api_model: GrafanaAPIModel):
        self.grafana_api_model = grafana_api_model
        self.logging = logging.Logger

    def create_or_update_dashboard(self, dashboard_json: any, overwrite: bool = False):
        folder_id: int = self.get_folder_id_by_dashboard_path()

        dashboard_json_complete: dict = {
            "dashboard": dashboard_json,
            "folderId": folder_id,
            "message": self.grafana_api_model.message,
            "overwrite": overwrite
        }

        api_call = GrafanaAPI.__call_the_api(self, "/api/dashboards/db", "POST", json.dumps(dashboard_json_complete))

        status: str = api_call["status"]

        if status != "success":
            logging.error(f"Check the error: {api_call}.")
            sys.exit(1)
        else:
            logging.info("You successfully deployed the dashboard.")

    def delete_dashboard_by_name_and_path(self):
        dashboard_uids: list = self.get_dashboard_uid_by_name_and_folder()

        if dashboard_uids != list():
            for dashboard_uid in dashboard_uids:
                api_call = GrafanaAPI.__call_the_api(self, f"/api/dashboards/uid/{dashboard_uid}", "DELETE")

                message: str = api_call["message"]

                if f"Dashboard {self.grafana_api_model.dashboard_name} deleted" != message:
                    logging.error(f"Please, check the error: {api_call}.")
                    sys.exit(1)
                else:
                    logging.info("You successfully destroyed the dashboard.")
        else:
            logging.info("Nothing to delete. There is no dashboard available.")

    def get_dashboard_uid_by_name_and_folder(self) -> list:
        folder_id: int = self.get_folder_id_by_dashboard_path()

        search_query: str = f"/api/search?folderIds={folder_id}&query={self.grafana_api_model.dashboard_name}"
        dashboard_meta_list: list = GrafanaAPI.__call_the_api(self, search_query)

        dashboard_uids: list = list()
        for dashboard_meta in dashboard_meta_list:
            dashboard_uids.append(dashboard_meta["uid"])

        return dashboard_uids

    def get_folder_id_by_dashboard_path(self) -> int:
        folders: list = self.get_all_folder_ids_and_names()
        folder_id: int = 0

        for f in folders:
            if self.grafana_api_model.dashboard_path == f["title"]:
                folder_id = f["id"]

        if folder_id == 0:
            logging.error("There's no folder_id available.")
            sys.exit(1)

        return folder_id

    def get_all_folder_ids_and_names(self) -> list:
        folders_raw: list = GrafanaAPI.__call_the_api(self, "/api/search/?folderIds=0")
        folders_raw_len: int = len(folders_raw)
        folders: list = list()

        for i in range(0, folders_raw_len):
            folders.append({"title": folders_raw[i]["title"], "id": folders_raw[i]["id"]})

        return folders

    def __call_the_api(self, api_call: str, method: str = "GET", dashboard_json_complete=None):
        api_url: str = f"{self.grafana_api_model.host}{api_call}"
        headers: dict = {"Authorization": f"Bearer {self.grafana_api_model.token}", "Content-Type": "application/json"}
        try:
            if method == "GET":
                return requests.get(api_url, headers=headers).json()
            elif method == "POST":
                if dashboard_json_complete is not None:
                    return requests.post(api_url, data=dashboard_json_complete, headers=headers).json()
                else:
                    logging.error("Please define the dashbboard_json_complete.")
                    sys.exit(1)
            elif method == "DELETE":
                return requests.delete(api_url, headers=headers).json()
            else:
                logging.error("Please a define valid method.")
                sys.exit(1)
        except Exception as e:
            logging.error(f"Please, check the error: {e}.")
            sys.exit(1)
