import json
import logging
from typing import Union

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    Report,
    ReportBrandingSettings,
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

    def get_reports(self) -> list:
        """The method includes a functionality to get all reports

        Required Permissions:
            Action: reports:read
            Scope: [reports:*, reports:id:*]

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all reports
        """

        api_call: Union[list, dict] = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.REPORTING.value,
            response_status_code=True,
        )

        status_code: int = (
            api_call[0].get("status")
            if isinstance(api_call, list)
            else api_call.get("status")
        )

        reporting_status_dict: dict = dict(
            {
                401: "Authentication failed.",
                500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
            }
        )

        if status_code == 200:
            return api_call
        elif 401 <= status_code <= 500:
            logging.error(reporting_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def get_report_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a report specified by the report id

        Args:
            id (int): Specify the report id

        Required Permissions:
            Action: reports:read
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the report
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.REPORTING.value}/{id}",
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request (invalid report ID).",
                    401: "Authentication failed.",
                    403: "Forbidden (access denied to a report or a dashboard used in the report).",
                    404: "Not found (such report does not exist).",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def create_report(self, report: Report) -> int:
        """The method includes a functionality to create a report

        Args:
            report (Report): Specify the report object

        Required Permissions:
            Action: reports:create
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the report id
        """

        report_object: Union[bool, dict] = self._validate_report_object(report)

        if isinstance(report_object, dict):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.REPORTING.value,
                RequestsMethods.POST,
                json.dumps(report_object),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    403: "Forbidden (access denied to a report or a dashboard used in the report).",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Report created":
                return int(api_call.get("id"))
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no report object defined.")
            raise ValueError

    def update_report(self, id: int, report: Report):
        """The method includes a functionality to update a report

        Args:
            id (int): Specify the report id
            report (Report): Specify the report object

        Required Permissions:
            Action: reports:write
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        report_object: Union[bool, dict] = self._validate_report_object(report)

        if id != 0 and isinstance(report_object, dict):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.REPORTING.value}/{id}",
                RequestsMethods.PUT,
                json.dumps(report_object),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    401: "Authentication failed.",
                    403: "Forbidden (access denied to a report or a dashboard used in the report).",
                    404: "Not found (such report does not exist).",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Report updated":
                logging.info("You successfully updated the report.")
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no id or report object defined.")
            raise ValueError

    def delete_report(self, id: int):
        """The method includes a functionality to delete a report specified by the report id

        Args:
            id (int): Specify the report id

        Required Permissions:
            Action: reports:delete
            Scope: [reports:*, reports:id:*, reports:id:<report_id>]

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.REPORTING.value}/{id}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request (invalid report ID).",
                    401: "Authentication failed.",
                    404: "Not found (such report does not exist).",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if (
                status_code == 200
                and api_call.get("message") == "Report config was removed"
            ):
                logging.info("You successfully deleted the report.")
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def send_report(
        self, id: int, emails: str = None, use_emails_from_report: bool = None
    ):
        """The method includes a functionality to send a report to a specified email addresses

        Args:
            id (int): Specify the id of forwarded report. It is the same as in the URL when editing a report, not to be confused with the id of the dashboard.
            emails (str): Specify the comma-separated list of emails to which to send the report to. Overrides the emails from the report. Required if useEmailsFromReport is not present (default None)
            use_emails_from_report (bool): Specify if the emails inside the report should be used. Required if emails is not present (default None)

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
                f"{APIEndpoints.REPORTING.value}/email",
                RequestsMethods.POST,
                json.dumps(result),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request (invalid report ID).",
                    401: "Authentication failed.",
                    403: "Forbidden (access denied to a report or a dashboard used in the report).",
                    404: "Report not found.",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Report was sent":
                logging.info("You successfully send the report.")
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no id, emails or useEmailsFromReport defined.")
            raise ValueError

    def get_report_branding_settings(self) -> dict:
        """The method includes a functionality to get the report branding settings

        Required Permissions:
            Action: reports.settings:read
            Scope: N/A

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the report branding settings
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.REPORTING.value}/settings",
            response_status_code=True,
        )

        status_code: int = api_call.get("status")

        reporting_status_dict: dict = dict(
            {
                401: "Authentication failed.",
                500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
            }
        )

        if api_call != dict() and api_call.get("id") is not None:
            return api_call
        elif 401 <= status_code <= 500:
            logging.error(reporting_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def save_report_branding_settings(self, branding_settings: ReportBrandingSettings):
        """The method includes a functionality to save the report branding settings

        Args:
            branding_settings (ReportBrandingSettings): Specify the report branding settings object.

        Required Permissions:
            Action: reports.settings:write
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            branding_settings is not None
            and len(branding_settings.report_logo_url) != 0
            and len(branding_settings.email_logo_url) != 0
            and len(branding_settings.email_footer_mode) != 0
        ):
            report_branding_settings_object: dict = dict(
                {
                    "branding": dict(
                        {
                            "reportLogoUrl": branding_settings.report_logo_url,
                            "emailLogoUrl": branding_settings.email_logo_url,
                            "emailFooterMode": branding_settings.email_footer_mode,
                        }
                    ),
                }
            )

            if branding_settings.email_footer_mode == "sent-by":
                if (
                    len(branding_settings.email_footer_text) != 0
                    and len(branding_settings.email_footer_link) != 0
                ):
                    report_branding_settings_object.update(
                        dict(
                            {
                                "branding": dict(
                                    {
                                        "emailFooterText": branding_settings.email_footer_text,
                                        "emailFooterLink": branding_settings.email_footer_link,
                                    }
                                )
                            }
                        )
                    )
                else:
                    logging.error(
                        "There is no correct value for the branding_settings email_footer_text or email_footer_link "
                        "defined."
                    )
                    raise ValueError

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.REPORTING.value}/settings",
                RequestsMethods.POST,
                json.dumps(report_branding_settings_object),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request (invalid report ID).",
                    401: "Authentication failed.",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if (
                status_code == 200
                and api_call.get("message") == "Report settings saved"
            ):
                logging.info("You successfully saved the report branding settings.")
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no branding_settings defined.")
            raise ValueError

    def send_report_test_email(self, report: Report):
        """The method includes a functionality to send a test report email

        Args:
            report (Report): Specify the report object

        Required Permissions:
            Action: reports: send
            Scope: N/A

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        report_object: Union[bool, dict] = self._validate_report_object(report)

        if isinstance(report_object, dict):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.REPORTING.value}/test-email",
                RequestsMethods.POST,
                json.dumps(report_object),
            )

            status_code: int = api_call.get("status")

            reporting_status_dict: dict = dict(
                {
                    400: "Bad request.",
                    401: "Authentication failed.",
                    403: "Forbidden (access denied to a report or a dashboard used in the report).",
                    500: "Unexpected error or server misconfiguration. Refer to server logs for more details.",
                }
            )

            if status_code == 200 and api_call.get("message") == "Test email sent":
                logging.info("You successfully sent the test email.")
            elif 400 <= status_code <= 500:
                logging.error(reporting_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no report object defined.")
            raise ValueError

    @staticmethod
    def _validate_report_object(report: Report) -> Union[bool, dict]:
        if (
            report is not None
            and len(report.name) != 0
            and len(report.recipients) != 0
            and len(report.reply_to) != 0
            and len(report.message) != 0
            and len(report.start_date) != 0
            and len(report.end_date) != 0
            and len(report.time_zone) != 0
            and len(report.orientation) != 0
            and len(report.layout) != 0
            and report.enable_dashboard_url is not None
            and report.dashboards is not None
            and len(report.frequency) != 0
            and report.formats is not None
        ):
            report_object: dict = dict(
                {
                    "name": report.name,
                    "recipients": report.recipients,
                    "replyTo": report.reply_to,
                    "message": report.message,
                    "schedule": dict(
                        {
                            "startDate": report.start_date,
                            "endDate": report.end_date,
                            "timeZone": report.time_zone,
                            "frequency": report.frequency,
                        }
                    ),
                    "options": dict(
                        {
                            "orientation": report.orientation,
                            "layout": report.layout,
                        }
                    ),
                    "enableDashboardUrl": report.enable_dashboard_url,
                    "formats": report.formats,
                }
            )

            if report.frequency == "custom":
                if len(report.interval_frequency) != 0 and report.interval_amount != 0:
                    report_object.update(
                        dict(
                            {
                                "schedule": dict(
                                    {
                                        "intervalFrequency": report.interval_frequency,
                                        "intervalAmount": report.interval_amount,
                                    }
                                )
                            }
                        )
                    )
                else:
                    logging.error(
                        "There is no interval_frequency or interval_amount defined."
                    )
                    raise ValueError
            elif report.frequency == "hourly" or report.frequency == "daily":
                if report.workdays_only is not None:
                    report_object.update(
                        dict({"schedule": dict({"workdaysOnly": report.workdays_only})})
                    )
                else:
                    logging.error("There is no workdays_only defined.")
                    raise ValueError

            dashboard_list: list = list()
            for dashboard in report.dashboards:
                dashboard_object: dict = dict()

                if len(dashboard.dashboard_uid) != 0:
                    dashboard_object.update(
                        {"dashboard": dict({"uid": dashboard.dashboard_uid})}
                    )
                else:
                    logging.error("There is no dashboard_uid value defined.")
                    raise ValueError

                if (
                    len(dashboard.time_range_from) != 0
                    and len(dashboard.time_range_to) != 0
                ):
                    dashboard_object.update(
                        {
                            "timeRange": dict(
                                {
                                    "from": dashboard.time_range_from,
                                    "to": dashboard.time_range_to,
                                }
                            )
                        }
                    )
                else:
                    logging.error(
                        "There is no time_range_from or time_range_to value defined."
                    )
                    raise ValueError

                if dashboard.report_variables is not None:
                    if dashboard.report_variables != dict():
                        dashboard_object.update(
                            {"reportVariables": dashboard.report_variables}
                        )
                    else:
                        logging.error(
                            "There is no correct value of the report_variables defined."
                        )
                        raise ValueError

                dashboard_list.append(dashboard_object)
            report_object.update(dict({"dashboards": dashboard_list}))

            return report_object
        else:
            return False
