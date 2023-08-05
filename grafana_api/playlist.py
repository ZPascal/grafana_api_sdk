import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    PlaylistObject,
)
from .api import Api


class Playlist:
    """The class includes all necessary methods to access the Grafana playlist API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_playlist(self, query: str = None, limit: int = None) -> list:
        """The method includes a functionality to get the organization playlist's specified by the optional pagination functionality

         Args:
            query (str): Specify the query to limit response to playlist having a name like this value(default None)
            limit (int): Specify the limit as integer of the response (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the organization playlist's
        """

        api_request_url: str = APIEndpoints.PLAYLISTS.value

        if query is not None:
            api_request_url: str = f"{api_request_url}?query={query}"

        if limit is not None and limit != 0:
            api_request_url: str = f"{api_request_url}?limit={limit}"

        if query is not None and (limit is not None or limit != 0):
            api_request_url: str = f"{api_request_url}?query={query}&limit={limit}"

        api_call: list = Api(self.grafana_api_model).call_the_api(
            api_request_url,
        )

        if api_call == list() or api_call[0].get("uid") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_playlist(self, playlist_uid: str) -> dict:
        """The method includes a functionality to get the playlist specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """

        if len(playlist_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_uid}",
            )

            if api_call == dict() or api_call.get("uid") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_uid defined.")
            raise ValueError

    def get_playlist_items(self, playlist_uid: str) -> list:
        """The method includes a functionality to get the playlist items specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist items
        """

        if len(playlist_uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_uid}/items",
            )

            if api_call == list() or api_call[0].get("value") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_uid defined.")
            raise ValueError

    def get_playlist_dashboards(self, playlist_uid: str) -> list:
        """The method includes a functionality to get the playlist dashboards specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist dashboards
        """

        if len(playlist_uid) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_uid}/dashboards",
            )

            if api_call == list() or api_call[0].get("title") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_uid defined.")
            raise ValueError

    def create_playlist(self, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to create a playlist specified by the playlist object

         Args:
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """

        if playlist is not None:
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
                f"{APIEndpoints.PLAYLISTS.value}",
                RequestsMethods.POST,
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

            if api_call == dict() or api_call.get("uid") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist object defined.")
            raise ValueError

    def update_playlist(self, playlist_uid: str, playlist: PlaylistObject) -> dict:
        """The method includes a functionality to update a playlist specified by the playlist object and playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid
            playlist (PlaylistObject): Specify the playlist object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding playlist
        """

        if len(playlist_uid) != 0 and playlist is not None:
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
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_uid}",
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

            if api_call == dict() or api_call.get("uid") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no playlist_uid or playlist object defined.")
            raise ValueError

    def delete_playlist(self, playlist_uid: str):
        """The method includes a functionality to delete a playlist specified by the playlist_uid

         Args:
            playlist_uid (str): Specify the playlist_uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(playlist_uid) != 0:
            api_call = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.PLAYLISTS.value}/{playlist_uid}",
                RequestsMethods.DELETE,
            )

            if api_call.status_code != 200:
                logging.error(f"Check the error: {api_call.text}.")
                raise Exception
            else:
                logging.info("You successfully deleted the corresponding playlist.")
        else:
            logging.error("There is no playlist_uid object defined.")
            raise ValueError
