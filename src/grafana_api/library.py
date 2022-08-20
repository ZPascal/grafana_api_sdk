import json
import logging

from requests import Response

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    PlaylistObject,
)
from .api import Api


class Library:
    """The class includes all necessary methods to access the Grafana legacy playlist API endpoints.  Be aware that the functionality is a Grafana <= v9 feature

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_playlist(self, playlist_id: int) -> dict:
        """The method includes a functionality to get the playlist specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """

        if playlist_id != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}",
                )
                .json()
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_id defined.")
            raise ValueError