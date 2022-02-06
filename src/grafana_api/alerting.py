import datetime
import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    Silence,
    AlertmanagerConfig,
    AlertmanagerReceivers,
)
from .utils import Utils


# https://editor.swagger.io/?url=https://raw.githubusercontent.com/grafana/grafana/main/pkg/services/ngalert/api/tooling/post.json
# TODO Optimize the documentation
# TODO Doc strings
# TODO Add integrationtests


class Alerting:
    """The class includes all necessary methods to access the Grafana datasource API endpoints. It's required that \
    the API token got the corresponding datasource access rights. Please check the used methods docstring for the \
    necessary access rights

    HINT: Note Grafana Enterprise API add required permissions if fine-grained access control is enabled

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alertmanager_alerts(self, recipient: str) -> list:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: list = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts",
                )
                .json()
            )

            if api_call == list() or api_call[0].get("receivers") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def create_or_update_alertmanager_alerts(self, recipient: str, alerts: list):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        alerts -> Specify the list of the Alert -> Model objects
        """

        if len(recipient) != 0 and alerts != list():
            alerts_json_list: list = list()

            for alert in alerts:
                alert_json_dict: dict = dict(
                    {
                        "startsAt": alert.starts_at,
                        "endsAt": alert.ends_at,
                        "generatorURL": alert.generator_url,
                        "labels": alert.labels,
                        "annotations": alert.annotations,
                    }
                )
                alerts_json_list.append(alert_json_dict)

            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts/groups",
                    RequestsMethods.POST,
                    json.dumps(alerts_json_list),
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Please, check the error: {api_call.get('msg')}.")
                raise Exception
            else:
                logging.info("You successfully created alerts.")
        else:
            logging.error("There is no recipient or alerts defined.")
            raise ValueError

    def get_alertmanager_group_alerts(self, recipient: str) -> list:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: list = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts",
                )
                .json()
            )

            if api_call == list() or api_call[0].get("alerts") is None:
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def delete_alertmanager_silence_by_id(self, recipient: str, silence_id: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(silence_id) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silence/{silence_id}",
                    RequestsMethods.DELETE,
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a silence.")
        else:
            logging.error("There is no recipient or silence_id defined.")
            raise ValueError

    def get_alertmanager_silence_by_id(self, recipient: str, silence_id: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(silence_id) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silence/{silence_id}",
                )
                .json()
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient or silence_id defined.")
            raise ValueError

    def get_alertmanager_silences(self, recipient: str) -> list:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: list = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silences",
                )
                .json()
            )

            if api_call == list() or api_call[0].get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def create_or_update_alertmanager_silence(
        self, recipient: str, silence: Silence
    ) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 or silence is not None:
            silence_json_dict: dict = dict(
                {
                    "comment": silence.comment,
                    "createdBy": silence.created_by,
                    "endsAt": silence.ends_at,
                    "id": silence.id,
                    "matchers": silence.matchers,
                    "startsAt": silence.starts_at,
                }
            )

            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silences",
                    RequestsMethods.POST,
                    json.dumps(silence_json_dict),
                )
                .json()
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient or silence defined.")
            raise ValueError

    def get_alertmanager_status(self, recipient: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/status",
                )
                .json()
            )

            if api_call == dict() or api_call.get("config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def delete_alertmanager_config(self, recipient: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                    RequestsMethods.DELETE,
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a alerting config.")
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def get_alertmanager_config(self, recipient: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                )
                .json()
            )

            if api_call == dict() or api_call.get("alertmanager_config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def create_or_update_alertmanager_alert_config(
        self,
        recipient: str,
        alertmanager_config: AlertmanagerConfig,
        template_files: dict = None,
    ):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and alertmanager_config is not None:
            alertmanager_configuration_json_dict: dict = dict()

            alertmanager_configuration_json_dict[
                "alertmanager_config"
            ] = alertmanager_config
            if template_files is not None:
                alertmanager_configuration_json_dict["template_files"] = template_files

            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                    RequestsMethods.POST,
                    json.dumps(alertmanager_configuration_json_dict),
                )
                .json()
            )

            if api_call == dict() or api_call.get("alertmanager_config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created an alertmanager alert config.")
        else:
            logging.error("There is no recipient or alertmanager_config defined.")
            raise ValueError

    def test_alertmanager_receivers(
        self, recipient: str, alert: dict, receivers: AlertmanagerReceivers
    ):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and alert != dict() and receivers is not None:
            alertmanager_receivers_json_dict: dict = dict()

            alertmanager_receivers_json_dict["alert"] = alert
            alertmanager_receivers_json_dict["receivers"] = receivers

            api_call: any = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/receivers/test",
                RequestsMethods.POST,
                json.dumps(alertmanager_receivers_json_dict),
            )

            status_code: int = api_call.status_code
            api_call_dict: dict = api_call.json()

            alert_manager_status_dict: dict = dict(
                {
                    200: "You successfully tested Grafana managed receivers.",
                    207: "You successfully tested Grafana managed receivers (Multi Status).",
                    400: f"Validation error. Check the error: {api_call_dict.get('msg')}.",
                    403: "Permission denied. Please, check the access rights.",
                    404: "Alert manager not found. Please, check the alert manager configuration.",
                    408: f"Failure. Check the error: {api_call.get('msg')}.",
                    409: "Alert manager not ready. Please, check the alert manager configuration.",
                }
            )

            if 200 <= status_code <= 207:
                logging.info(alert_manager_status_dict.get(status_code))
            elif 400 <= status_code <= 409:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no recipient, alert or receivers defined.")
            raise ValueError

    def get_prometheus_alerts(self, recipient: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_PROMETHEUS.value}/{recipient}/api/v1/alerts",
                )
                .json()
            )

            if api_call == dict() or api_call.get("data") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def get_prometheus_rules(self, recipient: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_PROMETHEUS.value}/{recipient}/api/v1/rules",
                )
                .json()
            )

            if api_call == dict() or api_call.get("data") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def get_ruler_rules(self, recipient: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules",
                )
                .json()
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def delete_ruler_namespace(self, recipient: str, namespace: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(namespace) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
                    RequestsMethods.DELETE,
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a ruler namespace.")
        else:
            logging.error("There is no recipient or namespace defined.")
            raise ValueError

    def get_ruler_groups_by_namespace(self, recipient: str, namespace: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(namespace) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
                )
                .json()
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient or namespace defined.")
            raise ValueError

    def create_or_update_ruler_group_by_namespace(
        self, recipient: str, namespace: str, name: str, rules: list, interval: int = 0
    ):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        rule -> RulerRule
        """

        if (
            len(recipient) != 0
            and len(namespace) != 0
            and len(name) != 0
            and rules != list()
        ):
            rules_json_list: list = list()

            for rule in rules:
                rule_json_dict: dict = dict(
                    {
                        "alert": rule.alert,
                        "annotations": rule.annotations,
                        "expr": rule.expr,
                        "for": rule.for_id,
                        "grafana_alert": rule.grafana_alert,
                        "labels": rule.labels,
                        "record": rule.record,
                    }
                )
                rules_json_list.append(rule_json_dict)

            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
                    RequestsMethods.POST,
                    json.dumps(
                        {"interval": interval, "name": name, "rules": rules_json_list}
                    ),
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created an ruler group.")
        else:
            logging.error("There is no recipient, namespace, name or rules defined.")
            raise ValueError

    def delete_ruler_group(self, recipient: str, namespace: str, group_name: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(namespace) != 0 and len(group_name) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}/{group_name}",
                    RequestsMethods.DELETE,
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a ruler group.")
        else:
            logging.error("There is no recipient, namespace or group_name defined.")
            raise ValueError

    def get_ruler_group(self, recipient: str, namespace: str, group_name: str) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(namespace) != 0 and len(group_name) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}/{group_name}",
                )
                .json()
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient, namespace or group_name defined.")
            raise ValueError

    def test_rule(self, data_query: list) -> str:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient ->
        Object -> DatasourceRuleQuery
        """

        if data_query != list():
            api_call: str = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    "/api/v1/eval",
                    RequestsMethods.POST,
                    json.dumps(
                        {"data": data_query, "now": str(datetime.datetime.now())}
                    ),
                )
                .text()
            )

            if len(api_call) == 0:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no data_query defined.")
            raise ValueError

    def test_recipient_rule(
        self, recipient: str, expr: str, condition: str, data_query: list
    ) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if (
            len(recipient) != 0
            and len(expr) != 0
            and len(condition) != 0
            and data_query != list()
        ):
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"/api/v1/rule/test/{recipient}",
                    RequestsMethods.POST,
                    json.dumps(
                        {
                            "expr": expr,
                            "grafana_condition": {
                                "condition": condition,
                                "data": data_query,
                                "now": str(datetime.datetime.now()),
                            },
                        }
                    ),
                )
                .json()
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no recipient, expr, condition or data_query defined."
            )
            raise ValueError

    def delete_ngalert_organization_configuration(self):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        api_call: dict = (
            Utils(self.grafana_api_model)
            .call_the_api(
                f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
                RequestsMethods.DELETE,
            )
            .json()
        )

        if api_call != dict() and api_call.get("msg") is not None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info(
                "You successfully deleted the ngalert organization configuration."
            )

    def get_ngalert_organization_configuration(self) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        api_call: any = Utils(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
        )

        status_code: int = api_call.status_code

        alert_manager_status_dict: dict = dict(
            {
                404: "There's no configuration available.",
                500: "Failure, an unexpected error occurred.",
            }
        )

        if status_code == 200:
            return api_call.json()
        elif 404 <= status_code <= 500:
            logging.error(alert_manager_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def create_or_update_ngalert_organization_configuration(
        self, alert_managers: list, alertmanagers_choice: str
    ):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if alert_managers != list() and len(alertmanagers_choice) != 0:
            api_call: dict = (
                Utils(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
                    RequestsMethods.POST,
                    json.dumps(
                        {
                            "alertmanagers": alert_managers,
                            "alertmanagersChoice": alertmanagers_choice,
                        }
                    ),
                )
                .json()
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully created an ngalert organization configuration."
                )
        else:
            logging.error(
                "There is no recipient, expr, condition or data_query defined."
            )
            raise ValueError

    def get_ngalert_alertmanagers_by_organization(self) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        api_call: dict = (
            Utils(self.grafana_api_model)
            .call_the_api(
                f"{APIEndpoints.ALERTS_NGALERT.value}/alertmanagers",
            )
            .json()
        )

        if api_call == dict():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call
