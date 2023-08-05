import os

from unittest import TestCase

from grafana_api.model import APIModel
from grafana_api.alerting_notifications import AlertingNotifications


class AlertingNotificationsTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
        http2_support=True if os.environ["HTTP2"] == "True" else False,
    )
    alerting_notifications: AlertingNotifications = AlertingNotifications(model)

    def test_get_all_notification_channels(self):
        self.alerting_notifications.delete_notification_channel_by_uid(
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-1"
            ).get("uid")
        )

        all_notification_channels: list = list(
            [
                {
                    "created": "2022-03-02T10:04:24+01:00",
                    "disableResolveMessage": False,
                    "frequency": "",
                    "id": 1,
                    "isDefault": False,
                    "name": "new alert notification",
                    "secureFields": {},
                    "sendReminder": False,
                    "settings": {"addresses": "test@test.com"},
                    "type": "email",
                    "uid": "new-alert-notification",
                    "updated": "2022-03-02T10:04:24+01:00",
                }
            ]
        )

        self.assertEqual(
            all_notification_channels,
            self.alerting_notifications.get_all_notification_channels(),
        )

    def test_get_all_notification_channels_lookup(self):
        all_notification_channels: list = list(
            [
                {
                    "id": 1,
                    "isDefault": False,
                    "name": "new alert notification",
                    "type": "email",
                    "uid": "new-alert-notification",
                }
            ]
        )

        self.assertEqual(
            all_notification_channels,
            self.alerting_notifications.get_all_notification_channels_lookup(),
        )

    def test_get_notification_channel_by_uid(self):
        notification_channel: dict = dict(
            {
                "created": "2022-03-02T10:04:24+01:00",
                "disableResolveMessage": False,
                "frequency": "",
                "id": 1,
                "isDefault": False,
                "name": "new alert notification",
                "secureFields": {},
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
                "type": "email",
                "uid": "new-alert-notification",
                "updated": "2022-03-02T10:04:24+01:00",
            }
        )

        self.assertEqual(
            notification_channel,
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification"
            ),
        )

    def test_get_notification_channel_by_id(self):
        notification_channel: dict = dict(
            {
                "created": "2022-03-02T10:04:24+01:00",
                "disableResolveMessage": False,
                "frequency": "",
                "id": 1,
                "isDefault": False,
                "name": "new alert notification",
                "secureFields": {},
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
                "type": "email",
                "uid": "new-alert-notification",
                "updated": "2022-03-02T10:04:24+01:00",
            }
        )

        self.assertEqual(
            notification_channel,
            self.alerting_notifications.get_notification_channel_by_id(1),
        )

    def test_a_create_notification_channel(self):
        notification_channel: dict = dict(
            {
                "uid": "new-alert-notification-1",
                "name": "new alert notification-1",
                "type": "email",
                "isDefault": False,
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
            }
        )

        self.alerting_notifications.create_notification_channel(notification_channel)

        self.assertEqual(
            "new-alert-notification-1",
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-1"
            ).get("uid"),
        )

    def test_b_update_notification_channel_by_uid(self):
        notification_channel: dict = dict(
            {
                "uid": "new-alert-notification-2",
                "name": "new alert notification-2",
                "type": "email",
                "isDefault": False,
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
            }
        )

        self.alerting_notifications.create_notification_channel(notification_channel)

        notification_channel_update: dict = dict(
            {
                "uid": "new-alert-notification-2",
                "name": "new-alert-notification-2.1",
                "type": "email",
                "isDefault": False,
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
            }
        )

        self.alerting_notifications.update_notification_channel_by_uid(
            "new-alert-notification-2", notification_channel_update
        )

        self.assertEqual(
            "new-alert-notification-2.1",
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-2"
            ).get("name"),
        )

    def test_c_update_notification_channel_by_id(self):
        notification_channel: dict = dict(
            {
                "uid": "new-alert-notification-3",
                "name": "new alert notification-3",
                "type": "email",
                "isDefault": False,
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
            }
        )

        self.alerting_notifications.create_notification_channel(notification_channel)

        notification_channel_update: dict = dict(
            {
                "id": self.alerting_notifications.get_notification_channel_by_uid(
                    "new-alert-notification-3"
                ).get("id"),
                "uid": "new-alert-notification-3",
                "name": "new-alert-notification-3.1",
                "type": "email",
                "isDefault": False,
                "sendReminder": False,
                "settings": {"addresses": "test@test.com"},
            }
        )
        self.alerting_notifications.update_notification_channel_by_id(
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-3"
            ).get("id"),
            notification_channel_update,
        )

        self.assertEqual(
            "new-alert-notification-3.1",
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-3"
            ).get("name"),
        )

    def test_d_delete_notification_channel_by_uid(self):
        notification_channel_uid: str = (
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-2"
            ).get("uid")
        )

        self.alerting_notifications.delete_notification_channel_by_uid(
            notification_channel_uid
        )

        with self.assertRaises(Exception):
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-2"
            )

    def test_e_delete_notification_channel_by_id(self):
        notification_channel_id: int = (
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-3"
            ).get("id")
        )

        self.alerting_notifications.delete_notification_channel_by_id(
            notification_channel_id
        )

        with self.assertRaises(Exception):
            self.alerting_notifications.get_notification_channel_by_uid(
                "new-alert-notification-3"
            )

    def test_test_notification_channel(self):
        notification_channel: dict = dict(
            {"type": "email", "settings": {"addresses": "info@theiotstudio.com"}}
        )

        self.assertEqual(
            None,
            self.alerting_notifications.test_notification_channel(notification_channel),
        )
