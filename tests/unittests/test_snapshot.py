from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from grafana_api.model import APIModel
from grafana_api.snapshot import Snapshot


class SnapshotTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_create_new_snapshot(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(
            {"id": 1}, snapshot.create_new_snapshot(dict({"test": "test"}))
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_new_snapshot_external_support(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        self.assertEqual(
            {"id": 1},
            snapshot.create_new_snapshot(
                dict({"test": "test"}), external=True, delete_key="test", key="test"
            ),
        )

    def test_create_new_snapshot_no_dashboard_json(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        with self.assertRaises(ValueError):
            snapshot.create_new_snapshot(dict())

    def test_create_new_snapshot__external_no_delete_key(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        with self.assertRaises(ValueError):
            snapshot.create_new_snapshot(dict({"test": "test"}), external=True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_new_snapshot_no_snapshot_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            snapshot.create_new_snapshot(dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_snapshots(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"id": 1}])

        self.assertEqual(list([{"id": 1}]), snapshot.get_snapshots())

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_snapshots_no_snapshots_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = list([])

        with self.assertRaises(Exception):
            snapshot.get_snapshots()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_snapshot_by_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"dashboard": {"id": 1}})

        self.assertEqual(
            dict({"dashboard": {"id": 1}}), snapshot.get_snapshot_by_key("test")
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_snapshot_by_key_no_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": 1})

        with self.assertRaises(ValueError):
            snapshot.get_snapshot_by_key("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_snapshot_by_key_no_snapshot_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            snapshot.get_snapshot_by_key("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {
                "message": "Snapshot deleted. It might take an hour before it's cleared from any CDN caches."
            }
        )

        self.assertEqual(None, snapshot.delete_snapshot_by_key("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_key_no_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(ValueError):
            snapshot.delete_snapshot_by_key("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_key_no_deletion_possible(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            snapshot.delete_snapshot_by_key("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_delete_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {
                "message": "Snapshot deleted. It might take an hour before it's cleared from any CDN caches."
            }
        )

        self.assertEqual(None, snapshot.delete_snapshot_by_delete_key("test"))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_delete_key_no_delete_key(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(ValueError):
            snapshot.delete_snapshot_by_delete_key("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_snapshot_by_delete_key_no_deletion_possible(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        snapshot: Snapshot = Snapshot(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "test"})

        with self.assertRaises(Exception):
            snapshot.delete_snapshot_by_delete_key("test")
