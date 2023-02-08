import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    PlaylistObject,
)
from .api import Api


class LegacyPlaylist:
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
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_id defined.")
            raise ValueError

    def get_playlist_items(self, playlist_id: int) -> list:
        """The method includes a functionality to get the playlist items specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist items
        """

        if playlist_id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}/items",
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_id defined.")
            raise ValueError

    def get_playlist_dashboards(self, playlist_id: int) -> list:
        """The method includes a functionality to get the playlist dashboards specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist dashboards
        """

        if playlist_id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}/dashboards",
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_id defined.")
            raise ValueError

    def update_playlist(self, playlist_id: int, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to update a playlist specified by the playlist object and playlist_id

         Args:
            playlist_id (int): Specify the playlist_id
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """

        if playlist_id != 0 and playlist is not None:
            items: list = list()

            for item in playlist.items:
                items.append(
                    {
                        "type": item.type,
                        "value": item.value,
                        "order": item.order,
                        "title": item.title,
                    }
                )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}",
                RequestsMethods.PUT,
                json.dumps(
                    dict(
                        {
                            "name": playlist.name,
                            "interval": playlist.interval,
                            "items": items,
                        }
                    )
                ),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_id or playlist object defined.")
            raise ValueError

    def delete_playlist(self, playlist_id: int):
        """The method includes a functionality to delete a playlist specified by the playlist_id

         Args:
            playlist_id (int): Specify the playlist_id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if playlist_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_id}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            if api_call.get("status") != 200:
                logging.error(f"Check the error: {api_call.get(api_call)}.")
                raise Exception
            else:
                logging.info("You successfully deleted the corresponding playlist.")
        else:
            logging.error("There is no playlist_id object defined.")
            raise ValueError
