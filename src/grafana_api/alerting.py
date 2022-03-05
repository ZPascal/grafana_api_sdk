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
from .api import Api


# TODO Add integrationtests


class Alerting:
    """The class includes all necessary methods to access the Grafana alerting API endpoints

    Keyword arguments:
    grafana_api_model -> Inject a Grafana API model object that includes all necessary values and information
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alertmanager_alerts(self, recipient: str = "grafana") -> list:
        """The method includes a functionality to get the alertmanager alerts specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: list = (
                Api(self.grafana_api_model)
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

    def create_or_update_alertmanager_alerts(
        self, alerts: list, recipient: str = "grafana"
    ):
        """The method includes a functionality to create or update the alertmanager alerts specified by the recipient \
        and the alerts list

        Keyword arguments:
        alerts -> Specify a list of the alert objects
        recipient -> Specify the recipient of the alerts (default grafana)
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
                Api(self.grafana_api_model)
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

    def get_alertmanager_group_alerts(self, recipient: str = "grafana") -> list:
        """The method includes a functionality to get the alertmanager group alerts specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: list = (
                Api(self.grafana_api_model)
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

    def delete_alertmanager_silence_by_id(
        self, silence_id: str, recipient: str = "grafana"
    ):
        """The method includes a functionality to delete the alertmanager silence specified by the silence id and the \
        recipient

        Keyword arguments:
        silence_id -> Specify the silence id of the alerts
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(silence_id) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_alertmanager_silence_by_id(
        self, silence_id: str, recipient: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get the alertmanager silence specified by the silence id and the \
        recipient

        Keyword arguments:
        silence_id -> Specify the silence id of the alerts
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(silence_id) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_alertmanager_silences(self, recipient: str = "grafana") -> list:
        """The method includes a functionality to get all alertmanager silences specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: list = (
                Api(self.grafana_api_model)
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
        self, silence: Silence, recipient: str = "grafana"
    ) -> dict:
        """The method includes a functionality to create or update the alertmanager silence specified by the silence \
        object and the recipient

        Keyword arguments:
        silence -> Specify the silence object
        recipient -> Specify the recipient of the alerts (default grafana)
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
                Api(self.grafana_api_model)
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

    def get_alertmanager_status(self, recipient: str = "grafana") -> dict:
        """The method includes a functionality to get the alertmanager status specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def delete_alertmanager_config(self, recipient: str = "grafana"):
        """The method includes a functionality to delete the alertmanager config specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_alertmanager_config(self, recipient: str = "grafana") -> dict:
        """The method includes a functionality to get the alertmanager config specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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
        alertmanager_config: AlertmanagerConfig,
        recipient: str = "grafana",
        template_files: dict = None,
    ):
        """The method includes a functionality to create or update the alertmanager alert config specified by the \
        alertmanager config object, recipient and template_files

        Keyword arguments:
        alertmanager_config -> Specify the alertmanager config object
        recipient -> Specify the recipient of the alerts (default grafana)
        template_files -> Specify the optional template files (default None)
        """

        if len(recipient) != 0 and alertmanager_config is not None:
            alertmanager_configuration_json_dict: dict = dict()

            alertmanager_configuration_json_dict[
                "alertmanager_config"
            ] = alertmanager_config
            if template_files is not None:
                alertmanager_configuration_json_dict["template_files"] = template_files

            api_call: dict = (
                Api(self.grafana_api_model)
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
        self, alert: dict, receivers: AlertmanagerReceivers, recipient: str = "grafana"
    ):
        """The method includes a functionality to test the alertmanager receivers specified by the \
        alert dict, receivers object and the recipient

        Keyword arguments:
        alert -> Specify the alert dict
        receivers -> Specify the receivers object
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and alert != dict() and receivers is not None:
            alertmanager_receivers_json_dict: dict = dict()

            alertmanager_receivers_json_dict["alert"] = alert
            alertmanager_receivers_json_dict["receivers"] = receivers

            api_call: any = Api(self.grafana_api_model).call_the_api(
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

    def get_prometheus_alerts(self, recipient: str = "grafana") -> dict:
        """The method includes a functionality to get all prometheus alerts specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_prometheus_rules(self, recipient: str = "grafana") -> dict:
        """The method includes a functionality to get all prometheus rules specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_ruler_rules(self, recipient: str = "grafana") -> dict:
        """The method includes a functionality to get all ruler rules specified by the recipient

        Keyword arguments:
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def delete_ruler_namespace(self, namespace: str, recipient: str = "grafana"):
        """The method includes a functionality to delete a ruler namespace specified by the namespace name and \
        the recipient

        Keyword arguments:
        namespace -> Specify the namespace name
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(namespace) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_ruler_groups_by_namespace(
        self, namespace: str, recipient: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get all ruler groups specified by the namespace name and \
        the recipient

        Keyword arguments:
        namespace -> Specify the namespace name
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(namespace) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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
        self,
        namespace: str,
        group_name: str,
        rules: list,
        recipient: str = "grafana",
        interval: int = 0,
    ):
        """The method includes a functionality to create or update a ruler group specified by the namespace name, \
        a ruler group name, a ruler rule object list, the recipient and an interval

        Keyword arguments:
        namespace -> Specify the namespace name
        group_name -> Specify the ruler group name
        rules -> Specify the ruler rule object list
        recipient -> Specify the recipient of the alerts (default grafana)
        interval -> Specify the interval of the ruler (default 0)
        """

        if (
            len(recipient) != 0
            and len(namespace) != 0
            and len(group_name) != 0
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
                Api(self.grafana_api_model)
                .call_the_api(
                    f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
                    RequestsMethods.POST,
                    json.dumps(
                        {
                            "interval": interval,
                            "name": group_name,
                            "rules": rules_json_list,
                        }
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

    def delete_ruler_group(
        self, namespace: str, group_name: str, recipient: str = "grafana"
    ):
        """The method includes a functionality to delete a ruler group specified by the namespace name, a ruler group \
        name and the recipient

        Keyword arguments:
        namespace -> Specify the namespace name
        group_name -> Specify the ruler group name
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(namespace) != 0 and len(group_name) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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

    def get_ruler_group(
        self, namespace: str, group_name: str, recipient: str = "grafana"
    ) -> dict:
        """The method includes a functionality to get a ruler group specified by the namespace name, a ruler group \
        name and the recipient

        Keyword arguments:
        namespace -> Specify the namespace name
        group_name -> Specify the ruler group name
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if len(recipient) != 0 and len(namespace) != 0 and len(group_name) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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
        """The method includes a functionality to test a rule specified by a list of datasource rule query objects

        Keyword arguments:
        data_query -> Specify a list of datasource rule query objects
        """

        if data_query != list():
            api_call: str = (
                Api(self.grafana_api_model)
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
        self, expr: str, condition: str, data_query: list, recipient: str = "grafana"
    ) -> dict:
        """The method includes a functionality to test a recipient role specified by the expr, the condition, \
        a list of data queries and the recipient

        Keyword arguments:
        expr -> Specify the expression
        condition -> Specify the condition
        data_query -> Specify a list of datasource rule query objects
        recipient -> Specify the recipient of the alerts (default grafana)
        """

        if (
            len(recipient) != 0
            and len(expr) != 0
            and len(condition) != 0
            and data_query != list()
        ):
            api_call: dict = (
                Api(self.grafana_api_model)
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
        """The method includes a functionality to delete the ngalert organization admin configuration"""

        api_call: dict = (
            Api(self.grafana_api_model)
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
        """The method includes a functionality to get the ngalert organization admin configuration"""

        api_call: any = Api(self.grafana_api_model).call_the_api(
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
        self, alert_managers: list, alertmanagers_choice: str = "all"
    ):
        """The method includes a functionality to create or update the ngalert organization admin configuration

        Keyword arguments:
        alert_managers -> Specify the list of alert manager names
        alertmanagers_choice -> Specify the alertmanagers choice (default all)
        """

        if alert_managers != list() and len(alertmanagers_choice) != 0:
            api_call: dict = (
                Api(self.grafana_api_model)
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
        """The method includes a functionality to get the discovered and dropped alertmanagers of the user's \
        organization and based on the specified configuration
        """

        api_call: dict = (
            Api(self.grafana_api_model)
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
