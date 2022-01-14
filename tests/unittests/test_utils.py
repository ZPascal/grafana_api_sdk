import requests

from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from requests.exceptions import MissingSchema

from src.grafana_api.model import APIModel, RequestsMethods
from src.grafana_api.utils import Utils


class UtilsTestCase(TestCase):
    def test_call_the_api_non_method(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils.call_the_api(api_call=MagicMock(), method=None)

    @patch("requests.get")
    def test_call_the_api_get_valid(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        get_mock.return_value = mock

        self.assertEqual(
            "success",
            utils.call_the_api(api_call=MagicMock())["status"],
        )

    def test_call_the_api_get_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            utils.call_the_api(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("requests.post")
    def test_call_the_api_post_valid(self, post_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        post_mock.return_value = mock

        self.assertEqual(
            "success",
            utils.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )["status"],
        )

    def test_call_the_api_post_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            utils.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )

    def test_call_the_api_post_no_data(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils.call_the_api(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("requests.delete")
    def test_call_the_api_delete_valid(self, delete_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"message": "Deletion successful"})

        delete_mock.return_value = mock

        self.assertEqual(
            "Deletion successful",
            utils.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)[
                "message"
            ],
        )

    def test_call_the_api_delete_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_call_the_api_non_json_output_non_method(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils. call_the_api_non_json_output(api_call=MagicMock(), method=None)

    @patch("requests.get")
    def test_call_the_api_non_json_output_get_valid(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        get_mock.return_value.text = "success"

        self.assertEqual(
            "success",
            utils. call_the_api_non_json_output(api_call=MagicMock()).text,
        )

    def test_call_the_api_non_json_output_get_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            utils. call_the_api_non_json_output(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("requests.post")
    def test_call_the_api_non_json_output_post_valid(self, post_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        post_mock.return_value.text = "success"

        self.assertEqual(
            "success",
            utils. call_the_api_non_json_output(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            ).text,
        )

    def test_call_the_api_non_json_output_post_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            utils. call_the_api_non_json_output(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )

    def test_call_the_api_non_json_output_post_no_data(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils. call_the_api_non_json_output(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("requests.delete")
    def test_call_the_api_non_json_output_delete_valid(self, delete_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        delete_mock.return_value.text = "Deletion successful"

        self.assertEqual(
            "Deletion successful",
            utils. call_the_api_non_json_output(api_call=MagicMock(), method=RequestsMethods.DELETE).text,
        )

    def test_call_the_api_non_json_output_delete_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(Exception):
            utils. call_the_api_non_json_output(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_check_the_api_call_response(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock(), message="Test")
        utils: Utils = Utils(grafana_api_model=model)

        with self.assertRaises(requests.exceptions.ConnectionError):
            utils._Utils__check_the_api_call_response(
                response=dict({"message": "invalid API key"})
            )
