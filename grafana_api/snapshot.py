import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
)
from .api import Api


class Snapshot:
    """The class includes all necessary methods to access the Grafana snapshot API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def create_new_snapshot(
        self,
        dashboard_json: dict,
        name: str = None,
        expires: int = None,
        external: bool = False,
        key: str = None,
        delete_key: str = None,
    ) -> dict:
        """The method includes a functionality to create the specified dashboard snapshot

        Args:
            dashboard_json (dict): Specify the dashboard_json of the dashboard
            name (str): Specify the optional name of the dashboard snapshot
            expires (int): Specify the optional expiry time as seconds of the dashboard snapshot. 3600 is 1 hour, 86400 is 1 day (default never expired)
            external (bool): Specify the optional external server rather than locally (default False)
            key (str): Specify the optional unique key. Required if external is true.
            delete_key (str): Specify the optional unique key used to delete the snapshot. It is different from the key so that only the creator can delete the snapshot. Required if external is true.

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the snapshot information of the dashboard
        """

        if dashboard_json != dict():
            if external:
                if (key is None or len(key) == 0) and (
                    delete_key is None or len(delete_key) == 0
                ):
                    logging.error(
                        "It's necessary that you define the key and the delete_key, if you use the external snapshot "
                        "opportunity. "
                    )
                    raise ValueError

            snapshot_json: dict = {
                "dashboard": dashboard_json,
                "name": name,
                "expires": expires,
                "external": external,
                "key": key,
                "deleteKey": delete_key,
            }

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.SNAPSHOTS.value,
                RequestsMethods.POST,
                json.dumps(snapshot_json),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no dashboard_json defined.")
            raise ValueError

    def get_snapshots(self) -> list:
        """The method includes a functionality to list all dashboard snapshots

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all dashboard snapshots
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.DASHBOARD_SNAPSHOTS.value,
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_snapshot_by_key(self, key: str) -> dict:
        """The method includes a functionality to get a specific dashboard snapshot by the key

        Args:
            key (str): Specify the key of the dashboard snapshot

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns a specific dashboard snapshot
        """

        if len(key) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SNAPSHOTS.value}/{key}",
            )

            if api_call == dict() or api_call.get("dashboard").get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no key defined.")
            raise ValueError

    def delete_snapshot_by_key(self, key: str):
        """The method includes a functionality to delete a specific dashboard snapshot by the key

        Args:
            key (str): Specify the key of the dashboard snapshot

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(key) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SNAPSHOTS.value}/{key}", RequestsMethods.DELETE
            )

            if (
                api_call.get("message")
                != "Snapshot deleted. It might take an hour before it's cleared from any CDN caches."
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the dashboard snapshot.")
        else:
            logging.error("There is no key defined.")
            raise ValueError

    def delete_snapshot_by_delete_key(self, delete_key: str):
        """The method includes a functionality to delete a specific dashboard snapshot by the delete_key

        Args:
            delete_key (str): Specify the delete_key of the dashboard snapshot

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(delete_key) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SNAPSHOTS.value}-delete/{delete_key}",
            )

            if (
                api_call.get("message")
                != "Snapshot deleted. It might take an hour before it's cleared from any CDN caches."
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the dashboard snapshot.")
        else:
            logging.error("There is no delete_key defined.")
            raise ValueError
