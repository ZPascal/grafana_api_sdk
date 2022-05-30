import requests

from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from requests.exceptions import MissingSchema

from src.grafana_api.model import APIModel, RequestsMethods
from src.grafana_api.api import Api


class ApiTestCase(TestCase):
    model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
    api: Api = Api(grafana_api_model=model)

    def test_call_the_api_non_method(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=None)

    def test_call_the_api_non_valid_method(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=MagicMock())

    @patch("requests.get")
    def test_call_the_api_basic_auth(self, get_mock):
        model: APIModel = APIModel(
            host="https://test.test.de", username="test", password="test"
        )
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})
        mock.text = str('{"status": "success"}')

        get_mock.return_value = mock

        self.assertEqual(
            "success",
            api.call_the_api(api_call=MagicMock()).json()["status"],
        )

    @patch("requests.get")
    def test_call_the_api_get_valid(self, get_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})
        mock.text = str('{"status": "success"}')

        get_mock.return_value = mock

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock()).json()["status"],
        )

    def test_call_the_api_get_not_valid(self):
        with self.assertRaises(MissingSchema):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("requests.put")
    def test_call_the_api_put_valid(self, put_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})
        mock.text = str('{"status": "success"}')

        put_mock.return_value = mock

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PUT,
                json_complete=MagicMock(),
            ).json()["status"],
        )

    def test_call_the_api_put_not_valid(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PUT)

    @patch("requests.post")
    def test_call_the_api_post_valid(self, post_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})
        mock.text = str('{"status": "success"}')

        post_mock.return_value = mock

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            ).json()["status"],
        )

    def test_call_the_api_post_not_valid(self):
        with self.assertRaises(MissingSchema):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )

    def test_call_the_api_post_no_data(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("requests.patch")
    def test_call_the_api_patch_valid(self, post_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})
        mock.text = str('{"status": "success"}')

        post_mock.return_value = mock

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete=MagicMock(),
            ).json()["status"],
        )

    def test_call_the_api_patch_not_valid(self):
        with self.assertRaises(MissingSchema):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete=MagicMock(),
            )

    def test_call_the_api_patch_no_data(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PATCH)

    @patch("requests.delete")
    def test_call_the_api_delete_valid(self, delete_mock):
        mock: Mock = Mock()
        mock.json = Mock(return_value={"message": "Deletion successful"})
        mock.text = str('{"message": "Deletion successful"}')

        delete_mock.return_value = mock

        self.assertEqual(
            "Deletion successful",
            self.api.call_the_api(
                api_call=MagicMock(), method=RequestsMethods.DELETE
            ).json()["message"],
        )

    def test_call_the_api_delete_not_valid(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_check_the_api_call_response(self):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))
        mock.text = str('{"test": "test"}')

        self.assertEqual(
            dict({"test": "test"}),
            self.api._Api__check_the_api_call_response(response=mock).json(),
        )

    def test_check_the_api_call_response_no_error_message(self):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "test"}))
        mock.text = str('{"message": "test"}')

        self.assertEqual(
            dict({"message": "test"}),
            self.api._Api__check_the_api_call_response(response=mock).json(),
        )

    def test_check_the_api_call_response_no_json_response_value(self):
        mock: Mock = Mock()
        mock.text = "test"

        self.assertEqual(
            "test", self.api._Api__check_the_api_call_response(response=mock).text
        )

    def test_check_the_api_call_response_exception(self):
        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "invalid API key"}))
        mock.text = str('{"message": "invalid API key"}')

        with self.assertRaises(requests.exceptions.ConnectionError):
            self.api._Api__check_the_api_call_response(response=mock)

    @patch("src.grafana_api.api.Api._Api__check_if_valid_json")
    def test__check_the_api_call_response_valid_json(self, check_if_valid_json_mock):
        check_if_valid_json_mock.return_value = True

        mock: Mock = Mock()
        mock.json = Mock(return_value=str(""))
        mock.text = str("")

        self.assertEqual(
            "", self.api._Api__check_the_api_call_response(response=mock).text
        )
