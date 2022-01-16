import logging
import json

from .utils import Utils
from .model import APIModel, APIEndpoints, RequestsMethods


class Folder:
    """The class includes all necessary methods to access the Grafana folder API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_folders(self) -> list:
        """The method includes a functionality to extract all folders inside the organization"""

        api_call: list = Utils(self.grafana_api_model).call_the_api(
            APIEndpoints.FOLDERS.value
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_folder_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to extract all folder information specified by the uid of the folder

        Keyword arguments:
        uid -> Specify the uid of the folder
        """

        if len(uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}"
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no dashboard uid defined.")
            raise ValueError

    def get_folder_by_id(self, id: int) -> dict:
        """The method includes a functionality to extract all folder information specified by the id of the folder

        Keyword arguments:
        id -> Specify the id of the folder
        """

        if id != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/id/{id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no folder id defined.")
            raise ValueError

    def create_folder(self, title: str, uid: str = None) -> dict:
        """The method includes a functionality to create a new folder inside the organization specified by the \
        defined title and the optional uid

        Keyword arguments:
        title -> Specify the title of the folder
        uid -> Specify the uid of the folder (the default value is None)
        """

        if len(title) != 0:
            folder_information: dict = dict()
            folder_information.update({"title": title})

            if uid is not None and len(uid) != 0:
                folder_information.update({"uid": uid})

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                APIEndpoints.FOLDERS.value,
                RequestsMethods.POST,
                json.dumps(folder_information),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no folder uid or title defined.")
            raise ValueError

    def update_folder(
        self, title: str, uid: str = None, version: int = 0, overwrite: bool = False
    ) -> dict:
        """The method includes a functionality to update a folder information inside the organization specified \
        by the uid, the title, the version of the folder or if folder information be overwritten

        Keyword arguments:
        uid -> Specify the uid of the folder
        title -> Specify the title of the folder
        version -> Specify the version of the folder
        overwrite -> Should the already existing folder information be overwritten
        """

        if overwrite is True:
            version = None

        if len(title) != 0 and version != 0:
            folder_information: dict = dict()
            folder_information.update({"title": title})
            folder_information.update({"overwrite": overwrite})

            if uid is not None and len(uid) != 0:
                folder_information.update({"uid": uid})

            if version is not None:
                folder_information.update({"version": version})

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}",
                RequestsMethods.PUT,
                json.dumps(folder_information),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no folder title or version defined.")
            raise ValueError

    def delete_folder(self, uid: str):
        """The method includes a functionality to delete a folder inside the organization specified by the \
        defined uid

        Keyword arguments:
        uid -> Specify the uid of the folder
        """

        if len(uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}",
                RequestsMethods.DELETE,
            )

            if "Folder deleted" != api_call.get("message"):
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the folder.")
        else:
            logging.info("There is no folder uid defined.")
            raise ValueError

    def get_folder_permissions(self, uid: str) -> list:
        """The method includes a functionality to extract the folder permissions inside the organization specified by \
        the defined uid

        Keyword arguments:
        uid -> Specify the uid of the folder
        """

        if len(uid) != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}/permissions",
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.info("There is no folder uid defined.")
            raise ValueError

    def update_folder_permissions(self, uid: str, permission_json: dict):
        """The method includes a functionality to update the folder permissions based on the specified uid \
            and the permission json document

        Keyword arguments:
        uid -> Specify the uid of the folder
        permission_json -> Specify the inserted permissions as dict
        """

        if len(uid) != 0 and len(permission_json) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}/permissions",
                RequestsMethods.POST,
                json.dumps(permission_json),
            )

            if api_call.get("message") != "Folder permissions updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully modified the folder permissions.")
        else:
            logging.info("There is no folder uid or permission json defined.")
            raise ValueError

    def get_folder_id_by_dashboard_path(self, dashboard_path: str) -> int:
        """The method includes a functionality to extract the folder id specified inside model dashboard path"""

        if len(dashboard_path) != 0:
            folders: list = self.get_all_folder_ids_and_names()
            folder_id: int = 0

            for f in folders:
                if dashboard_path == f.get("title"):
                    folder_id = f.get("id")

            if folder_id == 0:
                logging.error(
                    f"There's no folder_id for the dashboard named {dashboard_path} available."
                )
                raise Exception

            return folder_id
        else:
            logging.info("There is no dashboard_path defined.")
            raise ValueError

    def get_all_folder_ids_and_names(self) -> list:
        """The method extract all folder id and names inside the complete organisation"""

        folders_raw: list = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SEARCH.value}?folderIds=0"
        )
        folders_raw_len: int = len(folders_raw)
        folders: list = list()

        for i in range(0, folders_raw_len):
            folders.append(
                {"title": folders_raw[i].get("title"), "id": folders_raw[i].get("id")}
            )

        return folders
