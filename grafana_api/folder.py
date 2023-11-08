import logging
import json

import httpx

from .api import Api
from .model import APIModel, APIEndpoints, RequestsMethods


class Folder:
    """The class includes all necessary methods to access the Grafana folder API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_folders(self) -> list:
        """The method includes a functionality to extract all folders inside the organization

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all folders
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.FOLDERS.value
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_folder_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to extract all folder information specified by the uid of the folder

        Args:
            uid (str): Specify the uid of the folder

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a folder
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}"
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no dashboard uid defined.")
            raise ValueError

    def get_folder_by_id(self, id: int) -> dict:
        """The method includes a functionality to extract all folder information specified by the id of the folder

        Args:
            id (int): Specify the id of the folder

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a folder
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/id/{id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no folder id defined.")
            raise ValueError

    def create_folder(self, title: str, uid: str = None) -> dict:
        """The method includes a functionality to create a new folder inside the organization specified by the defined title and the optional uid

        Args:
            title (str): Specify the title of the folder
            uid (str): Specify the uid of the folder (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a newly created folder
        """

        if len(title) != 0:
            folder_information: dict = dict()
            folder_information.update({"title": title})

            if uid is not None and len(uid) != 0:
                folder_information.update({"uid": uid})

            api_call: dict = Api(self.grafana_api_model).call_the_api(
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
            logging.error("There is no folder uid or title defined.")
            raise ValueError

    def update_folder(
        self, title: str, uid: str, version: int = 0, overwrite: bool = False
    ) -> dict:
        """The method includes a functionality to update a folder information inside the organization specified by the uid, the title, the version of the folder or if folder information be overwritten

        Args:
            title (str): Specify the title of the folder
            uid (str): Specify the uid of the folder
            version (int): Specify the version of the folder (default 0)
            overwrite (bool): Should the already existing folder information be overwritten (default False)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns an updated folder
        """

        if overwrite is True:
            version = None

        if len(title) != 0 and version != 0 and len(uid) != 0:
            folder_information: dict = dict()
            folder_information.update({"title": title})
            folder_information.update({"overwrite": overwrite})
            folder_information.update({"uid": uid})

            if version is not None:
                folder_information.update({"version": version})

            api_call: dict = Api(self.grafana_api_model).call_the_api(
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
            logging.error("There is no folder title, version or uid defined.")
            raise ValueError

    def delete_folder(self, uid: str):
        """The method includes a functionality to delete a folder inside the organization specified by the defined uid

        Args:
            uid (str): Specify the uid of the folder

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0:
            api_call = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}",
                RequestsMethods.DELETE,
            )

            if (
                isinstance(api_call, dict)
                and api_call.get("message") != "Folder deleted"
            ):
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            elif isinstance(api_call, httpx.Response) and api_call.status_code != 200:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the folder.")
        else:
            logging.error("There is no folder uid defined.")
            raise ValueError

    def get_folder_permissions(self, uid: str) -> list:
        """The method includes a functionality to extract the folder permissions inside the organization specified by the defined uid

        Args:
            uid (str): Specify the uid of the folder

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of folder permissions
        """

        if len(uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}/permissions",
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("folderId") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no folder uid defined.")
            raise ValueError

    def update_folder_permissions(self, uid: str, permission_json: dict):
        """The method includes a functionality to update the folder permissions based on the specified uid and the permission json document

        Args:
            uid (str): Specify the uid of the folder
            permission_json (dict): Specify the inserted permissions as dict

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0 and len(permission_json) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.FOLDERS.value}/{uid}/permissions",
                RequestsMethods.POST,
                json.dumps(permission_json),
            )

            if api_call.get("message") not in [
                "Dashboard permissions updated",
                "Folder permissions updated",
            ]:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully modified the folder permissions.")
        else:
            logging.error("There is no folder uid or permission json defined.")
            raise ValueError

    def get_folder_id_by_dashboard_path(self, dashboard_path: str) -> int:
        """The method includes a functionality to extract the folder id specified inside model dashboard path

        Args:
            dashboard_path (str): Specify the dashboard path

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            folder_id (int): Returns the folder id
        """

        if dashboard_path.lower() == "general":
            return 0

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
            logging.error("There is no dashboard_path defined.")
            raise ValueError

    def get_all_folder_ids_and_names(self) -> list:
        """The method extract all folder id and names inside the complete organisation

        Returns:
            folders (list): Returns a list of dicts with folder ids and the corresponding names
        """

        folders_raw: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SEARCH.value}?folderIds=0"
        )
        folders_raw_len: int = len(folders_raw)
        folders: list = list()

        for i in range(0, folders_raw_len):
            folders.append(
                {"title": folders_raw[i].get("title"), "id": folders_raw[i].get("id")}
            )

        return folders
