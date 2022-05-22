import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    TeamObject,
)
from .api import Api


class QueryHistory:
    """The class includes all necessary methods to access the Grafana query history API endpoints. Be aware that it requires that the user is logged in and that Query history feature is enabled in config file

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def add_query_to_history(self, datasource_uid: str, queries: list) -> dict:
        """The method includes a functionality to get the organization teams specified by the optional pagination functionality

        Args:
            datasource_uid (str): Specify the datasource uid
            queries (list): Specify the queries as list from type QueryObject

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization teams
        """

        api_call: dict = (
            Api(self.grafana_api_model)
            .call_the_api(
                APIEndpoints.QUERY_HISTORY.value,
                RequestsMethods.POST,
                json.dumps(dict({"datasourceUid": datasource_uid, "queries": queries}))
            )
            .json()
        )

        if api_call == dict() or api_call.get("result") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def search_history_query(self, datasource_uid: str, queries: list) -> dict:
        """The method includes a functionality to get the organization teams specified by the optional pagination functionality

        Args:
            datasource_uid (str): Specify the datasource uid
            queries (list): Specify the queries as list from type QueryObject

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the organization teams
        """

        api_call: dict = (
            Api(self.grafana_api_model)
            .call_the_api(
                APIEndpoints.QUERY_HISTORY.value,
                RequestsMethods.POST,
                json.dumps(dict({"datasourceUid": datasource_uid, "queries": queries}))
            )
            .json()
        )

        if api_call == dict() or api_call.get("result") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call