import json
import logging
from typing import List

from .model import APIModel, APIEndpoints, RequestsMethods, AlertRule, AlertQuery, AlertRuleQueryModel, \
    AlertRuleQueryModelCondition, EmbeddedContactPoint, Route, Matcher, MuteTimeInterval, TimeInterval, \
    DayOfMonthRange, MonthRange, TimeRange, WeekdayRange, YearRange
from .api import Api


# TODO Unittests
# TODO Integrationtest


class AlertingProvisioning:
    """The class includes all necessary methods to access the Grafana alerting provisioning API endpoints

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_alert_rule(self, uid: str) -> dict:
        """The method includes a functionality to get the alert rule specified by the uid

        Args:
            uid (str): Specify the alert rule uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the alert rule
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/alert-rules/{uid}",
            )

            if api_call == dict() or api_call.get("id") is not None:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def add_alert_rule(self, alert_rule: AlertRule):
        """The method includes a functionality to create a new alert rule

        Args:
            alert_rule (AlertRule): Specify the alert rule

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if alert_rule is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/alert-rules",
                RequestsMethods.POST,
                json.dumps(self.__create_alert_rule_dictionary(alert_rule)),
                response_status_code=True
            )
            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully created the corresponding alert rule."
                )
        else:
            logging.error(
                "There is no alert_rule defined."
            )
            raise ValueError

    def update_alert_rule(self, uid: str, alert_rule: AlertRule):
        """The method includes a functionality to update an existing alert rule

        Args:
            uid (str): Specify the alert rule uid
            alert_rule (AlertRule): Specify the alert rule

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0 and alert_rule is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/alert-rules/{uid}",
                RequestsMethods.PUT,
                json.dumps(self.__create_alert_rule_dictionary(alert_rule)),
                response_status_code=True
            )
            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the corresponding alert rule."
                )
        else:
            logging.error(
                "There is no uid or alert_rule defined."
            )
            raise ValueError

    def update_the_interval_of_a_alert_rule_group(self, folder_uid: str, group: str, alert_rule_group_interval: int):
        """The method includes a functionality to update the interval of a alert rule group

        Args:
            folder_uid (str): Specify the folder uid
            group (str): Specify the group
            alert_rule_group_interval (int): Specify the alert rule group interval

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(folder_uid) != 0 and len(group) != 0 and alert_rule_group_interval != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/folder/{folder_uid}/rule-groups/{group}",
                RequestsMethods.PUT,
                json.dumps({"interval": alert_rule_group_interval}),
                response_status_code=True
            )
            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the corresponding alert rule group interval."
                )
        else:
            logging.error(
                "There is no folder_uid, group or alert_rule_group_interval defined."
            )
            raise ValueError

    def delete_alert_rule(self, uid: str):
        """The method includes a functionality to delete an alert rule

        Args:
            uid (str): Specify the alert rule uid

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call
        Returns:
            None
        """

        if len(uid) == 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/alert-rules/{uid}",
                RequestsMethods.DELETE,
                response_status_code=True
            )
            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully deleted the corresponding alert rule."
                )
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def get_all_contact_points(self) -> list:
        """The method includes a functionality to get all contact points

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all contact points
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTING_PROVISIONING.value}/contact-points",
        )

        if api_call == list():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def add_contact_point(self, embedded_contact_point: EmbeddedContactPoint):
        """The method includes a functionality to create a contact point

        Args:
            embedded_contact_point (EmbeddedContactPoint): Specify the embedded contact point

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if embedded_contact_point is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/contact-points",
                RequestsMethods.POST,
                json.dumps({
                    "name": embedded_contact_point.name,
                    "type": embedded_contact_point.type,
                    "settings": embedded_contact_point.settings,
                    "disableResolveMessage": embedded_contact_point.disable_resolve_message,
                    "provenance": embedded_contact_point.provenance,
                    "UID": embedded_contact_point.uid
                }),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully created a new contact point."
                )
        else:
            logging.error(
                "There is no embedded_contact_point defined."
            )
            raise ValueError

    def update_contact_point(self, uid: str, embedded_contact_point: EmbeddedContactPoint):
        """The method includes a functionality to update a contact point

        Args:
            uid (str): Specify the uid of the contact point
            embedded_contact_point (EmbeddedContactPoint): Specify the embedded contact point

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0 and embedded_contact_point is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/contact-points/{uid}",
                RequestsMethods.PUT,
                json.dumps({
                    "name": embedded_contact_point.name,
                    "type": embedded_contact_point.type,
                    "settings": embedded_contact_point.settings,
                    "disableResolveMessage": embedded_contact_point.disable_resolve_message,
                    "provenance": embedded_contact_point.provenance,
                    "UID": embedded_contact_point.uid
                }),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the contact point."
                )
        else:
            logging.error(
                "There is no embedded_contact_point or uid defined."
            )
            raise ValueError

    def delete_contact_point(self, uid: str):
        """The method includes a functionality to delete a contact point

        Args:
            uid (str): Specify the uid of the contact point

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/contact-points/{uid}",
                RequestsMethods.DELETE,
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully deleted the contact point."
                )
        else:
            logging.error(
                "There is no uid defined."
            )
            raise ValueError

    def get_notification_policies(self) -> dict:
        """The method includes a functionality to get the notification policy tree

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Returns the notification policy tree
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTING_PROVISIONING.value}/policies",
            response_status_code=True
        )

        if 200 <= api_call.get("status") < 300:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def add_notification_policies(self, route: Route):
        """The method includes a functionality to set the notification policy tree

        Args:
            route (Route): Specify the alert rule routes

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if route is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/policies",
                RequestsMethods.PUT,
                json.dumps(self.__create_alert_route_dictionary(route)),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully added the notification policies."
                )
        else:
            logging.error(
                "There is no route defined."
            )
            raise ValueError

    def get_all_mute_timings(self) -> list:
        """The method includes a functionality to get all mute timings

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTING_PROVISIONING.value}/mute-timings",
        )

        if api_call == list():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_mute_timing(self, name: str) -> dict:
        """The method includes a functionality to get a mute timings specified by the name

        Args:
            name (str): Specify the mute timing name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/mute-timings/{name}",
            )

            if api_call == dict():
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no name defined."
            )
            raise ValueError

    def add_mute_timing(self, mute_time_interval: MuteTimeInterval):
        """The method includes a functionality to create a mute timing

        Args:
            mute_time_interval (MuteTimeInterval): Specify the mute time interval

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        if mute_time_interval is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/mute-timings",
                RequestsMethods.POST,
                json.dumps(self.__create_mute_timing_dictionary(mute_time_interval)),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully added the mute timing."
                )
        else:
            logging.error(
                "There is no mute_time_interval defined."
            )
            raise ValueError

    def update_mute_timing(self, name: str, mute_time_interval: MuteTimeInterval):
        """The method includes a functionality to update an existing mute timing

        Args:
            name (str): Specify the mute timing name
            mute_time_interval (MuteTimeInterval): Specify the mute time interval

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        if len(name) != 0 and mute_time_interval is not None:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/mute-timings/{name}",
                RequestsMethods.PUT,
                json.dumps(self.__create_mute_timing_dictionary(mute_time_interval)),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully updated the mute timing."
                )
        else:
            logging.error(
                "There is no name or mute_time_interval defined."
            )
            raise ValueError

    def delete_mute_timing(self, name: str):
        """The method includes a functionality to delete a mute timings specified by the name

        Args:
            name (str): Specify the mute timing name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/mute-timings/{name}",
                RequestsMethods.DELETE,
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully deleted the mute timing."
                )
        else:
            logging.error(
                "There is no name defined."
            )
            raise ValueError

    def get_all_message_templates(self) -> list:
        """The method includes a functionality to get all message templates

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all message templates
        """

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.ALERTING_PROVISIONING.value}/templates",
        )

        if api_call == list():
            logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            return api_call

    def get_message_template(self, name: str) -> dict:
        """The method includes a functionality to get a message template specified by the name

        Args:
            name (str): Specify the message template name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all message templates
        """

        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/templates/{name}",
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                return api_call
        else:
            logging.error(
                "There is no name defined."
            )
            raise ValueError

    def create_or_update_message_template(self, name: str, message_template: str):
        """The method includes a functionality to create or update a message template

        Args:
            name (str): Specify the message template name
            message_template (str): Specify the message template

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(name) != 0 and len(message_template) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/templates/{name}",
                RequestsMethods.PUT,
                json.dumps({"template": message_template}),
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully created/ updated the message template."
                )
        else:
            logging.error(
                "There is no name or message defined."
            )
            raise ValueError

    def delete_message_template(self, name: str):
        """The method includes a functionality to delete a message template

        Args:
            name (str): Specify the message template name

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Returns all mute timings
        """

        if len(name) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.ALERTING_PROVISIONING.value}/templates/{name}",
                RequestsMethods.DELETE,
                response_status_code=True
            )

            if 200 <= api_call.get("status") < 300:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
            else:
                logging.info(
                    "You successfully deleted the message template."
                )
        else:
            logging.error(
                "There is no name defined."
            )
            raise ValueError

    def __create_mute_timing_dictionary(self, mute_time_interval: MuteTimeInterval) -> dict:
        return dict(
            {
                "name": mute_time_interval.name,
                "time_intervals": self.__create_mute_timing_interval_list(mute_time_interval.time_intervals),
            }
        )

    def __create_mute_timing_interval_list(self, time_intervals: List[TimeInterval]) -> list:
        mute_timing_interval_list: list = list()

        for time_interval in time_intervals:
            mute_timing_interval_list.append({"daysOfMonth": self.__create_timing_list(time_interval.days_of_month),
                                              "months": self.__create_timing_list(time_interval.months),
                                              "times": self.__create_timing_list(time_interval.times),
                                              "weekdays": self.__create_timing_list(time_interval.weekdays),
                                              "years": self.__create_timing_list(time_interval.years),
                                              })

        return mute_timing_interval_list

    @staticmethod
    def __create_timing_list(timing: (List[DayOfMonthRange], List[MonthRange], List[TimeRange],
                                      List[WeekdayRange], List[YearRange])) -> list:
        timing_list: list = list()

        for time in timing:
            timing_list.append({"begin": time.begin, "end": time.end})

        return timing_list

    def __create_alert_route_dictionary(self, route: Route) -> dict:
        return dict(
            {
                "continue": route.continue_parameter,
                "groupByStr": route.group_by_str,
                "muteTimeIntervals": route.mute_time_intervals,
                "receiver": route.receiver,
                "routes": self.__create_alert_routes_list(route.routes),
                "group_interval": route.group_interval,
                "group_wait": route.group_wait,
                "object_matchers": self.__create_object_matcher_list(route.object_matchers),
                "provenance": route.provenance,
                "repeat_interval": route.repeat_interval,
            }
        )

    def __create_alert_routes_list(self, routes: List[Route]) -> list:
        routes_list: list = list()

        for route in routes:
            routes_list.append(self.__create_alert_route_dictionary(route))

        return routes_list

    @staticmethod
    def __create_object_matcher_list(matchers: List[Matcher]) -> list:
        route_matchers_list: list = list()

        for matcher in matchers:
            route_matcher_dict: dict = dict(
                {
                    "name": matcher.name,
                    "type": matcher.type.value,
                    "value": matcher.value,
                }
            )

            route_matchers_list.append(route_matcher_dict)

        return route_matchers_list

    def __create_alert_rule_dictionary(self, alert_rule: AlertRule) -> dict:
        return dict(
            {
                "annotations": alert_rule.annotations,
                "condition": alert_rule.condition,
                "data": self.__create_alert_rule_query_dictionary(alert_rule.data),
                "execErrState": alert_rule.exec_err_state,
                "folderUID": alert_rule.folder_uid,
                "id": alert_rule.id,
                "labels": alert_rule.labels,
                "noDataState": alert_rule.no_data_state,
                "orgID": alert_rule.org_id,
                "ruleGroup": alert_rule.rule_group,
                "title": alert_rule.title,
                "uid": alert_rule.uid,
                "updated": alert_rule.updated,
                "for": alert_rule.for_time,
                "provenance": alert_rule.provenance
            }
        )

    def __create_alert_rule_query_dictionary(self, alert_queries: List[AlertQuery]) -> list:
        alert_rule_queries_list: list = list()

        for alert_query in alert_queries:
            alert_query_dict: dict = dict(
                {
                    "datasourceUID": alert_query.datasource_uid,
                    "model": self.__create_alert_rule_query_model_dictionary(alert_query.model),
                    "queryType": alert_query.query_type,
                    "refID": alert_query.ref_id,
                    "relativeTimeRange": {
                        "from": alert_query.relative_time_range_from,
                        "to": alert_query.relative_time_range_to
                    }
                }
            )

            alert_rule_queries_list.append(alert_query_dict)

        return alert_rule_queries_list

    def __create_alert_rule_query_model_dictionary(self, alert_query_model: AlertRuleQueryModel) -> dict:
        return dict(
            {
                "conditions": self.__create_alert_rule_query_model_condition_list(alert_query_model.conditions),
                "datasource": alert_query_model.datasource,
                "expression": alert_query_model.expression,
                "hide": alert_query_model.hide,
                "intervalMs": alert_query_model.interval_ms,
                "maxDataPoints": alert_query_model.max_data_points,
                "refId": alert_query_model.ref_id,
                "type": alert_query_model.type
            }
        )

    @staticmethod
    def __create_alert_rule_query_model_condition_list(
            alert_rule_query_model_conditions: List[AlertRuleQueryModelCondition]) -> list:

        alert_rule_query_model_conditions_list: list = list()

        for alert_rule_query_model_condition in alert_rule_query_model_conditions:
            alert_rule_query_model_condition_dict: dict = dict(
                {
                    "evaluator": {
                        "params": alert_rule_query_model_condition.evaluator_params,
                        "type": alert_rule_query_model_condition.evaluator_type
                    },
                    "operator": {
                        "type": alert_rule_query_model_condition.operator_type
                    },
                    "query": {
                        "params": alert_rule_query_model_condition.query_params
                    },
                    "reducer": {
                        "params": alert_rule_query_model_condition.reducer_params,
                        "type": alert_rule_query_model_condition.reducer_type
                    },
                    "type": alert_rule_query_model_condition.type
                }
            )

            alert_rule_query_model_conditions_list.append(alert_rule_query_model_condition_dict)

        return alert_rule_query_model_conditions_list
