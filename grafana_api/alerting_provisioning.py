import logging

from .model import APIModel, APIEndpoints
from .api import Api

# TODO implement the new test cases


class AlertingProvisioning:
    """The class includes all necessary methods to access the Grafana alerting provisioning API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alertmanager_alerts(self, recipient: any = "grafana") -> list:
        """The method includes a functionality to get the Alertmanager alerts specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager alerts
        """

        if (type(recipient) == int and recipient != 0) or (
            type(recipient) == str and len(recipient) != 0
        ):
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/alert-rules/",
            )

            if api_call == list() or api_call[0].get("receivers") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError
