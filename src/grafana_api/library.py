import json
import logging

from .model import APIModel, APIEndpoints, SortDirection, RequestsMethods
from .api import Api


class Library:
    """The class includes all necessary methods to access the Grafana library API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_library_elements(
        self,
        results_per_page: int = 100,
        pages: int = 1,
        search_string: str = None,
        kind: int = 1,
        sort_direction: SortDirection = SortDirection.DESC,
        types_filter: str = None,
        exclude_uid: str = None,
        folder_filter_ids: str = None,
    ) -> dict:
        """The method includes a functionality to get a list of all library elements the authenticated user has permission to view. Use the perPage query parameter to control the maximum number of library elements returned, The default limit is 100. You can also use the page query parameter to fetch library elements from any page other than the first one

         Args:
            results_per_page (int): Specify the results_per_page as integer (default 100)
            pages (int): Specify the pages as integer (default 1)
            search_string (str): Specify the search string (default None)
            kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
            sort_direction (SortDirection): Specify the sort order of elements. Use alpha-asc for ascending and alpha-desc for descending sort order (default alpha-desc)
            types_filter (str): Specify a comma separated list of types to filter the elements by (default None)
            exclude_uid (str): Specify the element uid to exclude from search results (default None)
            folder_filter_ids (str): Specify a comma separated list of folder ID(s) to filter the elements by (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the library elements
        """

        additional_parameters: str = ""
        if search_string is not None and len(search_string) != 0:
            additional_parameters += f"&searchString={search_string}"

        if types_filter is not None and len(types_filter) != 0:
            additional_parameters += f"&typeFilter={types_filter}"

        if exclude_uid is not None and len(exclude_uid) != 0:
            additional_parameters += f"&excludeUid={exclude_uid}"

        if folder_filter_ids is not None and len(folder_filter_ids) != 0:
            additional_parameters += f"&folderFilter={folder_filter_ids}"

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.LIBRARY.value}?perpage={results_per_page}&page={pages}&kind={kind}"
            f"&sortDirection={sort_direction}{additional_parameters}",
        )

        if api_call == dict() or api_call.get("result") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_library_element_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get a library element with the given uid

         Args:
            uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding library element
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LIBRARY.value}/{uid}",
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def get_library_element_by_name(self, name: str) -> dict:
        """The method includes a functionality to get a library element with the given name

         Args:
            name (str): Specify the name of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding library element
        """

        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LIBRARY.value}/name/{name}",
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no name defined.")
            raise ValueError

    def get_library_element_connections(self, uid: str) -> dict:
        """The method includes a functionality to get a list of connections for a library element based on the specified uid

         Args:
            uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding list of connections
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LIBRARY.value}/{uid}/connections",
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def create_library_element(
        self,
        folder_id: int,
        model: dict,
        kind: int = 1,
        folder_uid: str = None,
        name: str = None,
        uid: str = None,
    ) -> dict:
        """The method includes a functionality to create a library element based on the specified folder id and model

         Args:
             folder_id (int): Specify the folder where the library element is stored. It is deprecated since Grafana v9
             model (dict): Specify the JSON model for the library element
             kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
             folder_uid (str): Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder (default None)
             name (str): Specify the name of the library element (default None)
             uid (str): Specify the uid of the library element (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created library element
        """

        if (
            folder_id != 0
            and model is not None
            and model != dict()
            and kind is not None
            and kind != 0
        ):
            request_parameters: dict = dict(
                {"folderId": folder_id, "model": model, "kind": kind}
            )

            if folder_uid is not None and len(folder_uid) != 0:
                request_parameters.update({"folderUid": folder_uid})

            if name is not None and len(name) != 0:
                request_parameters.update({"name": name})

            if uid is not None and len(uid) != 0:
                request_parameters.update({"uid": uid})

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.LIBRARY.value,
                RequestsMethods.POST,
                json.dumps(request_parameters),
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no folder_id, kind or model defined.")
            raise ValueError

    def update_library_element(
        self,
        uid: str,
        folder_id: int,
        folder_uid: str,
        name: str,
        model: dict,
        version: int,
        kind: int = 1,
    ) -> dict:
        """The method includes a functionality to update a library element

         Args:
             uid (str): Specify the uid of the library element
             folder_id (int): Specify the folder where the library element is stored. It is deprecated since Grafana v9
             folder_uid (str): Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder
             name (str): Specify the name of the library element
             model (dict): Specify the JSON model for the library element
             version (int): Specify the version for the library element
             kind (int): Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated library element
        """

        if (
            len(uid) != 0
            and folder_id != 0
            and len(folder_uid) != 0
            and len(name) != 0
            and model is not None
            and model != dict()
            and version != 0
            and kind is not None
            and kind != 0
        ):
            request_parameters: dict = dict(
                {
                    "uid": uid,
                    "folderId": folder_id,
                    "folderUid": folder_uid,
                    "name": name,
                    "model": model,
                    "version": version,
                    "kind": kind,
                }
            )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LIBRARY.value}/{uid}",
                RequestsMethods.PATCH,
                json.dumps(request_parameters),
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no folder_id, folder_uid, name, version, kind or model defined."
            )
            raise ValueError

    def delete_library_element(self, uid: str):
        """The method includes a functionality to delete a library element specified by the uid

         Args:
             uid (str): Specify the uid of the library element

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LIBRARY.value}/{uid}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Library element deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully deleted the corresponding Library element."
                )
        else:
            logging.error("There is no uid defined.")
            raise ValueError
