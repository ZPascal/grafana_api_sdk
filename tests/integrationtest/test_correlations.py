import os

from unittest import TestCase

from grafana_api.model import APIModel, CorrelationObject
from grafana_api.correlations import Correlations
from grafana_api.datasource import Datasource


class CorrelationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    data_source: Datasource = Datasource(model)
    correlations: Correlations = Correlations(model)

    def test_a_create_data_source(self):
        data_source: dict = self.data_source.get_datasource_by_id(5)
        data_source["id"] = None
        data_source["uid"] = None
        data_source["name"] = "TestData DB 1"

        self.assertEqual(None, self.data_source.create_datasource(data_source))

    def test_b_correlations_lifecycle(self):
        data_source: dict = self.data_source.get_datasource_by_name("TestData DB 1")
        correlation_object: CorrelationObject = CorrelationObject(
            "5yBH2Yxnk",
            data_source["uid"],
            "Test",
            "Test correlations",
            "query",
            "message",
            dict(),
        )
        correlation_object: dict = self.correlations.create_correlations(
            correlation_object
        )
        self.assertEqual("Correlation created", correlation_object.get("message"))

        correlation_uid: str = correlation_object.get("result").get("uid")
        data_source_uid: str = correlation_object.get("result").get("sourceUID")

        self.assertEqual(
            correlation_object.get("result"),
            self.correlations.get_correlation(data_source_uid, correlation_uid),
        )
        self.assertEqual(
            [correlation_object.get("result")],
            self.correlations.get_all_correlations_by_datasource_uid(data_source_uid),
        )

        self.assertEqual(
            {
                "correlations": [correlation_object.get("result")],
                "limit": 100,
                "page": 1,
                "totalCount": 1,
            },
            self.correlations.get_all_correlations(),
        )

        self.assertEqual(
            "Correlation updated",
            self.correlations.update_correlations(
                data_source_uid, correlation_uid, "Test1", "Test1 correlations"
            ).get("message"),
        )
        self.assertEqual(
            None,
            self.correlations.delete_correlations(data_source_uid, correlation_uid),
        )

    def test_c_delete_data_source(self):
        self.assertEqual(
            None, self.data_source.delete_datasource_by_name("TestData DB 1")
        )
