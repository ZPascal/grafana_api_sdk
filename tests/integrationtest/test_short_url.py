import os
from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.short_url import ShortUrl


class ShortUrlTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    short_url: ShortUrl = ShortUrl(model)

    def test_create_short_url(self):
        self.assertIsNotNone(
            self.short_url.create_short_url("d/test1/test-1?orgId=4&from=now-1h&to=now")
        )
