import os
from unittest import TestCase

from src.grafana_api.model import APIModel
from src.grafana_api.library import Library


class LibraryTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    library: Library = Library(model)

    def test_a_get_all_library_elements(self):
        self.assertEqual(
            dict(
                {"result": {"totalCount": 0, "elements": [], "page": 1, "perPage": 100}}
            ),
            self.library.get_all_library_elements(),
        )

    def test_b_create_library_element(self):
        self.library.create_library_element(72, {"test": "test"}, name="Test")

    def test_c_get_library_element_by_uid(self):
        self.assertEqual(
            "Test",
            self.library.get_library_element_by_uid(
                self.library.get_library_element_by_name("Test")
                .get("result")[0]
                .get("uid")
            )
            .get("result")
            .get("name"),
        )

    def test_d_get_library_element_by_name(self):
        self.assertEqual(
            "Test",
            self.library.get_library_element_by_name("Test")
            .get("result")[0]
            .get("name"),
        )

    def test_e_get_library_element_connections(self):
        self.assertEqual(
            dict({"result": []}),
            self.library.get_library_element_connections(
                self.library.get_library_element_by_name("Test")
                .get("result")[0]
                .get("uid")
            ),
        )

    def test_g_delete_library_element(self):
        self.library.delete_library_element(
            self.library.get_library_element_by_name("Test").get("result")[0].get("uid")
        )

        self.assertEqual(
            dict(
                {"result": {"totalCount": 0, "elements": [], "page": 1, "perPage": 100}}
            ),
            self.library.get_all_library_elements(),
        )
