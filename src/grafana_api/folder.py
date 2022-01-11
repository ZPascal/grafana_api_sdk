import logging

from .utils import Utils
from .model import APIModel, APIEndpoints

# https://grafana.com/docs/grafana/latest/http_api/dashboard_versions/
# GET /api/folders 13.01
# GET /api/folders/:uid 13.01
# POST /api/folders 13.01
# PUT /api/folders/:uid 13.01
# DELETE /api/folders/:uid 14.01
# GET /api/folders/id/:id 14.01

# https://grafana.com/docs/grafana/latest/http_api/folder_permissions/
# GET /api/folders/:uid/permissions 14.01
# POST /api/folders/:uid/permissions 14.01
class Folder:

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_folder_id_by_dashboard_path(self) -> int:
        """The method includes a functionality to extract the folder id specified inside model dashboard path"""

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
        """The method extract all folder id and names inside the complete organisation"""

        folders_raw: list = Utils(self.grafana_api_model).call_the_api(f"{APIEndpoints.SEARCH.value}?folderIds=0")
        folders_raw_len: int = len(folders_raw)
        folders: list = list()

        for i in range(0, folders_raw_len):
            folders.append(
                {"title": folders_raw[i]["title"], "id": folders_raw[i]["id"]}
            )

        return folders
