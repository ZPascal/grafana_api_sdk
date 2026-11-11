import warnings
from unittest import TestCase

from grafana_api.deprecation import _deprecated


class DeprecationTestCase(TestCase):
    def test_deprecated_warns_with_qualname_and_hint(self):
        @_deprecated("use X instead")
        def old():
            return 1

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            old()

        self.assertEqual(1, len(caught))
        self.assertTrue(issubclass(caught[0].category, DeprecationWarning))
        self.assertEqual(
            f"{old.__qualname__} is deprecated, use X instead.", str(caught[0].message)
        )

    def test_deprecated_removed_flag_adds_reason(self):
        @_deprecated("use X instead", removed=True)
        def old():
            return 1

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            old()

        self.assertIn(
            "and the Grafana endpoint was removed in recent versions",
            str(caught[0].message),
        )

    def test_deprecated_keeps_name_and_return_value(self):
        @_deprecated("use X instead")
        def old(value):
            return value * 2

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(4, old(2))
        self.assertEqual("old", old.__name__)
