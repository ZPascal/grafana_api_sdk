import logging
import json
import base64

import urllib3
from urllib3 import exceptions

from .model import RequestsMethods, ERROR_MESSAGES, APIModel


class Api:
    """The class includes all necessary methods to make API calls to the Grafana API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def call_the_api(
        self,
        api_call: str,
        method: RequestsMethods = RequestsMethods.GET,
        json_complete: str = None,
        org_id_header: int = None,
        disable_provenance_header: bool = False,
        response_status_code: bool = False,
    ) -> any:
        """The method execute a defined API call against the Grafana endpoints

        Args:
            api_call (str): Specify the API call endpoint
            method (RequestsMethods): Specify the used method (default GET)
            json_complete (str): Specify the inserted JSON as string
            org_id_header (int): Specify the optional organization id as header for the corresponding API call
            disable_provenance_header (bool): Specify the optional disable provenance as header for the corresponding API call (default False)
            response_status_code (bool): Specify if the response should include the original status code (default False)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """

        api_url: str = f"{self.grafana_api_model.host}{api_call}"
        headers: dict = dict(
            {"Authorization": f"Bearer {self.grafana_api_model.token}"},
        )

        if (
            self.grafana_api_model.username is not None
            and self.grafana_api_model.password is not None
        ):
            credentials: str = base64.b64encode(
                str.encode(
                    f"{self.grafana_api_model.username}:{self.grafana_api_model.password}"
                )
            ).decode("utf-8")
            headers.update({"Authorization": f"Basic {credentials}"})

        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        if org_id_header is not None and type(org_id_header) == int:
            headers["X-Grafana-Org-Id"] = org_id_header

        if type(disable_provenance_header) == bool and disable_provenance_header:
            headers["X-Disable-Provenance"] = f"{disable_provenance_header}"

        http = urllib3.PoolManager(
            num_pools=self.grafana_api_model.num_pools,
            retries=self.grafana_api_model.retries,
            headers=headers,
            timeout=self.grafana_api_model.timeout,
            ssl_context=self.grafana_api_model.ssl_context,
        )

        try:
            if method.value == RequestsMethods.GET.value:
                return Api.__check_the_api_call_response(
                    http.request("GET", api_url),
                    response_status_code,
                )
            elif method.value == RequestsMethods.PUT.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        http.request("PUT", api_url, body=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        http.request("POST", api_url, body=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.PATCH.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        http.request("PATCH", api_url, body=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return Api.__check_the_api_call_response(
                    http.request("DELETE", api_url), response_status_code
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    @staticmethod
    def __check_the_api_call_response(
        response: any = None, response_status_code: bool = False
    ) -> any:
        """The method includes a functionality to check the output of API call method for errors

        Args:
            response (any): Specify the inserted response
            response_status_code (bool): Specify if the original status code should be attached to the result (default False)

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """

        if Api.__check_if_valid_json(response.data.decode("utf-8")):
            if (
                len(json.loads(response.data.decode("utf-8"))) != 0
                and type(json.loads(response.data.decode("utf-8"))) == dict
            ):
                if (
                    "message" in json.loads(response.data.decode("utf-8")).keys()
                    and json.loads(response.data.decode("utf-8"))["message"]
                    in ERROR_MESSAGES
                ):
                    logging.error(json.loads(response.data.decode("utf-8"))["message"])
                    raise exceptions.ConnectionError

            json_response: (dict | list) = json.loads(response.data.decode("utf-8"))

            if type(json_response) == dict and response_status_code:
                json_response.update({"status": response.status})
            elif type(json_response) == list and response_status_code:
                json_response[0].update({"status": response.status})
            return json_response
        else:
            if response_status_code:
                return dict(
                    {"status": response.status, "data": response.data.decode("utf-8")}
                )
            else:
                return response

    @staticmethod
    def __check_if_valid_json(response: any) -> bool:
        """The method includes a functionality to check if the response json is valid

        Args:
            response (any): Specify the inserted response json

        Returns:
            api_call (bool): Returns if the json is valid or not
        """

        try:
            json.loads(response)
        except (TypeError, ValueError):
            return False
        return True

    @staticmethod
    def prepare_api_string(query_string: str) -> str:
        if len(query_string) >= 1:
            return f"{query_string}&"
        else:
            return query_string
