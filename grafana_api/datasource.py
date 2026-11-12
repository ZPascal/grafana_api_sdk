import json
import logging
from typing import Any, Optional
from urllib.parse import quote

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    DatasourceCache,
    DatasourcePermission,
)
from .api import Api
from .deprecation import _deprecated

_PERMISSION_UPDATE_METHODS: str = (
    "DatasourcePermissions.update_datasource_user_access_by_uid, "
    "DatasourcePermissions.update_datasource_team_access_by_uid or "
    "DatasourcePermissions.update_datasource_basic_role_access_by_uid"
)


class Datasource:
    """The class includes all necessary methods to access the Grafana datasource API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model

    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_datasources(self) -> list:
        """The method includes a functionality to get all datasources.

        Required Permissions:
            Action: datasources:read
            Scope: datasources:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of all datasources

        """
        api_call: list = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.DATASOURCES.value,
            RequestsMethods.GET,
        )

        if api_call == [] or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    @_deprecated("use Datasource.get_datasource_by_uid instead", removed=True)
    def get_datasource_by_id(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource id.

        REMOVED: Recent Grafana versions removed this endpoint and answer with 404 Not found, so the call fails there. Use Datasource.get_datasource_by_uid instead.

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if datasource_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}",
                RequestsMethods.GET,
            )

            if api_call == {} or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    def get_datasource_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{uid}",
                RequestsMethods.GET,
            )

            if api_call == {} or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    @_deprecated("use Datasource.get_datasource_by_uid instead")
    def get_datasource_by_name(self, name: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource name.

        DEPRECATED: Use Datasource.get_datasource_by_uid instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/name/{name}",
                RequestsMethods.GET,
            )

            if api_call == {} or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no name defined.")
            raise ValueError

    @_deprecated("use Datasource.get_datasource_by_uid (read the uid from the result of Datasource.get_all_datasources) instead")
    def get_datasource_id_by_name(self, name: str) -> int:
        """The method includes a functionality to get the datasource id specified by the datasource name.

        DEPRECATED: Use Datasource.get_datasource_by_uid (read the uid from the result of Datasource.get_all_datasources) instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns a datasource id

        """
        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/id/{name}",
                RequestsMethods.GET,
            )

            if api_call == {} or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return int(api_call.get("id"))
        else:
            logging.error("There is no name defined.")
            raise ValueError

    def create_datasource(self, data_source: dict):
        """The method includes a functionality to create a datasource specified by the datasource as dict.

        Args:
            data_source (dict): Specify the datasource as dict

        Required Permissions:
            Action: datasources:create

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if data_source != {}:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.DATASOURCES.value,
                RequestsMethods.POST,
                json.dumps(data_source),
            )

            if api_call.get("message") != "Datasource added":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created a datasource.")
        else:
            logging.error("There is no data_source defined.")
            raise ValueError

    def update_datasource(self, data_source: dict, datasource_id: int = 0, datasource_uid: Optional[str] = None):
        """The method includes a functionality to update a datasource specified by the datasource as dict and the datasource id/ datasource uid.

        Args:
            data_source (dict): Specify the datasource as dict
            datasource_id (int): Specify the id of the datasource (default 0)
            datasource_uid (str): Specify the uid of the datasource (default None)

        Required Permissions:
            Action: datasources:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if data_source != {} and (datasource_id != 0 or datasource_uid is not None):
            if datasource_uid is not None:
                endpoint = f"{APIEndpoints.DATASOURCES.value}/uid/{datasource_uid}"
            else:
                endpoint = f"{APIEndpoints.DATASOURCES.value}/{datasource_id}"
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                endpoint,
                RequestsMethods.PUT,
                json.dumps(data_source),
            )

            if api_call.get("message") != "Datasource updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated a datasource.")
        else:
            logging.error("There is no datasource_id, dashboard_uid or data_source defined.")
            raise ValueError

    @_deprecated("use Datasource.delete_datasource_by_uid instead", removed=True)
    def delete_datasource_by_id(self, datasource_id: int):
        """The method includes a functionality to delete a datasource specified by the datasource id.

        REMOVED: Recent Grafana versions removed this endpoint and answer with 404 Not found, so the call fails there. Use Datasource.delete_datasource_by_uid instead.

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if datasource_id != 0 :
            endpoint = f"{APIEndpoints.DATASOURCES.value}/{datasource_id}"

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                endpoint,
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Data source deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a datasource.")
                return
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    def delete_datasource_by_uid(self, uid: str):
        """The method includes a functionality to delete a datasource specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{uid}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Data source deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a datasource.")
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    @_deprecated("use Datasource.delete_datasource_by_uid instead")
    def delete_datasource_by_name(self, name: str):
        """The method includes a functionality to delete a datasource specified by the datasource name.

        DEPRECATED: Use Datasource.delete_datasource_by_uid instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            name (str): Specify the name of the datasource

        Required Permissions:
            Action: datasources:delete
            Scope: [datasources:*, datasources:name:*, datasources:name:<name>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/name/{name}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Data source deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a datasource.")
        else:
            logging.error("There is no name defined.")
            raise ValueError

    @_deprecated("use Datasource.query_datasource_by_uid instead")
    def query_datasource_by_id(
        self, time: str, to: str, datasource_queries: list
    ) -> dict:
        """The method includes a functionality to execute a queries inside the datasource itself specified by the datasource id.

        DEPRECATED: Use Datasource.query_datasource_by_uid instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            time (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            to (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            datasource_queries (list): Specify a list of execution queries based on the DatasourceQuery class

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified query

        """
        if len(time) != 0 and len(to) != 0 and datasource_queries != []:
            datasource_queries_json_list: list = []

            for datasource_query in datasource_queries:
                if datasource_query.datasource_id != 0:
                    datasource_query_json_dict: dict = {
                            "refId": datasource_query.ref_id,
                            "intervalMs": datasource_query.interval_ms,
                            "maxDataPoints": datasource_query.max_data_points,
                            "datasourceId": datasource_query.datasource_id,
                            "rawSql": datasource_query.raw_sql,
                            "format": datasource_query.output_format,
                        }
                    datasource_queries_json_list.append(datasource_query_json_dict)
                else:
                    logging.error("There is no datasource_id defined.")
                    raise ValueError

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.DATASOURCE_LEGACY_QUERY.value,
                RequestsMethods.POST,
                json.dumps(
                    {"from": time, "to": to, "queries": datasource_queries_json_list}
                ),
            )

            if not api_call.get("results"):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call.get("results")
        else:
            logging.error("There is no time, to or datasource_queries defined.")
            raise ValueError

    def query_datasource_by_uid(
        self, time: str, to: str, datasource_queries: list
    ) -> dict:
        """The method includes a functionality to execute a queries inside the datasource itself specified by the datasource uid.

        Args:
            time (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            to (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            datasource_queries (list): Specify a list of execution queries based on the DatasourceQuery class

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified query

        """
        if len(time) != 0 and len(to) != 0 and datasource_queries != []:
            datasource_queries_json_list: list = []

            for datasource_query in datasource_queries:
                if len(datasource_query.datasource_uid) != 0:
                    datasource_query_json_dict: dict = {
                            "refId": datasource_query.ref_id,
                            "intervalMs": datasource_query.interval_ms,
                            "maxDataPoints": datasource_query.max_data_points,
                            "datasource": {"uid": datasource_query.datasource_uid},
                            "rawSql": datasource_query.raw_sql,
                            "format": datasource_query.output_format,
                        }
                    datasource_queries_json_list.append(datasource_query_json_dict)
                else:
                    logging.error("There is no datasource_uid defined.")
                    raise ValueError

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.DATASOURCE_QUERY.value,
                RequestsMethods.POST,
                json.dumps(
                    {"from": time, "to": to, "queries": datasource_queries_json_list}
                ),
            )

            if not api_call.get("results"):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call.get("results")
        else:
            logging.error("There is no time, to or datasource_queries defined.")
            raise ValueError

    def get_datasource_health_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to check the health of the datasource specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:query
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the health check result of the datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{uid}/health",
                RequestsMethods.GET,
            )

            if api_call.get("status") != "OK":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def get_datasource_resource_by_uid(self, uid: str, resource_path: str) -> Any:
        """The method includes a functionality to call a plugin resource of the datasource specified by the datasource uid and the resource path.

        Args:
            uid (str): Specify the uid of the datasource
            resource_path (str): Specify the path of the plugin resource (for example labels). A query string is forwarded as part of the path (for example labels?start=1). Path traversal segments (..) aren't allowed

        Required Permissions:
            Action: datasources:query
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<uid>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the decoded JSON response of the datasource plugin resource (an empty dict or list is a valid result) or the raw HTTP response if the plugin resource doesn't return JSON

        """
        resource_path = resource_path.lstrip("/")

        if len(uid) != 0 and len(resource_path) != 0 and ".." not in resource_path.split("/"):
            return Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/uid/{uid}/resources/{resource_path}",
                RequestsMethods.GET,
            )
        else:
            logging.error("There is no uid or a valid resource_path defined.")
            raise ValueError


