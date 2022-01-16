import logging
import requests

from .model import RequestsMethods, ERROR_MESSAGES, APIModel


class Utils:
    """The class includes all necessary methods to make API calls to the Grafana API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def call_the_api(
        self,
        api_call: str,
        method: RequestsMethods = RequestsMethods.GET,
        json_complete: str = None,
    ) -> any:
        """The method execute a defined API call against the Grafana endpoints

        Keyword arguments:
        api_call -> Specify the API call endpoint
        method -> Specify the used method
        json_complete -> Specify the inserted JSON as string
        """

        api_url: str = f"{self.grafana_api_model.host}{api_call}"

        headers: dict = {
            "Authorization": f"Bearer {self.grafana_api_model.token}",
            "Content-Type": "application/json",
        }
        try:
            if method.value == RequestsMethods.GET.value:
                return Utils.__check_the_api_call_response(
                    requests.get(api_url, headers=headers).json()
                )
            elif method.value == RequestsMethods.PUT.value:
                if json_complete is not None:
                    return Utils.__check_the_api_call_response(
                        requests.put(
                            api_url, data=json_complete, headers=headers
                        ).json()
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return Utils.__check_the_api_call_response(
                        requests.post(
                            api_url, data=json_complete, headers=headers
                        ).json()
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return Utils.__check_the_api_call_response(
                    requests.delete(api_url, headers=headers).json()
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    def call_the_api_non_json_output(
        self,
        api_call: str,
        method: RequestsMethods = RequestsMethods.GET,
        json_complete: str = None,
    ) -> any:
        """The method execute a defined API call against the Grafana endpoints

        Keyword arguments:
        api_call -> Specify the API call endpoint
        method -> Specify the used method
        json_complete -> Specify the inserted JSON as string
        """

        api_url: str = f"{self.grafana_api_model.host}{api_call}"

        headers: dict = {
            "Authorization": f"Bearer {self.grafana_api_model.token}",
            "Content-Type": "application/json",
        }
        try:
            if method.value == RequestsMethods.GET.value:
                return Utils.__check_the_api_call_response(
                    requests.get(api_url, headers=headers)
                )
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return Utils.__check_the_api_call_response(
                        requests.post(api_url, data=json_complete, headers=headers)
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return Utils.__check_the_api_call_response(
                    requests.delete(api_url, headers=headers)
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    @staticmethod
    def __check_the_api_call_response(response: any = None) -> any:
        """The method includes a functionality to check the output of API call method for errors

        Keyword arguments:
        response -> Specify the inserted response
        """

        if type(response) == dict:
            if "message" in response.keys() and response["message"] in ERROR_MESSAGES:
                logging.error(response["message"])
                raise requests.exceptions.ConnectionError

        return response
