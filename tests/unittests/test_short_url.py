from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.short_url import ShortUrl


class ShortUrlTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_create_short_url(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        short_url: ShortUrl = ShortUrl(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"url": "test"})

        self.assertEqual("test", short_url.create_short_url(path="Test").get("url"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_short_url_invalid_path(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        short_url: ShortUrl = ShortUrl(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(ValueError):
            short_url.create_short_url(path="")

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_short_url_invalid_output(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        short_url: ShortUrl = ShortUrl(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"url": None})

        with self.assertRaises(Exception):
            short_url.create_short_url(path="test")
