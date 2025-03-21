import logging

from .api import Api
from .model import APIModel, APIEndpoints


class Search:
    """The class includes all necessary methods to access the Grafana search API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search(self, search_query: str) -> list:
        """The method includes a functionality to execute a custom query

        Args:
            search_query (str): Specify the inserted query as string

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of query the results
        """

        if len(search_query) != 0:
            result: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SEARCH.value}?{search_query}"
            )
            if result == list():
                raise Exception
            else:
                return result
        else:
            logging.error("There is no search_query defined.")
            raise ValueError
