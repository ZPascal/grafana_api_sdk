from httpx import ConnectError, UnsupportedProtocol

from unittest import TestCase
from unittest.mock import AsyncMock, MagicMock, patch, Mock

from grafana_api.model import APIModel, RequestsMethods
from grafana_api.api import Api


class ApiTestCase(TestCase):
    model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
    api: Api = Api(grafana_api_model=model)

    def test_call_the_api_non_method(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=None)

    def test_call_the_api_non_valid_method(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=MagicMock())

    @patch("httpx.Client")
    def test_call_the_api_basic_auth(self, httpx_client_mock):
        model: APIModel = APIModel(
            host="https://test.test.de", username="test", password="test"
        )
        api: Api = Api(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = '{"status": 200}'

        self.assertEqual(
            200,
            api.call_the_api(api_call=MagicMock())["status"],
        )

    @patch("httpx.Client")
    def test_call_the_api_with_proxy_headers(self, httpx_client_mock):
        model: APIModel = APIModel(
            host="https://test.test.de",
            username="test",
            password="test",
            headers={"X-Custom-Header": "custom_value"},
        )
        api: Api = Api(grafana_api_model=model)

        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            api.call_the_api(api_call=MagicMock())["status"],
        )

        httpx_client_mock.assert_called()
        self.assertEqual(
            {
                "X-Custom-Header": "custom_value",
                "Authorization": "Basic dGVzdDp0ZXN0",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            httpx_client_mock.call_args[1]["headers"],
        )

    @patch("httpx.Client")
    def test_call_the_api_org_id(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock(), org_id_header=1)["status"],
        )

    @patch("httpx.Client")
    def test_call_the_api_disable_provenance(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock(), disable_provenance_header=True)[
                "status"
            ],
        )

    @patch("httpx.Client")
    def test_call_the_api_get_valid(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call=MagicMock())["status"],
        )

    def test_call_the_api_get_not_valid(self):
        with self.assertRaises(UnsupportedProtocol):
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.GET)

    @patch("httpx.Client")
    def test_call_the_api_put_valid(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PUT,
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_put_not_valid(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PUT)

    @patch("httpx.Client")
    def test_call_the_api_post_valid(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_post_not_valid(self):
        with self.assertRaises(UnsupportedProtocol):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.POST,
                json_complete='{"test": "test"}',
            )

    def test_call_the_api_post_no_data(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.POST)

    @patch("httpx.Client")
    def test_call_the_api_patch_valid(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"status": "success"}'
        )

        self.assertEqual(
            "success",
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_patch_not_valid(self):
        with self.assertRaises(UnsupportedProtocol):
            self.api.call_the_api(
                api_call=MagicMock(),
                method=RequestsMethods.PATCH,
                json_complete='{"test": "test"}',
            )

    def test_call_the_api_patch_no_data(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.PATCH)

    @patch("httpx.Client")
    def test_call_the_api_delete_valid(self, httpx_client_mock):
        httpx_client_mock.return_value.request.return_value.text = (
            '{"message": "Deletion successful"}'
        )

        self.assertEqual(
            "Deletion successful",
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)[
                "message"
            ],
        )

    def test_call_the_api_delete_not_valid(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=RequestsMethods.DELETE)

    def test_check_the_api_call_response(self):
        mock: Mock = Mock()
        mock.text = '{"test": "test"}'

        self.assertEqual(
            {"test": "test"},
            self.api._check_the_api_call_response(response=mock),
        )

    def test_check_the_api_call_response_no_error_message(self):
        mock: Mock = Mock()
        mock.text = '{"message": "test"}'

        self.assertEqual(
            {"message": "test"},
            self.api._check_the_api_call_response(response=mock),
        )

    def test_check_the_api_call_response_no_json_response_value(self):
        mock: Mock = Mock()
        mock.text = "test"

        self.assertEqual(
            "test", self.api._check_the_api_call_response(response=mock).text
        )

    def test_check_the_api_call_response_scalar_json(self):
        for text, expected in (("123", 123), ("true", True), ('"test"', "test")):
            mock: Mock = Mock()
            mock.text = text

            self.assertEqual(
                expected, self.api._check_the_api_call_response(response=mock)
            )

    def test_check_the_api_call_response_exception(self):
        mock: Mock = Mock()
        mock.text = '{"message": "invalid API key"}'

        with self.assertRaises(ConnectError):
            self.api._check_the_api_call_response(response=mock)

    @patch("grafana_api.api.Api._check_if_valid_json")
    def test_check_the_api_call_response_valid_json(self, check_if_valid_json_mock):
        check_if_valid_json_mock.return_value = True

        mock: Mock = Mock()
        mock.text = "{}"

        self.assertEqual({}, self.api._check_the_api_call_response(response=mock))

    @patch("grafana_api.api.Api._check_if_valid_json")
    def test_check_the_api_call_response_no_valid_json_status_code_result(
        self, check_if_valid_json_mock
    ):
        check_if_valid_json_mock.return_value = False

        mock: Mock = Mock()
        mock.text = ""
        mock.status_code = 200

        self.assertEqual(
            {"status": 200, "data": ""},
            self.api._check_the_api_call_response(
                response=mock, response_status_code=True
            ),
        )

    def test_check_the_api_call_response_return_status_code_dict(self):
        mock: Mock = Mock()
        mock.text = '{"test": "test"}'
        mock.status_code = 200

        self.assertEqual(
            {"status": 200, "test": "test"},
            self.api._check_the_api_call_response(
                response=mock, response_status_code=True
            ),
        )

    def test_check_the_api_call_response_return_status_code_list(self):
        mock: Mock = Mock()
        mock.text = '[{"test": "test"}, {"test": "test"}]'
        mock.status_code = 200

        self.assertEqual(
            [{"status": 200, "test": "test"}, {"test": "test"}],
            self.api._check_the_api_call_response(
                response=mock, response_status_code=True
            ),
        )

    def test_check_if_valid_json_null(self):
        self.assertEqual(False, self.api._check_if_valid_json("null"))

    def test_prepare_api_string(self):
        self.assertEqual("test&", self.api.prepare_api_string("test"))

    def test_prepare_api_string_no_real_value(self):
        self.assertEqual("", self.api.prepare_api_string(""))


