import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .utils import Utils


# TODO Optimize the documentation
# TODO Doc strings
# TODO Add integrationtests

class Alerting:
    """The class includes all necessary methods to access the Grafana alerting API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alerts(
            self,
            custom_querystring: str = None,
    ) -> list:
        """The method includes a functionality to extract

        Keyword arguments:
        custom_querystring -> Specify the
        """

        api_string: str = ""

        if custom_querystring is not None and len(custom_querystring) != 0:
            api_string = f"{APIEndpoints.ALERTS.value}/{custom_querystring}"
        elif custom_querystring is None:
            api_string = f"{APIEndpoints.ALERTS.value}"

        if len(api_string) != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
                api_string,
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "Please, check the functionality. An unexpected error occurred."
            )
            raise ValueError

    def get_alerts_by_dashboard_ids(
            self,
            dashboard_ids: list,
    ) -> list:
        """The method includes a functionality to create the specified dashboard

        Keyword arguments:
        dashboard_ids -> Specify the
        """

        if dashboard_ids != list():
            dashboard_ids_string: str = "?"
            for i in range(0, len(dashboard_ids)):
                dashboard_ids_string = f"{dashboard_ids_string}dashboardId={dashboard_ids[i]}"

                if i < len(dashboard_ids) - 1:
                    dashboard_ids_string = f"{dashboard_ids_string}&"

            api_call: list = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS.value}/{dashboard_ids_string}",
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no dashboard_ids defined."
            )
            raise ValueError

    def get_alert_by_id(self, id: int) -> dict:
        """The method includes a functionality to create the specified dashboard

        Keyword arguments:
        id -> Specify the
        """

        if id != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS.value}/{id}",
                RequestsMethods.GET,
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no id defined."
            )
            raise ValueError

    def pause_alert_by_id(self, id: int, paused: bool = True):
        """The method includes a functionality to create the specified dashboard

        Keyword arguments:
        id -> Specify the
        paused -> Specify the
        """

        if id != 0:
            json_complete: dict = {
                "paused": paused,
            }

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS.value}/{id}/pause",
                RequestsMethods.POST,
                json.dumps(json_complete),
            )

            # TODO Test the API and the result message !
            if api_call.get("message") != "alert paused" and api_call.get("message") != "alert unpaused":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(api_call.get("message"))
        else:
            logging.error(
                "There is no id defined."
            )
            raise ValueError

    def get_all_notification_channels(self) -> list:
        """The method includes a functionality to create the specified dashboard"""

        api_call: list = Utils(self.grafana_api_model).call_the_api(
            APIEndpoints.ALERT_NOTIFICATIONS.value,
            RequestsMethods.GET,
        )

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
        )

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
            )

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
            )

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
            )

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
            )

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
            )

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
            )

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
            )

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
            )

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
