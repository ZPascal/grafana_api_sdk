import logging
import json

import requests

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
        timeout: float = None,
        org_id_header: int = None,
    ) -> any:
        """The method execute a defined API call against the Grafana endpoints

        Args:
            api_call (str): Specify the API call endpoint
            method (RequestsMethods): Specify the used method (default GET)
            json_complete (str): Specify the inserted JSON as string
            timeout (float): Specify the timeout for the corresponding API call
            org_id_header (int): Specify the optional organization id for the corresponding API call

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
            url: str = (
                f"{self.grafana_api_model.username}:{self.grafana_api_model.password}@"
            )
            api_url = api_url.replace("https://", f"https://{url}")
            api_url = api_url.replace("http://", f"http://{url}")
            headers: dict = dict()

        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        if org_id_header is not None and type(org_id_header) == int:
            headers["X-Grafana-Org-Id"] = org_id_header

        try:
            if method.value == RequestsMethods.GET.value:
                return Api.__check_the_api_call_response(
                    requests.get(api_url, headers=headers, timeout=timeout)
                )
            elif method.value == RequestsMethods.PUT.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        requests.put(
                            api_url,
                            data=json_complete,
                            headers=headers,
                            timeout=timeout,
                        )
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        requests.post(
                            api_url,
                            data=json_complete,
                            headers=headers,
                            timeout=timeout,
                        )
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.PATCH.value:
                if json_complete is not None:
                    return Api.__check_the_api_call_response(
                        requests.patch(
                            api_url,
                            data=json_complete,
                            headers=headers,
                            timeout=timeout,
                        )
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return Api.__check_the_api_call_response(
                    requests.delete(api_url, headers=headers, timeout=timeout)
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    @staticmethod
    def __check_the_api_call_response(response: any = None) -> any:
        """The method includes a functionality to check the output of API call method for errors

        Args:
            response (any): Specify the inserted response

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """

        if Api.__check_if_valid_json(response.text):
            if len(response.text) != 0 and type(response.json()) == dict:
                if (
                    "message" in response.json().keys()
                    and response.json()["message"] in ERROR_MESSAGES
                ):
                    logging.error(response.json()["message"])
                    raise requests.exceptions.ConnectionError

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
        except ValueError:
            return False
        return True

    @staticmethod
    def prepare_api_string(query_string: str) -> str:
        if len(query_string) >= 1:
            return f"{query_string}&"
        else:
            return query_string
