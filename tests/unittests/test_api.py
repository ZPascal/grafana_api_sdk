from urllib3 import exceptions

from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock

from grafana_api.model import APIModel, RequestsMethods
from grafana_api.api import Api


class ApiTestCase(TestCase):
    model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
    api: Api = Api(grafana_api_model=model)

    def test_call_the_api_non_method(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=None)

    def test_call_the_api_non_valid_method(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=MagicMock())

    @patch("urllib3.PoolManager")
    def test_call_the_api_basic_auth(self, pool_mock):
        model: APIModel = APIModel(
            host="https://test.test.de", username="test", password="test"
        )
        api: Api = Api(grafana_api_model=model)

        pool_mock.return_value.request.return_value.data = b'{"status": 200}'

        self.assertEqual(
            200,
            api.call_the_api(api_call=MagicMock())["status"],
        )

    @patch("urllib3.PoolManager")
    def test_call_the_api_org_id(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"status": "success"}'

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock(), org_id_header=1)[
                "status"
            ],
        )

    @patch("urllib3.PoolManager")
    def test_call_the_api_get_valid(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"status": "success"}'

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock())["status"],
        )

    def test_call_the_api_get_not_valid(self):
        with self.assertRaises(exceptions.MaxRetryError):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("urllib3.PoolManager")
    def test_call_the_api_put_valid(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"status": "success"}'

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PUT,
                json_complete=MagicMock(),
            )["status"],
        )

    def test_call_the_api_put_not_valid(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PUT)

    @patch("urllib3.PoolManager")
    def test_call_the_api_post_valid(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"status": "success"}'

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )["status"],
        )

    def test_call_the_api_post_not_valid(self):
        with self.assertRaises(exceptions.ProtocolError):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete=MagicMock(),
            )

    def test_call_the_api_post_no_data(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("urllib3.PoolManager")
    def test_call_the_api_patch_valid(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"status": "success"}'

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete=MagicMock(),
            )["status"],
        )

    def test_call_the_api_patch_not_valid(self):
        with self.assertRaises(exceptions.ProtocolError):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete=MagicMock(),
            )

    def test_call_the_api_patch_no_data(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PATCH)

    @patch("urllib3.PoolManager")
    def test_call_the_api_delete_valid(self, pool_mock):
        pool_mock.return_value.request.return_value.data = b'{"message": "Deletion successful"}'

        self.assertEqual(
            "Deletion successful",
            self.api.call_the_api(
                api_call=MagicMock(), method=RequestsMethods.DELETE
            )["message"],
        )

    def test_call_the_api_delete_not_valid(self):
        with self.assertRaises(Exception):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_check_the_api_call_response(self):
        mock: Mock = Mock()
        mock.data = b'{"test": "test"}'

        self.assertEqual(
            dict({"test": "test"}),
            self.api._Api__check_the_api_call_response(response=mock),
        )

    def test_check_the_api_call_response_no_error_message(self):
        mock: Mock = Mock()
        mock.data = b'{"message": "test"}'

        self.assertEqual(
            dict({"message": "test"}),
            self.api._Api__check_the_api_call_response(response=mock),
        )

    def test_check_the_api_call_response_no_json_response_value(self):
        mock: Mock = Mock()
        mock.data = b"test"

        self.assertEqual(
            b"test", self.api._Api__check_the_api_call_response(response=mock).data
        )

    def test_check_the_api_call_response_exception(self):
        mock: Mock = Mock()
        mock.data = b'{"message": "invalid API key"}'

        with self.assertRaises(exceptions.ProtocolError):
            self.api._Api__check_the_api_call_response(response=mock)

    @patch("grafana_api.api.Api._Api__check_if_valid_json")
    def test__check_the_api_call_response_valid_json(self, check_if_valid_json_mock):
        check_if_valid_json_mock.return_value = True

        mock: Mock = Mock()
        mock.data = b"{}"

        self.assertEqual(
            {}, self.api._Api__check_the_api_call_response(response=mock)
        )

    def test_check_the_api_call_response_return_status_code_dict(self):
        mock: Mock = Mock()
        mock.data = b'{"test": "test"}'
        mock.status = 200

        self.assertEqual(
            dict({"status": 200, "test": "test"}),
            self.api._Api__check_the_api_call_response(response=mock, response_status_code=True),
        )

    def test_check_the_api_call_response_return_status_code_list(self):
        mock: Mock = Mock()
        mock.data = b'[{"test": "test"}, {"test": "test"}]'
        mock.status = 200

        self.assertEqual(
            list([{"status": 200, "test": "test"}, {"test": "test"}]),
            self.api._Api__check_the_api_call_response(response=mock, response_status_code=True),
        )

    def test_prepare_api_string(self):
        self.assertEqual("test&", self.api.prepare_api_string("test"))

    def test_prepare_api_string_no_real_value(self):
        self.assertEqual("", self.api.prepare_api_string(""))
