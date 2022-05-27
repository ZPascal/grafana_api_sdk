import os
from unittest import TestCase

from src.grafana_api.model import (
    APIModel,
    QueryObject,
    QueryDatasourceObject,
)
from src.grafana_api.datasource import Datasource
from src.grafana_api.query_history import QueryHistory


class QueryHistoryTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    data_source: Datasource = Datasource(model)
    query_history: QueryHistory = QueryHistory(model)

    def test_search_query_history(self):
        self.assertEqual(0, self.query_history.search_query_history(list(["5yBH2Yxnk"]), "logs").get("result").get("totalCount"))

    def test_add_query_to_history(self):
        query_datasource: QueryDatasourceObject = QueryDatasourceObject("testdata", "5yBH2Yxnk")
        query: QueryObject = QueryObject("A", "test", "logs", query_datasource)

        self.query_history.add_query_to_history(
            datasource_uid="5yBH2Yxnk",
            queries=list([query])
        )

        print(self.query_history.search_query_history(list(["5yBH2Yxnk"]), "logs"))