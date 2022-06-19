import os
from unittest import TestCase

from src.grafana_api.model import (
    APIModel,
)
from src.grafana_api.preferences import Preferences


class PreferencesTest(TestCase):
    model: APIModel = APIModel(
        host=os.environ["GRAFANA_HOST"],
        token=os.environ["GRAFANA_TOKEN"],
    )
    preferences: Preferences = Preferences(model)

    def test_a_get_current_user_preferences(self):
        self.assertEqual(
            "dark", self.preferences.get_current_user_preferences().get("theme")
        )

    def test_b_update_current_user_preferences(self):
        self.assertEqual(
            None, self.preferences.update_current_user_preferences(theme="light")
        )

        self.assertEqual(
            "light", self.preferences.get_current_user_preferences().get("theme")
        )

        self.preferences.update_current_user_preferences(theme="dark")

    def test_c_get_current_org_preferences(self):
        self.assertEqual(
            "dark", self.preferences.get_current_org_preferences().get("theme")
        )

    def test_d_update_current_org_preferences(self):
        self.assertEqual(
            None, self.preferences.update_current_org_preferences(theme="light")
        )
        self.assertEqual(
            "light", self.preferences.get_current_org_preferences().get("theme")
        )

        self.preferences.update_current_org_preferences(theme="dark")
