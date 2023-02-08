import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
)
from .api import Api


class QueryHistory:
    """The class includes all necessary methods to access the Grafana query history API endpoints. Be aware that it requires that the user is logged in and that query history feature is enabled in the config file

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def add_query_to_history(self, datasource_uid: str, queries: list) -> dict:
        """The method includes a functionality to add queries to query history

        Args:
            datasource_uid (str): Specify the datasource uid
            queries (list): Specify the queries as list from type QueryObject

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the added result of the query history
        """

        if len(datasource_uid) != 0 and len(queries) != 0:
            queries_json_list: list = list()

            for query in queries:
                query_json_dict: dict = dict(
                    {
                        "refId": query.ref_id,
                        "key": query.key,
                        "scenarioId": query.scenario_id,
                        "datasource": dict(
                            {"type": query.datasource.type, "uid": query.datasource.uid}
                        ),
                    }
                )
                queries_json_list.append(query_json_dict)

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.QUERY_HISTORY.value,
                RequestsMethods.POST,
                json.dumps(
                    dict(
                        {
                            "datasourceUid": datasource_uid,
                            "queries": queries_json_list,
                        }
                    )
                ),
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_uid or queries defined.")
            raise ValueError

    def search_query_history(
        self,
        datasource_uids: list,
        search_string: str,
        sort: str = "time-desc",
        only_starred: bool = False,
        pages: int = 1,
        results_per_page: int = 100,
    ) -> dict:
        """The method includes a functionality to search a query inside the query history

        Args:
            datasource_uids (list): Specify the datasource uid
            search_string (str): Specify the search string to filter the result
            sort (str): Specify the sorting order e.g. time-asc or time-desc (default time-desc)
            only_starred (bool): Specify if queries that are starred should be used for the search (default false)
            pages (int): Specify the pages as integer (default 1)
            results_per_page (int): Specify the results_per_page as integer (default 100)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding result of the query history
        """

        if len(datasource_uids) != 0 and len(search_string) != 0:
            datasource_uids_str: str = ""

            for i in range(0, len(datasource_uids)):
                datasource_uids_str = (
                    f"{datasource_uids_str}datasourceUid='{datasource_uids[i]}'"
                )

                if len(datasource_uids) != 1 and i != len(datasource_uids) - 1:
                    datasource_uids_str = f"{datasource_uids_str}&"

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.QUERY_HISTORY.value}?{datasource_uids_str}&searchString='{search_string}'&sort='{sort}'&onlyStarred={only_starred}&page={pages}&limit={results_per_page}",
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no datasource_uids or search_string defined.")
            raise ValueError

    def delete_query_history(self, uid: str):
        """The method includes a functionality to delete a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
             None
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.QUERY_HISTORY.value}/{uid}", RequestsMethods.DELETE
            )

            if api_call.get("message") != "Query deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the query.")
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def update_query_history(self, uid: str, comment: str) -> dict:
        """The method includes a functionality to update a query inside the query history

        Args:
            uid (str): Specify the uid of the query
            comment (str): Specify the comment of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the modified result of the query history
        """

        if len(uid) != 0 and len(comment) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.QUERY_HISTORY.value}/{uid}",
                RequestsMethods.PATCH,
                json.dumps({"comment": comment}),
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid or comment defined.")
            raise ValueError

    def star_query_history(self, uid: str) -> dict:
        """The method includes a functionality to star a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding stared query history
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.QUERY_HISTORY.value}/star/{uid}",
                RequestsMethods.POST,
                json.dumps({}),
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def unstar_query_history(self, uid: str) -> dict:
        """The method includes a functionality to unstar a query inside the query history

        Args:
            uid (str): Specify the uid of the query

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding unstared query history
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.QUERY_HISTORY.value}/star/{uid}",
                RequestsMethods.DELETE,
            )

            if api_call == dict() or api_call.get("result") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError
