import json
import logging
from httpx import Response

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    GlobalUser,
)
from .api import Api


class Admin:
    """The class includes all necessary methods to access the Grafana admin API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

    HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_settings(self) -> dict:
        """The method includes a functionality to get the settings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding settings
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/settings",
        )

        if api_call == dict() or api_call.get("DEFAULT") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def update_settings(self, updates: dict = None, removals: dict = None):
        """The method includes a functionality to update the settings. Be aware that the functionality is a Grafana v8.0+ feature and you can find detailed information about the dict values here: https://grafana.com/docs/grafana/latest/developers/http_api/admin/#update-settings

        Args:
            updates (dict): Specify the updates object
            removals (dict): Specify the removals object

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if updates is not None or removals is not None:
            settings_update: dict = dict()

            if updates is not None:
                settings_update.update(dict({"updates": updates}))

            if removals is not None:
                settings_update.update(dict({"removals": removals}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/settings",
                RequestsMethods.PUT,
                json.dumps(settings_update),
            )

            if api_call.get("message") != "Settings updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully updated the corresponding settings.")
        else:
            logging.error("There is no updates or removals defined.")
            raise ValueError

    def get_stats(self) -> dict:
        """The method includes a functionality to get the admin statistics

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the corresponding statistics
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/stats",
        )

        if api_call == dict() or api_call.get("orgs") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_preview_report(self) -> dict:
        """The method includes a functionality to get a preview report

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the preview report
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/usage-report-preview",
        )

        if api_call == dict() or api_call.get("version") is None:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def create_global_user(self, user: GlobalUser) -> int:
        """The method includes a functionality to create a global user

        Args:
            user (GlobalUser): Specify the global user object

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (int): Returns the corresponding user id
        """

        if (
            user is not None
            and len(user.name) != 0
            and len(user.email) != 0
            and len(user.login) != 0
            and len(user.password) != 0
        ):
            user_object: dict = dict(
                {
                    "name": user.name,
                    "email": user.email,
                    "login": user.login,
                    "password": user.password,
                }
            )

            if user.org_id is not None:
                user_object.update(dict({"OrgId": user.org_id}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users",
                RequestsMethods.POST,
                json.dumps(user_object),
            )

            if api_call.get("message") != "User created":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return int(api_call.get("id"))
        else:
            logging.error("There is no name, email, login or password defined.")
            raise ValueError

    def update_user_password(self, id: int, password: str):
        """The method includes a functionality to update the global user password

        Args:
            id (int): Specify the user id
            password (str): Specify the user new password

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and len(password) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}/password",
                RequestsMethods.PUT,
                json.dumps(dict({"password": password})),
            )

            if api_call.get("message") != "User password updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the corresponding user password."
                )
        else:
            logging.error("There is no id or password defined.")
            raise ValueError

    def update_user_permissions(self, id: int, is_grafana_admin: bool = None):
        """The method includes a functionality to update the global user permissions

        Args:
            id (int): Specify the user id
            is_grafana_admin (bool): Specify if the user is admin or not

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and is_grafana_admin is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}/permissions",
                RequestsMethods.PUT,
                json.dumps(dict({"isGrafanaAdmin": is_grafana_admin})),
            )

            if api_call.get("message") != "User permissions updated":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the corresponding user permissions."
                )
        else:
            logging.error("There is no id or is_grafana_admin defined.")
            raise ValueError

    def delete_global_user(self, id: int):
        """The method includes a functionality to delete a global user

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "User deleted":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the corresponding user.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def pause_all_alerts(self):
        """The method includes a functionality to pause all alerts

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/pause-all-alerts",
            RequestsMethods.POST,
            json.dumps(dict({"paused": True})),
        )

        if api_call.get("state") != "Paused":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully paused all alerts.")

    def unpause_all_alerts(self):
        """The method includes a functionality to unpause all alerts

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/pause-all-alerts",
            RequestsMethods.POST,
            json.dumps(dict({"paused": False})),
        )

        if api_call.get("state") != "Unpaused":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully unpaused all alerts.")

    def get_user_auth_token(self, id: int) -> list:
        """The method includes a functionality to get the corresponding user auth token

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the corresponding user auth tokens
        """

        if id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}/auth-tokens",
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def revoke_user_auth_token(self, id: int, auth_token_id: int):
        """The method includes a functionality to get the corresponding user auth token

        Args:
            id (int): Specify the user id
            auth_token_id (int): Specify the auth token id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0 and auth_token_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}/revoke-auth-token",
                RequestsMethods.POST,
                json.dumps(dict({"authTokenId": auth_token_id})),
            )

            if api_call.get("message") != "User auth token revoked":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully revoked the corresponding user token.")
        else:
            logging.error("There is no id or auth_token_id defined.")
            raise ValueError

    def logout_user(self, id: int):
        """The method includes a functionality to log out the corresponding user

        Args:
            id (int): Specify the user id

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ADMIN.value}/users/{id}/logout",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "User auth token revoked":
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully logout the corresponding user.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def reload_dashboards_provisioning_configuration(self):
        """The method includes a functionality to reload the dashboards provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/provisioning/dashboards/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "Dashboards config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the dashboards.")

    def reload_datasources_provisioning_configuration(self):
        """The method includes a functionality to reload the datasources provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/provisioning/datasources/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "Datasources config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the datasources.")

    def reload_plugins_provisioning_configuration(self):
        """The method includes a functionality to reload the plugins provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/provisioning/plugins/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "Plugins config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the plugins.")

    def reload_notifications_provisioning_configuration(self):
        """The method includes a functionality to reload the notifications provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/provisioning/notifications/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "Notifications config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the notifications.")

    def reload_access_controls_provisioning_configuration(self):
        """The method includes a functionality to reload the access-controls provisioning configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/provisioning/access-control/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "Accesscontrol config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the accesscontrol.")

    def reload_ldap_configuration(self):
        """The method includes a functionality to reload the ldap configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/ldap/reload",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "LDAP config reloaded":
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully reloaded the config of the ldap.")

    def rotate_data_encryption_keys(self):
        """The method includes a functionality to rotate the data encryption keys

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: Response = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ADMIN.value}/encryption/rotate-data-keys",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.status_code != 204:
            logging.error(f"Please, check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully rotated the data keys.")
