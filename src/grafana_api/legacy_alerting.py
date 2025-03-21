import json
import logging
import re

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Alerting:
    """The class includes all necessary methods to access the Grafana legacy alerting API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alerts(
        self,
        custom_querystring: str = None,
    ) -> list:
        """The method includes a functionality to get the legacy alerts

        Args:
            custom_querystring (str): Specify the custom querystring (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of all alerts
        """

        api_string: str = ""

        if custom_querystring is not None and len(custom_querystring) != 0:
            api_string = f"{APIEndpoints.LEGACY_ALERTS.value}/{custom_querystring}"
        elif custom_querystring is None:
            api_string = APIEndpoints.LEGACY_ALERTS.value

        if len(api_string) != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
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
        """The method includes a functionality to get legacy alerts specified by the dashboard ids

        Args:
            dashboard_ids (list): Specify the list of dashboard ids

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns a list of alerts
        """

        if dashboard_ids != list():
            dashboard_ids_string: str = "?"
            for i in range(0, len(dashboard_ids)):
                dashboard_ids_string = (
                    f"{dashboard_ids_string}dashboardId={dashboard_ids[i]}"
                )

                if i < len(dashboard_ids) - 1:
                    dashboard_ids_string = f"{dashboard_ids_string}&"

            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LEGACY_ALERTS.value}/{dashboard_ids_string}",
                RequestsMethods.GET,
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no dashboard_ids defined.")
            raise ValueError

    def get_alert_by_id(self, id: int) -> dict:
        """The method includes a functionality to get the legacy alert specified by the alert id

        Args:
            id (int): Specify the id of the legacy alert

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns an alert
        """

        def _to_camel_case(input_value: str) -> str:
            content = re.findall("[A-Z][^A-Z]*", input_value)
            if content != list():
                if len(content) != 1:
                    return content[0].lower() + "".join(content[1:])
                else:
                    return content[0].lower()
            return input_value

        if id != 0:
            api_call_raw: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LEGACY_ALERTS.value}/{id}",
                RequestsMethods.GET,
            )
            api_call: dict = {_to_camel_case(k): v for k, v in api_call_raw.items()}

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def pause_alert_by_id(self, id: int, paused: bool = True):
        """The method includes a functionality to pause/ unpause a legacy alert specified by the alert id

        Args:
            id (int): Specify the id of the legacy alert
            paused (bool): Specify the pause/ unpause parameter (default True)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            json_complete: dict = {
                "paused": paused,
            }

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.LEGACY_ALERTS.value}/{id}/pause",
                RequestsMethods.POST,
                json.dumps(json_complete),
            )

            if api_call.get(
                "message"
            ) != "alert paused" or "alert unpause" in api_call.get("message"):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(api_call.get("message"))
        else:
            logging.error("There is no id defined.")
            raise ValueError
