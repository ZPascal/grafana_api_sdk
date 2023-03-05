import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class ShortUrl:
    """The class includes all necessary methods to access the Grafana short url API endpoint

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def create_short_url(self, path: str):
        """The method includes a functionality to create a short link for a specific dashboard

        Args:
            path (str): Specify the corresponding dashboard path

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the uid and the url of the newly generated link
        """

        if len(path) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.SHORT_URLS.value,
                RequestsMethods.POST,
                json.dumps(dict({"path": path})),
            )

            if api_call == dict() or api_call.get("url") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no path defined.")
            raise ValueError
