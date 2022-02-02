import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods, Silence, AlertmanagerConfig
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
            api_call: list = Utils(self.grafana_api_model).call_the_api(
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

    def create_alertmanager_alerts(self, recipient: str, alerts: list):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        alerts -> Specify the list of the Alert -> Model objects
        """

        if len(recipient) != 0 and alerts != list():
            alerts_json_list: list = list()

            for alert in alerts:
                alert_json_dict: dict = dict({"startsAt": alert.starts_at, "endsAt": alert.ends_at,
                                              "generatorURL": alert.generator_url, "labels": alert.labels,
                                              "annotations": alert.annotations})
                alerts_json_list.append(alert_json_dict)

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/alerts/groups",
                RequestsMethods.POST,
                json.dumps(alerts_json_list),
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
            api_call: list = Utils(self.grafana_api_model).call_the_api(
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

    def delete_alertmanager_silence_by_id(self, recipient: str, silence_id: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and len(silence_id) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silence/{silence_id}",
                RequestsMethods.DELETE
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
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
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

    def get_alertmanager_silences(self, recipient: str) -> list:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: list = Utils(self.grafana_api_model).call_the_api(
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

    def create_alertmanager_silence(self, recipient: str, silence: Silence) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 or silence != Silence:
            silence_json_dict: dict = dict({"comment": silence.comment, "createdBy": silence.created_by,
                                            "endsAt": silence.ends_at, "id": silence.id, "matchers": silence.matchers,
                                            "startsAt": silence.starts_at})

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/api/v2/silences",
                RequestsMethods.POST,
                json.dumps(silence_json_dict)
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
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
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

    def delete_alertmanager_config(self, recipient: str):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0:
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                RequestsMethods.DELETE
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
            api_call: dict = Utils(self.grafana_api_model).call_the_api(
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

    def create_alertmanager_config(self, recipient: str, alertmanager_config: AlertmanagerConfig,
                                   template_files: dict = None) -> dict:
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and alertmanager_config != AlertmanagerConfig:
            alertmanager_configuration_json_dict: dict = dict()

            alertmanager_configuration_json_dict["alertmanager_config"] = alertmanager_config
            if template_files is not None:
                alertmanager_config["template_files"] = template_files

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                RequestsMethods.POST,
                json.dumps(alertmanager_configuration_json_dict)
            )

            if api_call == dict() or api_call.get("alertmanager_config") is None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error("There is no recipient or alertmanager_config defined.")
            raise ValueError

    def create_alertmanager_config(self, recipient: str, alertmanager_config: AlertmanagerConfig,
                                   template_files: dict = None):
        """The method includes a functionality to extract a specified version of a dashboard based on the specified \
        dashboard id and a version_id of the dashboard

        Keyword arguments:
        recipient -> Specify the id of the dashboard
        """

        if len(recipient) != 0 and alertmanager_config != AlertmanagerConfig:
            alertmanager_configuration_json_dict: dict = dict()

            alertmanager_configuration_json_dict["alertmanager_config"] = alertmanager_config
            if template_files is not None:
                alertmanager_config["template_files"] = template_files

            api_call: dict = Utils(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTS_ALERTMANAGER.value}/{recipient}/config/api/v1/alerts",
                RequestsMethods.POST,
                json.dumps(alertmanager_configuration_json_dict)
            )

            if api_call != dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully created alerting config.")
        else:
            logging.error("There is no recipient or alertmanager_config defined.")
            raise ValueError