import logging
import json
import base64
from typing import Union

import httpx
from httpx import ConnectError
import asyncio

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

        if org_id_header is not None and isinstance(org_id_header, int):
            headers["X-Grafana-Org-Id"] = org_id_header

        if isinstance(disable_provenance_header, bool) and disable_provenance_header:
            headers["X-Disable-Provenance"] = f"{disable_provenance_header}"

        http: Union[httpx.Client, httpx.AsyncClient] = self.create_the_http_api_client(
            headers
        )

        if self.grafana_api_model.http2_support:

            async def _execute_async_api_call():
                async with http:
                    return await self._execute_the_async_api_call(
                        http, method, api_url, response_status_code, json_complete
                    )

            return asyncio.run(_execute_async_api_call())

        return self._execute_the_api_call(
            http, method, api_url, response_status_code, json_complete
        )

    def _execute_the_api_call(
        self,
        http: httpx.Client,
        method: RequestsMethods,
        api_url: str,
        response_status_code: bool,
        json_complete: str,
    ) -> any:
        """The method includes a functionality to execute a synchronous api call

        Args:
            http (httpx.Client): Specify the used synchronous client
            method (RequestsMethods): Specify the used method
            api_url (str): Specify the used api url
            response_status_code (bool): Specify if the response code should be returned
            json_complete (str): Specify the forwarded json in case of patch, post or put calls

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """

        try:
            if method.value == RequestsMethods.GET.value:
                return self._check_the_api_call_response(
                    http.request("GET", api_url),
                    response_status_code,
                )
            elif method.value == RequestsMethods.PUT.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        http.request("PUT", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        http.request("POST", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.PATCH.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        http.request("PATCH", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return self._check_the_api_call_response(
                    http.request("DELETE", api_url), response_status_code
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    async def _execute_the_async_api_call(
        self,
        http: httpx.AsyncClient,
        method: RequestsMethods,
        api_url: str,
        response_status_code: bool,
        json_complete: str,
    ):
        """The method includes a functionality to execute an asynchronous api call

        Args:
            http (httpx.AsyncClient): Specify the used asynchronous client
            method (RequestsMethods): Specify the used method
            api_url (str): Specify the used api url
            response_status_code (bool): Specify if the response code should be returned
            json_complete (str): Specify the forwarded json in case of patch, post or put calls

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (any): Returns the value of the api call
        """

        try:
            if method.value == RequestsMethods.GET.value:
                return self._check_the_api_call_response(
                    await http.request("GET", api_url),
                    response_status_code,
                )
            elif method.value == RequestsMethods.PUT.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        await http.request("PUT", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.POST.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        await http.request("POST", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.PATCH.value:
                if json_complete is not None:
                    return self._check_the_api_call_response(
                        await http.request("PATCH", api_url, content=json_complete),
                        response_status_code,
                    )
                else:
                    logging.error("Please define the json_complete.")
                    raise Exception
            elif method.value == RequestsMethods.DELETE.value:
                return self._check_the_api_call_response(
                    await http.request("DELETE", api_url), response_status_code
                )
            else:
                logging.error("Please define a valid method.")
                raise Exception
        except Exception as e:
            raise e

    @staticmethod
    def _check_the_api_call_response(
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

        if Api._check_if_valid_json(response.text) and response.text != "null":
            if (
                len(json.loads(response.text)) != 0
                and type(json.loads(response.text)) == dict
            ):
                if (
                    "message" in json.loads(response.text).keys()
                    and json.loads(response.text)["message"] in ERROR_MESSAGES
                ):
                    logging.error(json.loads(response.text)["message"])
                    raise ConnectError(str(json.loads(response.text)["message"]))

            json_response: Union[dict, list] = json.loads(response.text)

            if isinstance(json_response, dict) and response_status_code:
                json_response.update({"status": response.status_code})
            elif isinstance(json_response, list) and response_status_code:
                json_response[0].update({"status": response.status_code})
            return json_response
        else:
            if response_status_code:
                return dict({"status": response.status_code, "data": response.text})
            else:
                return response

    @staticmethod
    def _check_if_valid_json(response: any) -> bool:
        """The method includes a functionality to check if the response json is valid

        Args:
            response (any): Specify the inserted response json

        Returns:
            result (bool): Returns if the json is valid or not
        """

        try:
            json.loads(response)
        except (TypeError, ValueError):
            return False
        return True

    @staticmethod
    def prepare_api_string(query_string: str) -> str:
        """The method includes a functionality to prepare the api string for the queries

        Args:
            query_string (str): Specify the corresponding query string

        Returns:
            query_string (str): Returns the adjusted query string
        """

        if len(query_string) >= 1:
            return f"{query_string}&"
        else:
            return query_string

    def create_the_http_api_client(
        self, headers: dict = None
    ) -> Union[httpx.Client, httpx.AsyncClient]:
        """The method includes a functionality to create the corresponding HTTP client

        Args:
            headers (dict): Specify the optional inserted headers (Default None)

        Returns:
            client (Union[httpx.Client, httpx.AsyncClient]): Returns the corresponding client
        """

        transport: httpx.HTTPTransport = httpx.HTTPTransport(
            verify=self.grafana_api_model.ssl_context,
            retries=self.grafana_api_model.retries,
        )
        limits: httpx.Limits = httpx.Limits(
            max_connections=self.grafana_api_model.num_pools
        )
        http2: bool = self.grafana_api_model.http2_support

        if http2:
            async_transport: httpx.AsyncHTTPTransport = httpx.AsyncHTTPTransport(
                retries=self.grafana_api_model.retries, http2=http2
            )
            return httpx.AsyncClient(
                http2=True,
                limits=limits,
                timeout=self.grafana_api_model.timeout,
                headers=headers,
                transport=async_transport,
                verify=self.grafana_api_model.ssl_context,
            )
        else:
            return httpx.Client(
                limits=limits,
                timeout=self.grafana_api_model.timeout,
                headers=headers,
                transport=transport,
                verify=self.grafana_api_model.ssl_context,
            )
