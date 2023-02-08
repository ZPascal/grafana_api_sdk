import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
)
from .api import Api


class Reporting:
    """The class includes all necessary methods to access the Grafana reporting API endpoints. Be aware that the functionality is a Grafana ENTERPRISE v7.0+ feature

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def send_report(
        self, id: int, emails: str = None, use_emails_from_report: bool = None
    ):
        """The method includes a functionality to send a report to a specified email addresses

        Args:
            id (int): Specify the id of sented report. It is the same as in the URL when editing a report, not to be confused with the id of the dashboard.
            emails (str): Specify the comma-separated list of emails to which to send the report to. Overrides the emails from the report. Required if useEmailsFromReport is not present (default None)
            use_emails_from_report (bool): Specify the if the emails inside the report should be used. Required if emails is not present (default None)

        Required Permissions:
            Action: reports:send
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and (
            emails is not None
            and (len(emails) != 0)
            or (use_emails_from_report is not None and use_emails_from_report)
        ):
            if emails is not None and len(emails) != 0:
                result: dict = dict({"id": id, "emails": emails})
            else:
                result: dict = dict(
                    {"id": id, "useEmailsFromReport": use_emails_from_report}
                )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.REPORTING.value,
                RequestsMethods.POST,
                json.dumps(result),
                timeout=60,
            )

            if api_call.get("message") != "Report was sent":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully send the report.")
        else:
            logging.error("There is no id, emails or useEmailsFromReport defined.")
            raise ValueError
