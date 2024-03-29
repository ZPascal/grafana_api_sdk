from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel
from grafana_api.alerting_notifications import AlertingNotifications


class AlertingNotificationsTestCase(TestCase):
    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_notification_channels(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": 1})])

        self.assertEqual(
            list([dict({"id": 1})]), alerting.get_all_notification_channels()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_notification_channels_no_notification_channels_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_all_notification_channels()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_notification_channels_lookup(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = list([dict({"id": 1})])

        self.assertEqual(
            list([dict({"id": 1})]), alerting.get_all_notification_channels_lookup()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_all_notification_channels_lookup_no_notification_channels_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = list()

        with self.assertRaises(Exception):
            alerting.get_all_notification_channels_lookup()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_channel_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}), alerting.get_notification_channel_by_uid("test")
        )

    def test_get_notification_channel_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_notification_channel_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_channel_by_uid_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_notification_channel_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_channel_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}), alerting.get_notification_channel_by_id(1)
        )

    def test_get_notification_channel_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.get_notification_channel_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_notification_channel_by_id_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.get_notification_channel_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_notification_channel(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            alerting.create_notification_channel(dict({"test": "test"})),
        )

    def test_create_notification_channel_no_notification_channel(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.create_notification_channel(dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_notification_channel_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.create_notification_channel(dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_notification_channel_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            alerting.update_notification_channel_by_uid("test", dict({"test": "test"})),
        )

    def test_update_notification_channel_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.update_notification_channel_by_uid("", dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_notification_channel_by_uid_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.update_notification_channel_by_uid("test", dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_notification_channel_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"id": "test"})

        self.assertEqual(
            dict({"id": "test"}),
            alerting.update_notification_channel_by_id(1, dict({"test": "test"})),
        )

    def test_update_notification_channel_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.update_notification_channel_by_id(0, dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_notification_channel_by_id_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.update_notification_channel_by_id(1, dict({"test": "test"}))

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_notification_channel_by_uid(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Notification deleted"})

        self.assertEqual(None, alerting.delete_notification_channel_by_uid("test"))

    def test_delete_notification_channel_by_uid_no_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_notification_channel_by_uid("")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_notification_channel_by_uid_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.delete_notification_channel_by_uid("test")

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_notification_channel_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Notification deleted"})

        self.assertEqual(None, alerting.delete_notification_channel_by_id(1))

    def test_delete_notification_channel_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.delete_notification_channel_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_notification_channel_by_id_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.delete_notification_channel_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_notification_channel(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test notification sent"})

        self.assertEqual(
            None, alerting.test_notification_channel(dict({"test": "test"}))
        )

    def test_test_notification_channel_no_notification_channel(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        with self.assertRaises(ValueError):
            alerting.test_notification_channel(dict())

    @patch("grafana_api.api.Api.call_the_api")
    def test_test_notification_channel_no_notification_channel_available(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        alerting: AlertingNotifications = AlertingNotifications(grafana_api_model=model)

        call_the_api_mock.return_value = dict()

        with self.assertRaises(Exception):
            alerting.test_notification_channel(dict({"test": "test"}))
