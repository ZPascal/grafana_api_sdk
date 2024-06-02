from unittest import TestCase
from unittest.mock import MagicMock, patch

from grafana_api.model import APIModel, Report, DashboardSchema, ReportBrandingSettings
from grafana_api.reporting import Reporting


class ReportingTestCase(TestCase):

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_reports(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"test": "test", "status": 200}])

        self.assertEqual(
            list([{"test": "test", "status": 200}]), reporting.get_reports()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_reports_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 401}])

        with self.assertRaises(Exception):
            reporting.get_reports()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_reports_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = list([{"status": 600}])

        with self.assertRaises(Exception):
            reporting.get_reports()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_by_id(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"test": "test", "status": 200})

        self.assertEqual(
            dict({"test": "test", "status": 200}), reporting.get_report_by_id(1)
        )

    def test_get_report_by_id_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.get_report_by_id(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_by_id_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 404})

        with self.assertRaises(Exception):
            reporting.get_report_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_by_id_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})

        with self.assertRaises(Exception):
            reporting.get_report_by_id(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"id": 10, "status": 200, "message": "Report created"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        self.assertEqual(10, reporting.create_report(report))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report_custom_frequency(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"id": 10, "status": 200, "message": "Report created"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "custom",
            "hours",
            2,
        )

        self.assertEqual(10, reporting.create_report(report))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report_daily_frequency(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"id": 10, "status": 200, "message": "Report created"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "daily",
            workdays_only=True,
        )

        self.assertEqual(10, reporting.create_report(report))

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report_default_report_variables(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"id": 10, "status": 200, "message": "Report created"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema("test", "test", "test")
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        self.assertEqual(10, reporting.create_report(report))

    def test_create_report_no_report(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.create_report(None)

    def test_create_report_custom_frequency_no_interval_amount(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "custom",
            "hours",
        )

        with self.assertRaises(ValueError):
            reporting.create_report(report)

    def test_create_report_daily_frequency_no_workdays_only(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "daily",
        )

        with self.assertRaises(ValueError):
            reporting.create_report(report)

    def test_create_report_dashboard_schema_no_dashboard_uid(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        dashboard_schema: DashboardSchema = DashboardSchema(
            "", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "daily",
            workdays_only=False,
        )

        with self.assertRaises(ValueError):
            reporting.create_report(report)

    def test_create_report_dashboard_schema_no_time_range_from(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "daily",
            workdays_only=False,
        )

        with self.assertRaises(ValueError):
            reporting.create_report(report)

    def test_create_report_dashboard_schema_no_correct_report_variables(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict()
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
            "daily",
            workdays_only=False,
        )

        with self.assertRaises(ValueError):
            reporting.create_report(report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 400})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.create_report(report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_create_report_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.create_report(report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_report(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Report updated"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        self.assertEqual(None, reporting.update_report(1, report))

    def test_update_report_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.update_report(0, None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_report_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 400})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.update_report(1, report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_update_report_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.update_report(1, report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_report(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Report config was removed"}
        )

        self.assertEqual(None, reporting.delete_report(1))

    def test_delete_report_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.delete_report(0)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_report_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 400})

        with self.assertRaises(Exception):
            reporting.delete_report(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_delete_report_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})

        with self.assertRaises(Exception):
            reporting.delete_report(1)

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"message": "Report was sent", "status": 200}
        )

        self.assertEqual(None, reporting.send_report(1, emails="test,test"))

    def test_send_report_no_id(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.send_report(0, emails="")

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_report_not_found(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test", "status": 404})

        with self.assertRaises(Exception):
            reporting.send_report(1, use_emails_from_report=True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"message": "Test", "status": 600})

        with self.assertRaises(Exception):
            reporting.send_report(1, use_emails_from_report=True)

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_branding_settings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 200, "id": 1})

        self.assertEqual(
            dict({"status": 200, "id": 1}), reporting.get_report_branding_settings()
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_branding_settings_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 401})

        with self.assertRaises(Exception):
            reporting.get_report_branding_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_get_report_branding_settings_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})

        with self.assertRaises(Exception):
            reporting.get_report_branding_settings()

    @patch("grafana_api.api.Api.call_the_api")
    def test_save_report_branding_settings(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Report settings saved"}
        )
        report_branding_settings: ReportBrandingSettings = ReportBrandingSettings(
            "test", "test", "none"
        )

        self.assertEqual(
            None, reporting.save_report_branding_settings(report_branding_settings)
        )

    @patch("grafana_api.api.Api.call_the_api")
    def test_save_report_branding_settings_sent_by_mode(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Report settings saved"}
        )
        report_branding_settings: ReportBrandingSettings = ReportBrandingSettings(
            "test", "test", "sent-by", "test", "test"
        )

        self.assertEqual(
            None, reporting.save_report_branding_settings(report_branding_settings)
        )

    def test_save_report_branding_settings_no_branding_settings(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.save_report_branding_settings(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_save_report_branding_settings_sent_by_no_email_footer_text(
        self, call_the_api_mock
    ):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict()
        report_branding_settings: ReportBrandingSettings = ReportBrandingSettings(
            "test", "test", "sent-by", "", "test"
        )

        with self.assertRaises(ValueError):
            reporting.save_report_branding_settings(report_branding_settings)

    @patch("grafana_api.api.Api.call_the_api")
    def test_save_report_branding_settings_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 401})
        report_branding_settings: ReportBrandingSettings = ReportBrandingSettings(
            "test", "test", "none"
        )

        with self.assertRaises(Exception):
            reporting.save_report_branding_settings(report_branding_settings)

    @patch("grafana_api.api.Api.call_the_api")
    def test_save_report_branding_settings_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})
        report_branding_settings: ReportBrandingSettings = ReportBrandingSettings(
            "test", "test", "none"
        )

        with self.assertRaises(Exception):
            reporting.save_report_branding_settings(report_branding_settings)

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_test_email(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict(
            {"status": 200, "message": "Test email sent"}
        )
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        self.assertEqual(None, reporting.send_report_test_email(report))

    def test_send_report_test_email_no_report(self):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        with self.assertRaises(ValueError):
            reporting.send_report_test_email(None)

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_test_email_not_available(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 401})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.send_report_test_email(report)

    @patch("grafana_api.api.Api.call_the_api")
    def test_send_report_test_email_error(self, call_the_api_mock):
        model: APIModel = APIModel(host=MagicMock(), token=MagicMock())
        reporting: Reporting = Reporting(grafana_api_model=model)

        call_the_api_mock.return_value = dict({"status": 600})
        dashboard_schema: DashboardSchema = DashboardSchema(
            "test", "test", "test", dict({"test": "test"})
        )
        report: Report = Report(
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            "test",
            False,
            [dashboard_schema],
        )

        with self.assertRaises(Exception):
            reporting.send_report_test_email(report)
