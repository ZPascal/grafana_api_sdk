import os
from unittest import TestCase

from grafana_api.model import APIModel, CorrelationObject
from grafana_api.correlations import Correlations
from grafana_api.datasource import Datasource


class CorrelationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
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
        correlation_object: CorrelationObject = CorrelationObject("5yBH2Yxnk", data_source["uid"],
                                                                  "Test", "Test correlations",
                                                                  "query", "message", dict())
        correlations_object = self.correlations.create_correlations(correlation_object)
        self.assertEqual("Correlation created", correlations_object.get("message"))

        correlations_object_uid: str = correlations_object.get("result").get("uid")
        data_source_uid: str = correlations_object.get("result").get("sourceUID")

        self.assertEqual(
            "Correlation updated",
            self.correlations.update_correlations(
                data_source_uid, correlations_object_uid, "Test1", "Test1 correlations"
            ).get("message"),
        )
        self.assertEqual(
            None,
            self.correlations.delete_correlations(
                data_source_uid, correlations_object_uid
            ),
        )

    def test_c_delete_data_source(self):
        self.assertEqual(
            None, self.data_source.delete_datasource_by_name("TestData DB 1")
        )
