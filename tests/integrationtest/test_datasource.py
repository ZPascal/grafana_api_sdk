import os

from unittest import TestCase

from grafana_api.model import APIModel, DatasourceQuery
from grafana_api.datasource import Datasource

class DataSourceTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    data_source: Datasource = Datasource(model)

    def _get_datasource_by_name(self, name: str) -> dict:
        """Resolve a datasource by its name without using the deprecated name endpoints."""
        for data_source in self.data_source.get_all_datasources():
            if data_source["name"] == name:
                return self.data_source.get_datasource_by_uid(data_source["uid"])

        self.fail(f"The datasource {name} doesn't exist.")

    def test_list_all_data_sources(self):
        data_sources: list = self.data_source.get_all_datasources()

        self.assertEqual(5, data_sources[0]["id"])

    def test_get_datasource_by_uid(self):
        data_source: dict = self.data_source.get_datasource_by_uid("5yBH2Yxnk")

        self.assertEqual(5, data_source["id"])

    def test_get_datasource_health_by_uid(self):
        health: dict = self.data_source.get_datasource_health_by_uid("5yBH2Yxnk")

        self.assertEqual("OK", health["status"])

    def test_get_datasource_health_by_uid_unknown_uid(self):
        with self.assertRaises(Exception):  # noqa: B017
            self.data_source.get_datasource_health_by_uid("does-not-exist")

    def test_get_datasource_resource_by_uid(self):
        scenarios: list = self.data_source.get_datasource_resource_by_uid(
            "5yBH2Yxnk", "scenarios"
        )

        self.assertIsInstance(scenarios, list)
        self.assertNotEqual([], scenarios)

    def test_query_datasource_by_uid(self):
        results: dict = self.data_source.query_datasource_by_uid(
            "now-5m", "now", [DatasourceQuery("", datasource_uid="5yBH2Yxnk")]
        )

        self.assertIn("A", results)

    def test_get_datasource_by_name(self):
        with self.assertWarns(DeprecationWarning):
            data_source: dict = self.data_source.get_datasource_by_name("TestData DB")

        self.assertEqual(5, data_source["id"])

    def test_get_datasource_id_by_name(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                5, self.data_source.get_datasource_id_by_name("TestData DB")
            )

    def test_a_create_datasource(self):
        data_source: dict = self.data_source.get_datasource_by_uid("5yBH2Yxnk")
        data_source["id"] = None
        data_source["uid"] = None
        data_source["name"] = "TestData DB 1"

        self.assertEqual(None, self.data_source.create_datasource(data_source))

        uid: str = self._get_datasource_by_name("TestData DB 1")["uid"]
        self.assertEqual(
            "TestData DB 1", self.data_source.get_datasource_by_uid(uid)["name"]
        )

    def test_b_update_datasource(self):
        data_source: dict = self._get_datasource_by_name("TestData DB 1")
        uid: str = data_source["uid"]
        data_source["name"] = "TestData DB 2"

        self.assertEqual(
            None,
            self.data_source.update_datasource(data_source, datasource_uid=uid),
        )
        self.assertEqual(
            "TestData DB 2", self.data_source.get_datasource_by_uid(uid)["name"]
        )

    def test_c_delete_datasource_by_uid(self):
        uid: str = self._get_datasource_by_name("TestData DB 2")["uid"]

        self.assertEqual(None, self.data_source.delete_datasource_by_uid(uid))

        with self.assertRaises(Exception):  # noqa: B017
            self.data_source.get_datasource_by_uid(uid)

    def test_delete_datasource_by_uid(self):
        self.test_a_create_datasource()
        uid: str = self._get_datasource_by_name("TestData DB 1")["uid"]

        self.assertEqual(None, self.data_source.delete_datasource_by_uid(uid))

        with self.assertRaises(Exception):  # noqa: B017
            self.data_source.get_datasource_by_uid(uid)

    def test_delete_datasource_by_name(self):
        self.test_a_create_datasource()
        uid: str = self._get_datasource_by_name("TestData DB 1")["uid"]

        with self.assertWarns(DeprecationWarning):
            self.assertEqual(
                None, self.data_source.delete_datasource_by_name("TestData DB 1")
            )

        with self.assertRaises(Exception):  # noqa: B017
            self.data_source.get_datasource_by_uid(uid)
