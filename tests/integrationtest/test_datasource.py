import os

from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.datasource import Datasource


class DataSourceTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    data_source: Datasource = Datasource(model)

    def test_list_all_data_sources(self):
        data_sources: list = self.data_source.get_all_datasources()

        self.assertEqual(5, data_sources[0]["id"])

    def test_get_datasource_by_id(self):
        data_source: dict = self.data_source.get_datasource_by_id(5)

        self.assertEqual("5yBH2Yxnk", data_source["uid"])

    def test_get_datasource_by_uid(self):
        data_source: dict = self.data_source.get_datasource_by_uid("5yBH2Yxnk")

        self.assertEqual(5, data_source["id"])

    def test_get_datasource_by_name(self):
        data_source: dict = self.data_source.get_datasource_by_name("TestData DB")

        self.assertEqual(5, data_source["id"])

    def test_get_datasource_id_by_name(self):
        self.assertEqual(5, self.data_source.get_datasource_id_by_name("TestData DB"))

    def test_a_create_datasource(self):
        data_source: dict = self.data_source.get_datasource_by_id(5)
        data_source["id"] = None
        data_source["uid"] = None
        data_source["name"] = "TestData DB 1"

        self.assertEqual(None, self.data_source.create_datasource(data_source))
        self.assertEqual(
            self.data_source.get_datasource_id_by_name("TestData DB 1"),
            self.data_source.get_datasource_by_name("TestData DB 1")["id"],
        )

    def test_b_update_datasource(self):
        data_source: dict = self.data_source.get_datasource_by_name("TestData DB 1")
        data_source["name"] = "TestData DB 2"

        self.assertEqual(
            None,
            self.data_source.update_datasource(
                self.data_source.get_datasource_id_by_name("TestData DB 1"), data_source
            ),
        )
        self.assertEqual(
            self.data_source.get_datasource_id_by_name("TestData DB 2"),
            self.data_source.get_datasource_by_name("TestData DB 2")["id"],
        )

    def test_c_delete_datasource_by_id(self):
        id: int = self.data_source.get_datasource_id_by_name("TestData DB 2")

        self.assertEqual(None, self.data_source.delete_datasource_by_id(id))

        with self.assertRaises(Exception):
            self.data_source.get_datasource_by_id(id)

    def test_delete_datasource_by_uid(self):
        self.test_a_create_datasource()
        data_source: dict = self.data_source.get_datasource_by_name("TestData DB 1")

        self.assertEqual(
            None, self.data_source.delete_datasource_by_uid(data_source["uid"])
        )

        with self.assertRaises(Exception):
            self.data_source.get_datasource_by_id(data_source["id"])

    def test_delete_datasource_by_name(self):
        self.test_a_create_datasource()
        data_source: dict = self.data_source.get_datasource_by_name("TestData DB 1")

        self.assertEqual(
            None, self.data_source.delete_datasource_by_name("TestData DB 1")
        )

        with self.assertRaises(Exception):
            self.data_source.get_datasource_by_id(data_source["id"])
