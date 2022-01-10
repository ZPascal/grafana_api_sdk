from enum import Enum


class APIEndpoints(Enum):
    SEARCH = "/api/search"
    DASHBOARDS = "/api/dashboards"


class RequestsMethods(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"


class APIModel:
    def __init__(
        self,
        host: str = None,
        token: str = None,
        message: str = None,
        dashboard_path: str = None,
        dashboard_name: str = None,
    ) -> object:
        self.host = host
        self.token = token
        self.message = message
        self.dashboard_path = dashboard_path
        self.dashboard_name = dashboard_name
