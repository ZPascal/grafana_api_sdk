from .api import Api
from .model import APIModel, APIEndpoints


class Search:
    """The class includes all necessary methods to access the Grafana search API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search(self, search_query: str) -> list:
        """The method includes a functionality to execute a custom query

        Keyword arguments:
        search_query -> Specify the inserted query as string?
        """

        result: list = (
            Api(self.grafana_api_model)
            .call_the_api(f"{APIEndpoints.SEARCH.value}?{search_query}")
            .json()
        )
        if result == list():
            raise Exception
        else:
            return result
