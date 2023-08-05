import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods
from .api import Api


class Preferences:
    """The class includes all necessary methods to access the Grafana preferences API endpoints.

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_current_user_preferences(
        self,
    ) -> dict:
        """The method includes a functionality to get the current user preferences

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current user preferences
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.USER_PREFERENCES.value,
        )

        if isinstance(api_call, dict) is False or api_call == dict():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def update_current_user_preferences(
        self,
        theme: str = None,
        timezone: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
    ):
        """The method includes a functionality to update the current user preferences

        Args:
            theme (str): Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
            home_dashboard_id (int): Specify the dashboard id of the home folder (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)
            timezone (str): Specify the timezone e.g. utc, browser, or an empty string for the default (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            theme is not None
            or (home_dashboard_id != 0 or home_dashboard_uid is not None)
            or timezone is not None
        ):
            modified_values: dict = dict()

            if theme is not None:
                modified_values.update(dict({"theme": theme}))

            if home_dashboard_id != 0 and isinstance(home_dashboard_id, int):
                modified_values.update(dict({"homeDashboardId": home_dashboard_id}))
            else:
                modified_values.update({"homeDashboardUID": home_dashboard_uid})

            if timezone is not None:
                modified_values.update(dict({"timezone": timezone}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.USER_PREFERENCES.value,
                RequestsMethods.PATCH,
                json.dumps(modified_values),
            )

            if api_call.get("message") != "Preferences updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the current user preferences.")
        else:
            logging.error("There is no updated value defined.")
            raise ValueError

    def get_current_org_preferences(
        self,
    ) -> dict:
        """The method includes a functionality to get the current org preferences

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the current user preferences
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            APIEndpoints.ORG_PREFERENCES.value,
        )

        if isinstance(api_call, dict) is False or api_call == dict():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def update_current_org_preferences(
        self,
        theme: str = None,
        home_dashboard_id: int = 0,
        home_dashboard_uid: str = None,
        timezone: str = None,
    ):
        """The method includes a functionality to update the current org preferences

        Args:
            theme (str): Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
            home_dashboard_id (int): Specify the dashboard id of the home folder (default 0)
            home_dashboard_uid (str): Specify the home team dashboard by uid (default None)
            timezone (str): Specify the timezone e.g. utc, browser, or an empty string for the default (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            theme is not None
            or (home_dashboard_id != 0 or home_dashboard_uid is not None)
            or timezone is not None
        ):
            modified_values: dict = dict()

            if theme is not None:
                modified_values.update(dict({"theme": theme}))

            if home_dashboard_id != 0 and isinstance(home_dashboard_id, int):
                modified_values.update(dict({"homeDashboardId": home_dashboard_id}))
            else:
                modified_values.update({"homeDashboardUID": home_dashboard_uid})

            if timezone is not None:
                modified_values.update(dict({"timezone": timezone}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.ORG_PREFERENCES.value,
                RequestsMethods.PATCH,
                json.dumps(modified_values),
            )

            if api_call.get("message") != "Preferences updated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the current org preferences.")
        else:
            logging.error("There is no updated value defined.")
            raise ValueError
