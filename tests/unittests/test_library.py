from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from src.grafana_api.model import APIModel
from src.grafana_api.library import Library


class LibraryTestCase(TestCase):
    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_library_elements(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(dict({"result": "test"}), library.get_all_library_elements())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_library_elements_advanced_values(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            library.get_all_library_elements(
                search_string="test",
                types_filter="test,test",
                exclude_uid="test",
                folder_filter_ids="1,2",
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_all_library_elements_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.get_all_library_elements()

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}), library.get_library_element_by_uid("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_uid_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.get_library_element_by_uid("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_uid_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.get_library_element_by_uid("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}), library.get_library_element_by_name("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_name_no_name(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.get_library_element_by_name("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_by_name_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.get_library_element_by_name("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_connections(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}), library.get_library_element_connections("test")
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_connections_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.get_library_element_connections("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_get_library_element_connections_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.get_library_element_connections("test")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_library_element(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            library.create_library_element(1, dict({"test": "test"})),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_library_element_advanced_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            library.create_library_element(
                1, dict({"test": "test"}), folder_uid="test", name="test", uid="test"
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_library_element_no_model(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.create_library_element(1, dict())

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_create_library_element_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.create_library_element(1, dict({"test": "test"}))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_library_element(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            library.update_library_element(
                "test", 1, "test", "test", dict({"test": "test"}), 1
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_library_element_advanced_setup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"result": "test"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(
            dict({"result": "test"}),
            library.update_library_element(
                "test", 1, "test", "test", dict({"test": "test"}), 1
            ),
        )

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_library_element_no_model(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.update_library_element("test", 1, "test", "test", dict(), 1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_update_library_element_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.update_library_element(1, "test", "test", dict({"test": "test"}), 1)

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_library_element(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict({"message": "Library element deleted"}))

        call_the_api_mock.return_value = mock

        self.assertEqual(None, library.delete_library_element("test"))

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_library_element_no_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(ValueError):
            library.delete_library_element("")

    @patch("src.grafana_api.api.Api.call_the_api")
    def test_delete_library_element_error_response(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        library: Library = Library(grafana_api_model=model)

        mock: Mock = Mock()
        mock.json = Mock(return_value=dict())

        call_the_api_mock.return_value = mock

        with self.assertRaises(Exception):
            library.delete_library_element("test")
