import os
from unittest import TestCase

from src.grafana_api.model import APIModel
from src.grafana_api.snapshot import Snapshot
from src.grafana_api.dashboard import Dashboard


class SnapshotTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    snapshot: Snapshot = Snapshot(model)
    dashboard: Dashboard = Dashboard(model)

    def test_a_create_new_snapshot(self):
        snapshot: dict = self.snapshot.create_new_snapshot(
            self.dashboard.get_dashboard_by_uid("test1").get("dashboard"),
            name="TestSnapshot1",
        )
        self.assertIsNotNone(snapshot.get("id"))

    def test_get_snapshots(self):
        self.assertEqual(1, len(self.snapshot.get_snapshots()))

    def test_get_snapshot_by_key(self):
        snapshot_key: str = self.snapshot.get_snapshots()[0].get("key")
        self.assertIsNotNone(
            self.snapshot.get_snapshot_by_key(snapshot_key).get("dashboard").get("id")
        )

    def test_b_delete_snapshot_by_key(self):
        snapshot_key: str = self.snapshot.get_snapshots()[1].get("key")
        self.snapshot.delete_snapshot_by_key(snapshot_key)
        self.assertEqual(1, len(self.snapshot.get_snapshots()))

    def test_c_delete_snapshot_by_delete_key(self):
        snapshot: dict = self.snapshot.create_new_snapshot(
            self.dashboard.get_dashboard_by_uid("test1").get("dashboard"),
            name="TestSnapshot2",
            delete_key="test",
        )
        self.snapshot.delete_snapshot_by_delete_key("test")
        with self.assertRaises(Exception):
            self.snapshot.get_snapshot_by_key(snapshot.get("key"))
