import datetime
import json
import logging

from .model import (
    APIModel,
    APIEndpoints,
    RequestsMethods,
    Silence,
    AlertmanagerConfig,
)
from .api import Api


class Alerting:
    """The class includes all necessary methods to access the Grafana alerting API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alertmanager_alerts(self, recipient: any = "grafana") -> list:
        """The method includes a functionality to get the Alertmanager alerts specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager alerts
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts",
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
        self, alerts: list, recipient: any = "grafana"
    ):
        """The method includes a functionality to create or update the Alertmanager alerts specified by the recipient and the alerts list

        Args:
            alerts (list): Specify a list of the alert objects
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and alerts != list():
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

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts/groups",
                RequestsMethods.POST,
                json.dumps(alerts_json_list),
            )

            if api_call != dict():
                logging.error(f"Please, check the error: {api_call.get('message')}.")
                raise Exception
            else:
                logging.info("You successfully created alerts.")
        else:
            logging.error("There is no recipient or alerts defined.")
            raise ValueError

    def get_alertmanager_group_alerts(self, recipient: any = "grafana") -> list:
        """The method includes a functionality to get the Alertmanager group alerts specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager group alerts
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts",
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
        self, silence_id: str, recipient: any = "grafana"
    ):
        """The method includes a functionality to delete the Alertmanager silence specified by the silence id and the recipient

        Args:
            silence_id (str): Specify the silence id of the alerts
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and len(silence_id) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silence/{silence_id}",
                RequestsMethods.DELETE,
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
        self, silence_id: str, recipient: any = "grafana"
    ) -> dict:
        """The method includes a functionality to get the Alertmanager silence specified by the silence id and the recipient

        Args:
            silence_id (str): Specify the silence id of the alerts
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of Alertmanager silence alert
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and len(silence_id) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silence/{silence_id}",
            )

            if api_call == dict() or api_call.get("id") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient or silence_id defined.")
            raise ValueError

    def get_alertmanager_silences(self, recipient: any = "grafana") -> list:
        """The method includes a functionality to get all Alertmanager silences specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns the list of Alertmanager silence alerts
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silences",
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
        self, silence: Silence, recipient: any = "grafana"
    ) -> dict:
        """The method includes a functionality to create or update the Alertmanager silence specified by the silence object and the recipient

        Args:
            silence -> Specify the silence object
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of newly created silence alert
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) or silence is not None:
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

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silences",
                RequestsMethods.POST,
                json.dumps(silence_json_dict),
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
        """The method includes a functionality to get the Alertmanager status specified by the recipient

        Args:
            recipient (str): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the Alertmanager status
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/status",
            )

            if api_call == dict() or api_call.get("config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def delete_alertmanager_config(self, recipient: any = "grafana"):
        """The method includes a functionality to delete the Alertmanager config specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                RequestsMethods.DELETE,
            )

            if (
                api_call.get("message")
                != "configuration deleted; the default is applied"
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully deleted a alerting config.")
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def get_alertmanager_config(self, recipient: any = "grafana") -> dict:
        """The method includes a functionality to get the Alertmanager config specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the Alertmanager config
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
            )

            if api_call == dict() or api_call.get("alertmanager_config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def create_or_update_alertmanager_config(
        self,
        alertmanager_config: AlertmanagerConfig,
        recipient: any = "grafana",
        template_files: dict = None,
    ):
        """The method includes a functionality to create or update the Alertmanager config specified by the Alertmanager config object, recipient and template_files

        Args:
            alertmanager_config (AlertmanagerConfig): Specify the Alertmanager config object
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)
            template_files(dict): Specify the optional template files (default None)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and alertmanager_config is not None:
            alertmanager_configuration_json_dict: dict = dict()

            alertmanager_configuration_json_dict["alertmanager_config"] = dict(
                {
                    "global": alertmanager_config.global_config,
                    "inhibit_rules": alertmanager_config.inhibit_rules,
                    "mute_time_intervals": alertmanager_config.mute_time_intervals,
                    "receivers": alertmanager_config.receivers,
                    "route": alertmanager_config.route,
                    "templates": alertmanager_config.templates,
                }
            )

            if template_files is not None:
                alertmanager_configuration_json_dict["template_files"] = template_files

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                RequestsMethods.POST,
                json.dumps(alertmanager_configuration_json_dict),
            )

            if (
                api_call == dict()
                or api_call.get("message")
                != "policies were provisioned and cannot be changed through the UI"
            ):
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created an Alertmanager alert config.")
        else:
            logging.error("There is no recipient or alertmanager_config defined.")
            raise ValueError

    def test_alertmanager_receivers(
        self, alert: dict, receivers: list, recipient: any = "grafana"
    ):
        """The method includes a functionality to test the Alertmanager receivers specified by the alert dict, receivers object and the recipient

        Args:
            alert (dict): Specify the alert dict
            receivers (list): Specify the list of AlertmanagerReceivers objects
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (
                (isinstance(recipient, int) and recipient != 0)
                or (isinstance(recipient, str) and len(recipient) != 0)
            )
            and alert != dict()
            and receivers is not None
        ):
            alertmanager_receivers_json_dict: dict = dict()
            receivers_list: list = list()

            alertmanager_receivers_json_dict["alert"] = alert

            for receiver in receivers:
                receivers_list.append(
                    dict(
                        {
                            "name": receiver.name,
                            "email_configs": receiver.email_configs,
                            "grafana_managed_receiver_configs": receiver.grafana_managed_receiver_configs,
                            "opsgenie_configs": receiver.opsgenie_configs,
                            "pagerduty_configs": receiver.pagerduty_configs,
                            "pushover_configs": receiver.pushover_configs,
                            "slack_configs": receiver.slack_configs,
                            "sns_configs": receiver.sns_configs,
                            "victorops_configs": receiver.victorops_configs,
                            "webhook_configs": receiver.webhook_configs,
                            "wechat_configs": receiver.wechat_configs,
                        }
                    )
                )

            alertmanager_receivers_json_dict["receivers"] = receivers_list

            api_call: any = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/receivers/test",
                RequestsMethods.POST,
                json.dumps(alertmanager_receivers_json_dict),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")
            api_call_dict: dict = api_call

            alert_manager_status_dict: dict = dict(
                {
                    200: "You successfully tested Grafana managed receivers.",
                    207: "You successfully tested Grafana managed receivers (Multi Status).",
                    400: f"Validation error. Check the error: {api_call_dict.get('message')}.",
                    403: "Permission denied. Please, check the access rights.",
                    404: "Alert manager not found. Please, check the alert manager configuration.",
                    408: f"Failure. Check the error: {api_call_dict.get('message')}.",
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

    def get_prometheus_alerts(self, recipient: any = "grafana") -> dict:
        """The method includes a functionality to get all prometheus alerts specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the prometheus alerts
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_PROMETHEUS.value}/{recipient}/api/v1/alerts",
            )

            if api_call == dict() or api_call.get("data") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def get_prometheus_rules(self, recipient: any = "grafana") -> dict:
        """The method includes a functionality to get all prometheus rules specified by the recipient

        Args:
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the prometheus rules
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_PROMETHEUS.value}/{recipient}/api/v1/rules",
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

        Args:
            recipient (str): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the ruler rules
        """

        if (isinstance(recipient, int) and recipient != 0) or (
            isinstance(recipient, str) and len(recipient) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules",
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient defined.")
            raise ValueError

    def delete_ruler_namespace(self, namespace: str, recipient: any = "grafana"):
        """The method includes a functionality to delete a ruler namespace specified by the namespace name and the recipient

        Args:
            namespace (str): Specify the namespace name
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and len(namespace) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
                RequestsMethods.DELETE,
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
        self, namespace: str, recipient: any = "grafana"
    ) -> dict:
        """The method includes a functionality to get all ruler groups specified by the namespace name and the recipient

        Args:
            namespace (str): Specify the namespace name
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of the ruler groups
        """

        if (
            (isinstance(recipient, int) and recipient != 0)
            or (isinstance(recipient, str) and len(recipient) != 0)
        ) and len(namespace) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}",
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
        recipient: any = "grafana",
        interval: int = 0,
    ):
        """The method includes a functionality to create or update a ruler group specified by the namespace name, a ruler group name, a ruler rule object list, the recipient and an interval

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            rules (list): Specify the ruler rule object list
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)
            interval (int): Specify the interval of the ruler (default 0)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (
                (isinstance(recipient, int) and recipient != 0)
                or (isinstance(recipient, str) and len(recipient) != 0)
            )
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

            api_call: dict = Api(self.grafana_api_model).call_the_api(
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

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created an ruler group.")
        else:
            logging.error("There is no recipient, namespace, name or rules defined.")
            raise ValueError

    def delete_ruler_group(
        self, namespace: str, group_name: str, recipient: any = "grafana"
    ):
        """The method includes a functionality to delete a ruler group specified by the namespace name, a ruler group name and the recipient

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            (
                (isinstance(recipient, int) and recipient != 0)
                or (isinstance(recipient, str) and len(recipient) != 0)
            )
            and len(namespace) != 0
            and len(group_name) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}/{group_name}",
                RequestsMethods.DELETE,
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
        self, namespace: str, group_name: str, recipient: any = "grafana"
    ) -> dict:
        """The method includes a functionality to get a ruler group specified by the namespace name, a ruler group name and the recipient

        Args:
            namespace (str): Specify the namespace name
            group_name (str): Specify the ruler group name
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the dict of all ruler groups
        """

        if (
            (
                (isinstance(recipient, int) and recipient != 0)
                or (isinstance(recipient, str) and len(recipient) != 0)
            )
            and len(namespace) != 0
            and len(group_name) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_RULER.value}/{recipient}/api/v1/rules/{namespace}/{group_name}",
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient, namespace or group_name defined.")
            raise ValueError

    def test_rule(self, data_query: list) -> dict:
        """The method includes a functionality to test a rule specified by a list of datasource rule query objects

        Args:
            data_query (list): Specify a list of datasource rule query objects

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (str): Returns the result of the specified query
        """

        if data_query != list():
            datasource_rule_query_objects_json: list = list()
            datasource_rule_query_object_json: dict = dict()

            for datasource_rule_query_object in data_query:
                datasource_rule_query_object_json[
                    "datasourceUid"
                ] = datasource_rule_query_object.datasource_uid
                datasource_rule_query_object_json[
                    "model"
                ] = datasource_rule_query_object.model
                datasource_rule_query_object_json[
                    "queryType"
                ] = datasource_rule_query_object.query_type
                datasource_rule_query_object_json[
                    "refId"
                ] = datasource_rule_query_object.ref_id
                datasource_rule_query_object_json[
                    "relativeTimeRange"
                ] = datasource_rule_query_object.relative_time_range
                datasource_rule_query_objects_json.append(
                    datasource_rule_query_object_json
                )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                "/api/v1/eval",
                RequestsMethods.POST,
                json.dumps(
                    {
                        "data": datasource_rule_query_objects_json,
                        "now": str(datetime.datetime.now()),
                    }
                ),
            )

            if api_call == dict() or api_call.get("message") is not None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no data_query defined.")
            raise ValueError

    def test_recipient_rule(
        self, expr: str, condition: str, data_query: list, recipient: any = "grafana"
    ) -> dict:
        """The method includes a functionality to test a recipient role specified by the expr, the condition, a list of data queries and the recipient

        Args:
            expr (str): Specify a list of datasource rule query objects
            condition (str): Specify the condition
            data_query (list): Specify a list of datasource rule query objects
            recipient (any): Specify the recipient datasource id of the alerts (default grafana)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the result of the specified recipient rule
        """

        if (
            (
                (isinstance(recipient, int) and recipient != 0)
                or (isinstance(recipient, str) and len(recipient) != 0)
            )
            and len(expr) != 0
            and len(condition) != 0
            and data_query != list()
        ):
            datasource_rule_query_objects_json: list = list()
            datasource_rule_query_object_json: dict = dict()

            for datasource_rule_query_object in data_query:
                datasource_rule_query_object_json[
                    "datasourceUid"
                ] = datasource_rule_query_object.datasource_uid
                datasource_rule_query_object_json[
                    "model"
                ] = datasource_rule_query_object.model
                datasource_rule_query_object_json[
                    "queryType"
                ] = datasource_rule_query_object.query_type
                datasource_rule_query_object_json[
                    "refId"
                ] = datasource_rule_query_object.ref_id
                datasource_rule_query_object_json[
                    "relativeTimeRange"
                ] = datasource_rule_query_object.relative_time_range
                datasource_rule_query_objects_json.append(
                    datasource_rule_query_object_json
                )

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"/api/v1/rule/test/{recipient}",
                RequestsMethods.POST,
                json.dumps(
                    {
                        "expr": expr,
                        "grafana_condition": {
                            "condition": condition,
                            "data": datasource_rule_query_objects_json,
                            "now": str(datetime.datetime.now()),
                        },
                    }
                ),
            )

            if api_call == dict() or api_call.get("message") is not None:
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
        """The method includes a functionality to delete the NGAlert organization admin configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
            RequestsMethods.DELETE,
        )

        if api_call != dict() and api_call.get("message") is not None:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.info(
                "You successfully deleted the NGAlert organization configuration."
            )

    def get_ngalert_organization_configuration(self) -> dict:
        """The method includes a functionality to get the NGAlert organization admin configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the NGAlert organization configuration
        """

        api_call: any = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
            response_status_code=True,
        )

        status_code: int = api_call.get("status")

        alert_manager_status_dict: dict = dict(
            {
                404: "There's no configuration available.",
                500: "Failure, an unexpected error occurred.",
            }
        )

        if status_code == 200:
            return api_call
        elif 404 <= status_code <= 500:
            logging.error(alert_manager_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def create_or_update_ngalert_organization_configuration(
        self, alert_managers: list, alertmanagers_choice: str = "all"
    ):
        """The method includes a functionality to create or update the NGAlert organization admin configuration

        Args:
            alert_managers (list): Specify the list of alert manager names
            alertmanagers_choice (str): Specify the Alertmanagers choice (default all)

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if alert_managers != list() and len(alertmanagers_choice) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_NGALERT.value}/admin_config",
                RequestsMethods.POST,
                json.dumps(
                    {
                        "Alertmanagers": alert_managers,
                        "alertmanagersChoice": alertmanagers_choice,
                    }
                ),
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully created an NGAlert organization configuration."
                )
        else:
            logging.error(
                "There is no recipient, expr, condition or data_query defined."
            )
            raise ValueError

    def get_ngalert_alertmanagers_by_organization(self) -> dict:
        """The method includes a functionality to get the discovered and dropped Alertmanagers of the user's organization and based on the specified configuration

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the NGAlert Alertmanagers
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTS_NGALERT.value}/Alertmanagers",
        )

        if api_call == dict():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call