class ApiHttp2TestCase(TestCase):
    model: APIModel = APIModel(
        host="https://test.com", token="test", http2_support=True
    )
    api: Api = Api(grafana_api_model=model)

    @staticmethod
    def _response(text: str) -> Mock:
        response: Mock = Mock()
        response.text = text
        return response

    def test_call_the_api_http2_no_valid_method(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(api_call=MagicMock(), method=MagicMock())

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_get(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        self.assertEqual(
            "success",
            self.api.call_the_api(api_call="/test")["status"],
        )

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_get_error(self, request_mock):
        request_mock.side_effect = ConnectError("Test")

        with self.assertRaises(ConnectError):
            self.api.call_the_api(api_call="/test")

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_put(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        self.assertEqual(
            "success",
            self.api.call_the_api(
                method=RequestsMethods.PUT,
                api_call="/test",
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_http2_put_no_json_complete(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(
                method=RequestsMethods.PUT, api_call="/test", json_complete=None
            )

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_post(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        self.assertEqual(
            "success",
            self.api.call_the_api(
                method=RequestsMethods.POST,
                api_call="/test",
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_http2_post_no_json_complete(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(
                method=RequestsMethods.POST, api_call="/test", json_complete=None
            )

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_patch(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        self.assertEqual(
            "success",
            self.api.call_the_api(
                method=RequestsMethods.PATCH,
                api_call="/test",
                json_complete='{"test": "test"}',
            )["status"],
        )

    def test_call_the_api_http2_patch_no_json_complete(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.api.call_the_api(
                method=RequestsMethods.PATCH, api_call="/test", json_complete=None
            )

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_delete(self, request_mock):
        request_mock.return_value = self._response(
            '{"message": "Deletion successful"}'
        )

        self.assertEqual(
            "Deletion successful",
            self.api.call_the_api(method=RequestsMethods.DELETE, api_call="/test")[
                "message"
            ],
        )

    @patch("httpx.Client.request")
    def test_call_the_api_post_sends_only_one_request(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        api: Api = Api(APIModel(host="https://test.com", token="test"))
        api.call_the_api(
            api_call="/test", method=RequestsMethods.POST, json_complete='{"a": 1}'
        )

        self.assertEqual(1, request_mock.call_count)

    @patch("httpx.AsyncClient.request", new_callable=AsyncMock)
    def test_call_the_api_http2_post_sends_only_one_request(self, request_mock):
        request_mock.return_value = self._response('{"status": "success"}')

        self.api.call_the_api(
            api_call="/test", method=RequestsMethods.POST, json_complete='{"a": 1}'
        )

        self.assertEqual(1, request_mock.call_count)
