import json
import logging

from .api import Api
from .model import APIModel, APIEndpoints, RequestsMethods


class ServiceAccount:
    """The class includes all necessary methods to access the Grafana service account API endpoints. Be aware that the functionality inside the class only works with basic authentication (username and password) and that the authenticated user is a Grafana Admin

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def search_service_account(
        self, results_per_page: int = 1000, pages: int = 1, query: str = None
    ) -> dict:
        """The method includes a functionality to get the service accounts specified by the optional pagination functionality

        Required Permissions:
            Action: serviceaccounts:read
            Scope: global:serviceaccounts:*

        Args:
            results_per_page (int): Specify the results_per_page as integer (default 1000)
            pages (int): Specify the pages as integer (default 1)
            query (str): Specify the query (default None)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service accounts
        """

        api_request_url: str = f"{APIEndpoints.SERVICE_ACCOUNTS.value}/search?perpage={results_per_page}&page={pages}"

        if query is not None and len(query) != 0:
            api_request_url: str = f"{api_request_url}&query={query}"

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            api_request_url,
        )

        if api_call == dict() or api_call.get("totalCount") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_service_account_by_id(self, id: int) -> dict:
        """The method includes a functionality to get a service account specified by the id

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account
        """

        if id is not None and id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def create_service_account(self, name: str, role: str) -> dict:
        """The method includes a functionality to create a service account

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the created service account
        """

        if len(name) != 0 and len(role) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                APIEndpoints.SERVICE_ACCOUNTS.value,
                RequestsMethods.POST,
                json.dumps(dict({"name": name, "role": role})),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no name or role defined.")
            raise ValueError

    def update_service_account(self, id: int, name: str, role: str) -> dict:
        """The method includes a functionality to update a service account specified by the id, name and role

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account
        """

        if id is not None and id != 0 and len(name) != 0 and len(role) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}",
                RequestsMethods.PATCH,
                json.dumps(dict({"name": name, "role": role})),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id, name or role defined.")
            raise ValueError

    def delete_service_account(self, id: int):
        """The method includes a functionality to delete a service account specified by the id

        Required Permissions:
            Action: serviceaccounts:delete
            Scope: serviceaccounts:id:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id is not None and id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Service account deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the service account.")
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def get_service_account_tokens_by_id(self, id: int) -> list:
        """The method includes a functionality to get a service account tokens specified by the id

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the service account tokens
        """

        if id is not None and id != 0:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}/tokens",
            )

            if api_call != list() and api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id defined.")
            raise ValueError

    def create_service_account_token_by_id(self, id: int, name: str, role: str) -> dict:
        """The method includes a functionality to create a service account token specified by the id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            name (str): Specify the name of the service account
            role (str): Specify the role of the service account

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the service account token
        """

        if id is not None and id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}/tokens",
                RequestsMethods.POST,
                json.dumps(dict({"name": name, "role": role})),
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no id, name or role defined.")
            raise ValueError

    def delete_service_account_token_by_id(self, id: int, token_id: int):
        """The method includes a functionality to delete a service account token specified by the id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            id (int): Specify the id of the service account
            token_id (int):

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id is not None and id != 0 and token_id is not None and token_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}/tokens/{token_id}",
                RequestsMethods.DELETE,
            )

            if api_call.get("message") != "Service account token deleted":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted the service account token.")
        else:
            logging.error("There is no id or token_id defined.")
            raise ValueError

    def migrate_api_keys_to_service_accounts(self):
        """The method includes a functionality to migrate all api keys to service accounts

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SERVICE_ACCOUNTS.value}/migrate",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if (
            api_call.get("migrated") is None
            and api_call.get("message") != "API keys migrated to service accounts"
        ):
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info(
                "You successfully migrated the API keys to the service accounts."
            )

    def migrate_api_key_to_service_account(self, key_id: int):
        """The method includes a functionality to migrate an api key to a service account specified by the key id

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Args:
            key_id (int): Specify the api key id of the api key

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if key_id is not None and key_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/migrate/{key_id}",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "Service accounts migrated":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully migrated the api key to an service account."
                )
        else:
            logging.error("There is no key_id defined.")
            raise ValueError

    def get_service_account_migration_status(self) -> bool:
        """The method includes a functionality to get the corresponding api key migration status

        Required Permissions:
            Action: serviceaccounts:read
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the api key migration status
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SERVICE_ACCOUNTS.value}/migrationstatus",
        )

        if api_call == dict() or api_call.get("migrated") is None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call.get("migrated")

    def hide_the_api_keys_tab(self):
        """The method includes a functionality to hide the api keys tab inside the UI

        Required Permissions:
            Action: serviceaccounts:write
            Scope: serviceaccounts:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.SERVICE_ACCOUNTS.value}/hideApiKeys",
            RequestsMethods.POST,
            json.dumps(dict()),
        )

        if api_call.get("message") != "API keys hidden":
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info("You successfully hide the api keys tab inside the UI.")

    def revert_service_account_token_to_api_key(self, id: int, key_id: int):
        """The method includes a functionality to revert a service account and transform it to the legacy api token specified by the service account id and the key id

        Required Permissions:
            Action: serviceaccounts:delete
            Scope: serviceaccounts:id:*

        Args:
            id (int): Specify the id of the service account
            key_id (int): Specify the api key id of the api key

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if id is not None and id != 0 and key_id is not None and key_id != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.SERVICE_ACCOUNTS.value}/{id}/revert/{key_id}",
                RequestsMethods.POST,
                json.dumps(dict()),
            )

            if api_call.get("message") != "reverted service account to API key":
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully reverted the service account.")
        else:
            logging.error("There is no id or key_id defined.")
            raise ValueError