class DatasourcePermissions:
    """The class includes all necessary methods to access the Grafana datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model

    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    @staticmethod
    def _ds_type_query(ds_type: Optional[str]) -> str:
        """The method builds the optional ds_type query string.

        Args:
            ds_type (str): Specify the optional plugin type of the datasource

        Returns:
            query (str): Returns the query string or an empty string

        """
        return f"?ds_type={quote(ds_type, safe='')}" if ds_type else ""

    def get_datasource_permissions_by_uid(
        self, uid: str, ds_type: Optional[str] = None
    ) -> list:
        """The method includes a functionality to get the datasource permissions specified by the datasource uid. The functionality is a Grafana ENTERPRISE feature.

        Args:
            uid (str): Specify the uid of the datasource
            ds_type (str): Specify the optional plugin type of the datasource (for example prometheus). It's necessary if more than one datasource in the organisation uses the same uid (default None)

        Required Permissions:
            Action: datasources.permissions:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the datasource permissions

        """
        if len(uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCE_PERMISSIONS.value}/{uid}{self._ds_type_query(ds_type)}",
                RequestsMethods.GET,
                response_status_code=True,
            )

            status_code: int = (
                api_call[0].get("status")
                if isinstance(api_call, list)
                else api_call.get("status")
            )

            datasource_permissions_status_dict: dict = {
                    401: "Unauthorized.",
                    403: "Access Denied.",
                    500: "Internal error.",
                }

            if status_code == 200:
                return api_call
            elif 401 <= status_code <= 500:
                logging.error(datasource_permissions_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def update_datasource_user_access_by_uid(
        self,
        uid: str,
        id: int,
        datasource_user_permission: DatasourcePermission,
        ds_type: Optional[str] = None,
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the user id. The functionality is a Grafana ENTERPRISE feature.

        Args:
            uid (str): Specify the uid of the datasource
            id (int): Specify the id of the user
            datasource_user_permission (DatasourcePermission): Specify the datasource user permission
            ds_type (str): Specify the optional plugin type of the datasource (for example prometheus). It's necessary if more than one datasource in the organisation uses the same uid (default None)

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if (
            len(uid) != 0
            and id != 0
            and datasource_user_permission.permission is not None
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCE_PERMISSIONS.value}/{uid}/users/{id}{self._ds_type_query(ds_type)}",
                RequestsMethods.POST,
                json.dumps({"permission": datasource_user_permission.permission}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            datasource_permissions_status_dict: dict = {
                    400: "Permission cannot be added, see response body for details.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                }

            if status_code == 200 and api_call.get("message") == "Permission updated":
                logging.info("You successfully updated the datasource user permission.")
            elif status_code == 200 and api_call.get("message") == "Permission removed":
                logging.info("You successfully removed the datasource user permission.")
            elif 400 == status_code:
                logging.error(
                    f"{datasource_permissions_status_dict.get(status_code)} | Response: {api_call}"
                )
                raise Exception
            elif 401 <= status_code <= 403:
                logging.error(datasource_permissions_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error(
                "There is no uid, id or datasource_user_permission object defined."
            )
            raise ValueError

    def update_datasource_team_access_by_uid(
        self,
        uid: str,
        id: int,
        datasource_team_permission: DatasourcePermission,
        ds_type: Optional[str] = None,
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the team id. The functionality is a Grafana ENTERPRISE feature.

        Args:
            uid (str): Specify the uid of the datasource
            id (int): Specify the id of the team
            datasource_team_permission (DatasourcePermission): Specify the datasource team permission
            ds_type (str): Specify the optional plugin type of the datasource (for example prometheus). It's necessary if more than one datasource in the organisation uses the same uid (default None)

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if (
            len(uid) != 0
            and id != 0
            and datasource_team_permission.permission is not None
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCE_PERMISSIONS.value}/{uid}/teams/{id}{self._ds_type_query(ds_type)}",
                RequestsMethods.POST,
                json.dumps({"permission": datasource_team_permission.permission}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            datasource_permissions_status_dict: dict = {
                    400: "Permission cannot be added, see response body for details.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                }

            if status_code == 200 and api_call.get("message") == "Permission updated":
                logging.info("You successfully updated the datasource team permission.")
            elif status_code == 200 and api_call.get("message") == "Permission removed":
                logging.info("You successfully removed the datasource team permission.")
            elif 400 == status_code:
                logging.error(
                    f"{datasource_permissions_status_dict.get(status_code)} | Response: {api_call}"
                )
                raise Exception
            elif 401 <= status_code <= 403:
                logging.error(datasource_permissions_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error(
                "There is no uid, id or datasource_team_permission object defined."
            )
            raise ValueError

    def update_datasource_basic_role_access_by_uid(
        self,
        uid: str,
        build_in_role_name: str,
        datasource_team_permission: DatasourcePermission,
        ds_type: Optional[str] = None,
    ):
        """The method includes a functionality to update the datasource permission specified by the datasource uid and the build in role name. The functionality is a Grafana ENTERPRISE feature.

        Args:
            uid (str): Specify the uid of the datasource
            build_in_role_name (str): Specify the build in role name
            datasource_team_permission (DatasourcePermission): Specify the datasource team permission
            ds_type (str): Specify the optional plugin type of the datasource (for example prometheus). It's necessary if more than one datasource in the organisation uses the same uid (default None)

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if (
            len(uid) != 0
            and len(build_in_role_name) != 0
            and datasource_team_permission.permission is not None
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCE_PERMISSIONS.value}/{uid}/builtInRoles/{build_in_role_name}{self._ds_type_query(ds_type)}",
                RequestsMethods.POST,
                json.dumps({"permission": datasource_team_permission.permission}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            datasource_permissions_status_dict: dict = {
                    400: "Permission cannot be added, see response body for details.",
                    401: "Unauthorized.",
                    403: "Access Denied.",
                }

            if status_code == 200 and api_call.get("message") == "Permission updated":
                logging.info(
                    "You successfully updated the datasource build in role name permission."
                )
            elif status_code == 200 and api_call.get("message") == "Permission removed":
                logging.info(
                    "You successfully removed the datasource build in role name permission."
                )
            elif 400 == status_code:
                logging.error(
                    f"{datasource_permissions_status_dict.get(status_code)} | Response: {api_call}"
                )
                raise Exception
            elif 401 <= status_code <= 403:
                logging.error(datasource_permissions_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error(
                "There is no uid, build_in_role_name or datasource_team_permission object defined."
            )
            raise ValueError


class DatasourceLegacyPermissions:
    """The class includes all necessary methods to access the Grafana legacy datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model

    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    @_deprecated("the UID based datasource permissions API has no equivalent")
    def enable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to enable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature.

        DEPRECATED: The UID based datasource permissions API has no equivalent for this call. The corresponding Grafana endpoint is no longer part of the current API documentation.

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if datasource_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}/enable-permissions",
                RequestsMethods.POST,
                json.dumps({}),
            )

            if api_call.get("message") != "Datasource permissions enabled":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully enabled the datasource permissions.")
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    @_deprecated("the UID based datasource permissions API has no equivalent")
    def disable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to disable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature.

        DEPRECATED: The UID based datasource permissions API has no equivalent for this call. The corresponding Grafana endpoint is no longer part of the current API documentation.

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if datasource_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}/disable-permissions",
                RequestsMethods.POST,
                json.dumps({}),
            )

            if api_call.get("message") != "Datasource permissions disabled":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully disabled the datasource permissions.")
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    @_deprecated("use DatasourcePermissions.get_datasource_permissions_by_uid instead")
    def get_datasource_permissions(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature.

        DEPRECATED: Use DatasourcePermissions.get_datasource_permissions_by_uid instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            datasource_id (int): Specify the id of the datasource

        Required Permissions:
            Action: datasources.permissions:read
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the datasource permissions

        """
        if datasource_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}/permissions",
                RequestsMethods.GET,
            )

            if api_call == {} or api_call.get("datasourceId") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    @_deprecated(f"use {_PERMISSION_UPDATE_METHODS} instead")
    def add_datasource_permissions(
        self, datasource_id: int, datasource_permission: dict
    ):
        """The method includes a functionality to add datasource permission specified by the datasource id and the datasource permission dict. The functionality is a Grafana ENTERPRISE feature.

        DEPRECATED: Use DatasourcePermissions.update_datasource_user_access_by_uid, DatasourcePermissions.update_datasource_team_access_by_uid or DatasourcePermissions.update_datasource_basic_role_access_by_uid instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            datasource_id (int): Specify the id of the datasource
            datasource_permission (dict): Specify the permission of the datasource

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if datasource_id != 0 and datasource_permission != {}:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}/permissions",
                RequestsMethods.POST,
                json.dumps(datasource_permission),
            )

            if api_call.get("message") != "Datasource permission added":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully added a datasource permission.")
        else:
            logging.error("There is no datasource_id or datasource_permission defined.")
            raise ValueError

    @_deprecated(f"use {_PERMISSION_UPDATE_METHODS} (with an empty permission) instead")
    def delete_datasource_permissions(self, datasource_id: int, permission_id: int):
        """The method includes a functionality to delete datasource permission specified by the datasource id and the permission id. The functionality is a Grafana ENTERPRISE feature.

        DEPRECATED: Use DatasourcePermissions.update_datasource_user_access_by_uid, DatasourcePermissions.update_datasource_team_access_by_uid or DatasourcePermissions.update_datasource_basic_role_access_by_uid (with an empty permission) instead. The corresponding Grafana endpoint is no longer part of the current API documentation or is marked as deprecated.

        Args:
            datasource_id (int): Specify the id of the datasource
            permission_id (id): Specify the permission id

        Required Permissions:
            Action: datasources.permissions:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None

        """
        if datasource_id != 0 and permission_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}/permissions/{permission_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Datasource permission removed":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully removed a datasource permission.")
        else:
            logging.error("There is no datasource_id or permission_id defined.")
            raise ValueError


class DatasourceQueryResourceCaching:
    """The class includes all necessary methods to access the Grafana datasource query and resource caching API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana ENTERPRISE feature.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model

    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource cache config specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache",
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def enable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to enable the datasource cache specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:read
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache/enable",
                RequestsMethods.POST,
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def disable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to disable the datasource cache specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache/disable",
                RequestsMethods.POST,
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def clean_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to clean the datasource cache of all data sources with caching enabled. The uid of the datasource will only be used to return the configuration for that data source.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache/clean",
                RequestsMethods.POST,
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def update_datasource_cache(
        self, uid: str, datasource_cache: DatasourceCache
    ) -> dict:
        """The method includes a functionality to update the datasource cache specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource
            datasource_cache (DatasourceCache): Specif the datasource cache object

        Required Permissions:
            Action: datasources.caching:write
            Scope: datasources:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if (
            len(uid) != 0
            and datasource_cache is not None
            and datasource_cache.datasource_id != 0
            and len(datasource_cache.datasource_uid) != 0
            and datasource_cache.enabled is not None
            and datasource_cache.use_default_ttl is not None
            and datasource_cache.ttl_queries_ms != 0
            and datasource_cache.ttl_resources_ms != 0
        ):
            datasource_cache_object: dict = {
                    "dataSourceID": datasource_cache.datasource_id,
                    "dataSourceUID": datasource_cache.datasource_uid,
                    "enabled": datasource_cache.enabled,
                    "useDefaultTTL": datasource_cache.use_default_ttl,
                    "ttlQueriesMs": datasource_cache.ttl_queries_ms,
                    "ttlResourcesMs": datasource_cache.ttl_resources_ms,
                }

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache",
                RequestsMethods.POST,
                json.dumps(datasource_cache_object),
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid or the right datasource_cache object defined."
            )
            raise ValueError


class DatasourceLabelBasedAccessControl:
    """The class includes all necessary methods to access the Grafana datasource label based access control for teams API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana Cloud feature. Only cloud Loki data sources are supported.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model

    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_lbac_rules_for_datasource(self, uid: str) -> list:
        """The method includes a functionality to get all datasource label based access control rules for team specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:read
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all LBAC rules

        """
        if len(uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/lbac/teams",
            )

            if api_call is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def update_lbac_rules_for_datasource(self, uid: str) -> dict:
        """The method includes a functionality to enable the datasource cache specified by the datasource uid.

        Args:
            uid (str): Specify the uid of the datasource

        Required Permissions:
            Action: datasources:write, datasources.permissions:write
            Scope: [datasources:*, datasources:uid:*, datasources:uid:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a datasource

        """
        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/lbac/teams",
                RequestsMethods.POST,
            )

            if api_call == {} or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError
