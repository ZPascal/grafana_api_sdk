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
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

    def __init__(
        self,
        host: str = None,
        token: str = None,
        message: str = None,
        dashboard_path: str = None,
        dashboard_name: str = None,
    ):
        self.host = host
        self.token = token
        self.message = message
        self.dashboard_path = dashboard_path
        self.dashboard_name = dashboard_name
