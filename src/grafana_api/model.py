from enum import Enum

""""""
ERROR_MESSAGES: list = ["invalid API key"]


class APIEndpoints(Enum):
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

    SEARCH = "/api/search"
    DASHBOARDS = "/api/dashboards"
    FOLDERS = "/api/folders"


class RequestsMethods(Enum):
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


class APIModel:
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    host -> Specify the host of the Grafana system
    token -> Specify the access token of the Grafana system
    """

    def __init__(
        self,
        host: str = None,
        token: str = None,
    ):
        self.host = host
        self.token = token
