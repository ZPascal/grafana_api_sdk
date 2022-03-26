import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Organisation:
    """The class includes all necessary methods to access the Grafana organisation API endpoint

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model


# https://grafana.com/docs/grafana/latest/http_api/org/
