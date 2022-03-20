import requests

from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from requests.exceptions import MissingSchema

from src.grafana_api.model import APIModel, RequestsMethods
from src.grafana_api.api import Api


class ApiTestCase(TestCase):
    def test_call_the_api_non_method(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(Exception):
            api.call_the_api(api_call=MagicMock(), method=None)

    def test_call_the_api_non_valid_method(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(Exception):
            api.call_the_api(api_call=MagicMock(), method=MagicMock())

    @patch("requests.get")
    def test_call_the_api_get_valid(self, get_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        get_mock.return_value = mock

        self.assertEqual(
            "success",
            api.call_the_api(api_call=MagicMock()).json()["status"],
        )

    def test_call_the_api_get_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            api.call_the_api(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("requests.put")
    def test_call_the_api_put_valid(self, put_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        put_mock.return_value = mock

        self.assertEqual(
            "success",
            api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PUT,
                json_complete=MagicMock(),
            ).json()["status"],
        )

    def test_call_the_api_put_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(Exception):
            api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PUT)

    @patch("requests.post")
    def test_call_the_api_post_valid(self, post_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"status": "success"})

        post_mock.return_value = mock

        self.assertEqual(
            "success",
            api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            ).json()["status"],
        )

    def test_call_the_api_post_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(MissingSchema):
            api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )

    def test_call_the_api_post_no_data(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(Exception):
            api.call_the_api(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("requests.delete")
    def test_call_the_api_delete_valid(self, delete_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value={"message": "Deletion successful"})

        delete_mock.return_value = mock

        self.assertEqual(
            "Deletion successful",
            api.call_the_api(
                api_call=MagicMock(), method=RequestsMethods.DELETE
            ).json()["message"],
        )

    def test_call_the_api_delete_not_valid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        with self.assertRaises(Exception):
            api.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_check_the_api_call_response(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"test": "test"}))

        self.assertEqual(
            dict({"test": "test"}),
            api._Api__check_the_api_call_response(response=mock).json(),
        )

    def test_check_the_api_call_response_no_error_message(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "test"}))

        self.assertEqual(
            dict({"message": "test"}),
            api._Api__check_the_api_call_response(response=mock).json(),
        )

    def test_check_the_api_call_response_no_json_response_value(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.text = Mock(return_value="test")

        self.assertEqual(
            "test", api._Api__check_the_api_call_response(response=mock).text()
        )

    def test_check_the_api_call_response_exception(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        api: Api = Api(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "invalid API key"}))

        with self.assertRaises(requests.exceptions.ConnectionError):
            api._Api__check_the_api_call_response(response=mock)
