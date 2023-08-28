import os
import asyncio

from unittest import TestCase

from grafana_api.model import (
    APIModel,
)
from grafana_api.api import Api


class APITest(TestCase):
    https2_support: bool = True if os.environ["HTTP2"] == "True" else False
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=https2_support,
    )
    api: Api = Api(model)

    def test_get_http_client_version(self):
        http = self.api.create_the_http_api_client()
        url: str = f"{self.model.host}/api/health"

        if self.https2_support:

            async def _execute_async_http_requests():
                async with http:
                    return await http.request("GET", url)

            response = asyncio.run(_execute_async_http_requests())
            self.assertEqual("HTTP/2", response.http_version)
        else:
            response = http.request("GET", url)
            self.assertEqual("HTTP/1.1", response.http_version)
