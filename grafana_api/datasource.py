import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods, DatasourceCache
from .api import Api


class Datasource:
    """The class includes all necessary methods to access the Grafana datasource API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_datasources(self) -> list:
        """The method includes a functionality to get all datasources

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

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_datasource_by_id(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource id

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

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    def get_datasource_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource uid

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

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def get_datasource_by_name(self, name: str) -> dict:
        """The method includes a functionality to get the datasource specified by the datasource name

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

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no name defined.")
            raise ValueError

    def get_datasource_id_by_name(self, name: str) -> int:
        """The method includes a functionality to get the datasource id specified by the datasource name

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

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call.get("id")
        else:
            logging.error("There is no name defined.")
            raise ValueError

    def create_datasource(self, data_source: dict):
        """The method includes a functionality to create a datasource specified by the datasource as dict

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

        if data_source != dict():
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

    def update_datasource(self, datasource_id: int, data_source: dict):
        """The method includes a functionality to update a datasource specified by the datasource as dict and the datasource id

        Args:
            datasource_id (int): Specify the id of the datasource
            data_source (dict): Specify the datasource as dict

        Required Permissions:
            Action: datasources:write
            Scope: [datasources:*, datasources:id:*, datasources:id:<id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if datasource_id != 0 and data_source != dict():
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}",
                RequestsMethods.PUT,
                json.dumps(data_source),
            )

            if api_call.get("message") != "Datasource updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated a datasource.")
        else:
            logging.error("There is no datasource_id or data_source defined.")
            raise ValueError

    def delete_datasource_by_id(self, datasource_id: int):
        """The method includes a functionality to delete a datasource specified by the datasource id

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

        if datasource_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{datasource_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Data source deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a datasource.")
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    def delete_datasource_by_uid(self, uid: str):
        """The method includes a functionality to delete a datasource specified by the datasource uid

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

    def delete_datasource_by_name(self, name: str):
        """The method includes a functionality to delete a datasource specified by the datasource name

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

    def query_datasource_by_id(
        self, time: str, to: str, datasource_queries: list
    ) -> dict:
        """The method includes a functionality to execute a queries inside the datasource itself specified by the datasource id

        Args:
            from (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            to (str): Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
            datasource_queries (list): Specify a list of execution queries based on the DatasourceQuery class

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified query
        """

        if len(time) != 0 and len(to) != 0 and datasource_queries != list():
            datasource_queries_json_list: list = list()

            for datasource_query in datasource_queries:
                datasource_query_json_dict: dict = dict(
                    {
                        "refId": datasource_query.ref_id,
                        "intervalMs": datasource_query.interval_ms,
                        "maxDataPoints": datasource_query.max_data_points,
                        "datasourceId": datasource_query.datasource_id,
                        "rawSql": datasource_query.raw_sql,
                        "format": datasource_query.output_format,
                    }
                )
                datasource_queries_json_list.append(datasource_query_json_dict)

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.DATASOURCE_QUERY.value,
                RequestsMethods.POST,
                json.dumps(datasource_queries_json_list),
            )

            if api_call == dict() or api_call.get("results") == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call.get("results")
        else:
            logging.error("There is no time, to or datasource_queries defined.")
            raise ValueError

    def enable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to enable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

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

    def disable_datasource_permissions(self, datasource_id: int):
        """The method includes a functionality to disable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

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

    def get_datasource_permissions(self, datasource_id: int) -> dict:
        """The method includes a functionality to get the datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

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

            if api_call == dict() or api_call.get("datasourceId") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_id defined.")
            raise ValueError

    def add_datasource_permissions(
        self, datasource_id: int, datasource_permission: dict
    ):
        """The method includes a functionality to add datasource permission specified by the datasource id and the datasource permission dict. The functionality is a Grafana ENTERPRISE feature

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

        if datasource_id != 0 and datasource_permission != dict():
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

    def delete_datasource_permissions(self, datasource_id: int, permission_id: int):
        """The method includes a functionality to delete datasource permission specified by the datasource id and the permission id. The functionality is a Grafana ENTERPRISE feature

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
    """The class includes all necessary methods to access the Grafana datasource query and resource caching API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana ENTERPRISE feature

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to get the datasource cache config specified by the datasource uid

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

            if api_call == dict() or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def enable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to enable the datasource cache specified by the datasource uid

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

            if api_call == dict() or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def disable_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to disable the datasource cache specified by the datasource uid

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

            if api_call == dict() or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def clean_datasource_cache(self, uid: str) -> dict:
        """The method includes a functionality to clean the datasource cache of all data sources with caching enabled. The uid of the datasource will only be used to return the configuration for that data source

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

            if api_call == dict() or api_call.get("dataSourceID") is None:
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
        """The method includes a functionality to update the datasource cache specified by the datasource uid

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
            datasource_cache_object: dict = dict(
                {
                    "dataSourceID": datasource_cache.datasource_id,
                    "dataSourceUID": datasource_cache.datasource_uid,
                    "enabled": datasource_cache.enabled,
                    "useDefaultTTL": datasource_cache.use_default_ttl,
                    "ttlQueriesMs": datasource_cache.ttl_queries_ms,
                    "ttlResourcesMs": datasource_cache.ttl_resources_ms,
                }
            )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.DATASOURCES.value}/{uid}/cache",
                RequestsMethods.POST,
                json.dumps(datasource_cache_object),
            )

            if api_call == dict() or api_call.get("dataSourceID") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid or the right datasource_cache object defined."
            )
            raise ValueError
