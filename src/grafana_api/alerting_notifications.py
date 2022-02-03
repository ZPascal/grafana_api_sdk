import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .utils import Utils


# TODO Optimize the documentation
# TODO Doc strings
# TODO Add integrationtests

class AlertingNotifications:
    """The class includes all necessary methods to access the Grafana alerting API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_notification_channels(self) -> list:
        """The method includes a functionality to create the specified dashboard"""

        api_call: list = Utils(self.grafana_api_model).call_the_api(
            APIEndpoints.ALERT_NOTIFICATIONS.value,
            RequestsMethods.GET,
        ).json()

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_all_notification_channels_lookup(self) -> list:
        """The method includes a functionality to create the specified dashboard"""

        api_call: list = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/lookup",
            RequestsMethods.GET,
        ).json()

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_notification_channel_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to create the specified dashboard"""

        if len(uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.GET,
            ).json()

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def get_notification_channel_by_id(self, id: int) -> dict:
        """The method includes a functionality to create the specified dashboard"""

        if id != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.GET,
            ).json()

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def create_notification_channel(self, notification_channel: dict) -> dict:
        """The method includes a functionality to create the specified dashboard"""

        if notification_channel != dict():
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                APIEndpoints.ALERT_NOTIFICATIONS.value,
                RequestsMethods.POST,
                json.dumps(notification_channel),
            ).json()

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no notification_channel defined."
            )
            raise ValueError

    def update_notification_channel_by_uid(self, uid: str, notification_channel: dict) -> dict:
        """The method includes a functionality to create the specified dashboard"""

        if len(uid) != 0 and notification_channel != dict():
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.PUT,
                json.dumps(notification_channel),
            ).json()

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid or notification_channel defined."
            )
            raise ValueError

    def update_notification_channel_by_id(self, id: int, notification_channel: dict) -> dict:
        """The method includes a functionality to create the specified dashboard"""

        if id != 0 and notification_channel != dict():
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.PUT,
                json.dumps(notification_channel),
            ).json()

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no id or notification_channel defined."
            )
            raise ValueError

    def delete_notification_channel_by_uid(self, uid: str):
        """The method includes a functionality to create the specified dashboard"""

        if len(uid) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.DELETE,
            ).json()

            if api_call.get("message") != "Notification deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the notification channel.")
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def delete_notification_channel_by_id(self, id: int):
        """The method includes a functionality to create the specified dashboard"""

        if id != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.DELETE,
            ).json()

            if api_call.get("message") != "Notification deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the notification channel.")
        else:
            logging.error(
                "There is no id defined."
            )
            raise ValueError

    def test_notification_channel(self, notification_channel: dict):
        """The method includes a functionality to create the specified dashboard"""

        if notification_channel != dict():
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/test",
                RequestsMethods.POST,
                json.dumps(notification_channel),
            ).json()

            if api_call.get("message") != "Test notification sent":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully tested the notification channel.")
        else:
            logging.error(
                "There is no notification_channel defined."
            )
            raise ValueError
