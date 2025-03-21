import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class AlertingNotifications:
    """The class includes all necessary methods to access the Grafana alerting notifications API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_all_notification_channels(self) -> list:
        """The method includes a functionality to get all alerting notification channels

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all notification channels
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.ALERT_NOTIFICATIONS.value,
            RequestsMethods.GET,
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_all_notification_channels_lookup(self) -> list:
        """The method includes a functionality to lookup and get reduced information of all alerting notification channels

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all notification channels as reduced information
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/lookup",
            RequestsMethods.GET,
        )

        if api_call == list() or api_call[0].get("id") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_notification_channel_by_uid(self, uid: str) -> dict:
        """The method includes a functionality to get an alerting notification channel specified by the uid

        Args:
            uid (str): Specify the uid of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the specified notification channel
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.GET,
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def get_notification_channel_by_id(self, id: int) -> dict:
        """The method includes a functionality to get an alerting notification channel specified by the id

        Args:
            id (int): Specify the id of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the specified notification channel
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.GET,
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def create_notification_channel(self, notification_channel: dict) -> dict:
        """The method includes a functionality to create an alerting notification channel specified by the notification channel dict

        Args:
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the newly created notification channel
        """

        if notification_channel != dict():
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.ALERT_NOTIFICATIONS.value,
                RequestsMethods.POST,
                json.dumps(notification_channel),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no notification_channel defined.")
            raise ValueError

    def update_notification_channel_by_uid(
        self, uid: str, notification_channel: dict
    ) -> dict:
        """The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the uid

        Args:
            uid (str): Specify the uid of the notification channel
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated notification channel
        """

        if len(uid) != 0 and notification_channel != dict():
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.PUT,
                json.dumps(notification_channel),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no uid or notification_channel defined.")
            raise ValueError

    def update_notification_channel_by_id(
        self, id: int, notification_channel: dict
    ) -> dict:
        """The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the id

        Args:
            id (int): Specify the id of the notification channel
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the updated notification channel
        """

        if id != 0 and notification_channel != dict():
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.PUT,
                json.dumps(notification_channel),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id or notification_channel defined.")
            raise ValueError

    def delete_notification_channel_by_uid(self, uid: str):
        """The method includes a functionality to delete an alerting notification channel specified by the uid

        Args:
            uid (uid): Specify the uid of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/uid/{uid}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Notification deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the notification channel.")
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def delete_notification_channel_by_id(self, id: int):
        """The method includes a functionality to delete an alerting notification channel specified by the id

        Args:
            id (int): Specify the id of the notification channel

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/{id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Notification deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully destroyed the notification channel.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def test_notification_channel(self, notification_channel: dict):
        """The method includes a functionality to test an alerting notification channel specified by the notification_channel

        Args:
            notification_channel (dict): Specify the channel of the notification

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if notification_channel != dict():
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERT_NOTIFICATIONS.value}/test",
                RequestsMethods.POST,
                json.dumps(notification_channel),
            )

            if api_call.get("message") != "Test notification sent":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully tested the notification channel.")
        else:
            logging.error("There is no notification_channel defined.")
            raise ValueError
