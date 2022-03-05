from enum import Enum
from typing import NamedTuple

# The constant includes all necessary error messages that can occurs, if you establish a connection to the Grafana API.
ERROR_MESSAGES: list = ["invalid API key"]


class APIEndpoints(Enum):
    """The class includes all necessary API endpoint strings to connect the Grafana API."""

    SEARCH = "/api/search"
    DASHBOARDS = "/api/dashboards"
    FOLDERS = "/api/folders"
    LEGACY_ALERTS = "/api/alerts"
    ALERT_NOTIFICATIONS = "/api/alert-notifications"
    ALERTS_ALERTMANAGER = "/api/alertmanager"
    ALERTS_PROMETHEUS = "/api/prometheus"
    ALERTS_RULER = "/api/ruler"
    ALERTS_TESTING = "/api/v1"
    ALERTS_NGALERT = "/api/v1/ngalert"
    DATASOURCES = "/api/datasources"
    DATASOURCE_QUERY = "/api/tsdb/query"


class RequestsMethods(Enum):
    """The class includes all necessary methods to establish an HTTP/ HTTPS connection to the Grafana API endpoints."""

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


class APIModel(NamedTuple):
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints.

    Keyword arguments:
    host -- Specify the host of the Grafana system.
    token -- Specify the access token of the Grafana system.
    """

    host: str
    token: str


class DatasourceQuery(NamedTuple):
    """The class includes all necessary variables to specify a query for the datasource search endpoint.

    Keyword arguments:
    datasource_id -- Specify the id of the data source.
    raw_sql -- Specify the raw SQL string to search inside the Grafana system.
    ref_id -- Specify a reference id of the search command. (default A)
    interval_ms -- Specify the time interval in milliseconds of output format. (default 1000)
    max_data_points -- Specify maximum amount of data points that dashboard panel can render. (default 100)
    output_format -- Specify the output format of the query. (default time_series)
    """

    datasource_id: int
    raw_sql: str
    ref_id: str = "A"
    interval_ms: int = 1000
    max_data_points: int = 100
    output_format: str = "time_series"


class DatasourceRuleQuery(NamedTuple):
    """The class includes all necessary variables to specify a query for the datasource rule search endpoint.

    Keyword arguments:
    datasource_id -- Specify the id of the data source.
    model -- Specify the model of the search command.
    query_type --  Specify the query time of the search command.
    ref_id -- Specify a reference id of the search command.
    relative_time_range -- Specify the related time range of the search command.
    """

    datasource_uid: str
    model: dict
    query_type: str
    ref_id: str
    relative_time_range: dict


class Alert(NamedTuple):
    """The class includes all necessary variables to generate an alert object that is necessary to communicate with \
    the Grafana alert endpoint.

    Keyword arguments:
    starts_at -- Specify the start date of the alert.
    ends_at -- Specify end date of the alert.
    annotations -- Specify the annotations of the alert.
    generator_url -- Specify the url of the generator endpoint.
    labels -- Specify labels of the alert.
    """

    starts_at: str
    ends_at: str
    annotations: dict
    generator_url: str
    labels: dict


class Silence(NamedTuple):
    """The class includes all necessary variables to generate a silence object that is necessary to communicate with \
    the Grafana silence endpoint.

    Keyword arguments:
    starts_at -- Specify the start date of the silence.
    created_by -- Specify the name of the silence creator.
    ends_at -- Specify end date of the silence.
    comment -- Specify a custom comment for the silence.
    id -- Specify an id for the silence.
    matchers -- Specify matchers for the silence.
    """

    starts_at: str
    created_by: str
    ends_at: str
    comment: str
    id: str
    matchers: dict


class AlertmanagerConfig(NamedTuple):
    """The class includes all necessary variables to generate an Alertmanager config object that is necessary to \
    communicate and set up the Grafana Alertmanager endpoint.

    Keyword arguments:
    global_config -- Specify the global config of the Alertmanager.
    inhibit_rules -- Specify the inhibit rules of the Alertmanager.
    mute_time_intervals -- Specify the mute time intervals of the Alertmanager.
    receivers -- Specify the receivers of the Alertmanager.
    route -- Specify the route of the Alertmanager.
    templates -- Specify an Alertmanager template.
    """

    global_config: dict
    inhibit_rules: list
    mute_time_intervals: list
    receivers: list
    route: dict
    templates: list


class AlertmanagerReceivers(NamedTuple):
    """The class includes all necessary variables to generate an Alertmanager receivers object that is necessary to \
    communicate and set up the Grafana Alertmanager receivers endpoint.

    Keyword arguments:
    name -- Specify the name of the receiver
    email_configs -- Specify the email configuration of the receiver's
    grafana_managed_receiver_configs -- Specify the Grafana managed receiver configuration of the receiver's
    opsgenie_configs -- Specify the ops genie configuration of the receiver's
    pagerduty_configs -- Specify the pager duty configuration of the receiver's
    pushover_configs -- Specify the push over configuration of the receiver's
    slack_configs -- Specify the Slack configuration of the receiver's
    victorops_configs -- Specify the victor ops configuration of the receiver's
    webhook_configs -- Specify the webhook configuration of the receiver's
    wechat_configs -- Specify the wechaty configuration of the receiver's
    """

    name: str
    email_configs: list
    grafana_managed_receiver_configs: list
    opsgenie_configs: list
    pagerduty_configs: list
    pushover_configs: list
    slack_configs: list
    sns_configs: list
    victorops_configs: list
    webhook_configs: list
    wechat_configs: list


class RulerRule(NamedTuple):
    """The class includes all necessary variables to generate a Ruler rule object that is necessary to \
    communicate and set up a Grafana Ruler rule.

    Keyword arguments:
    alert -- Specify the name of the rule.
    annotations -- Specify the annotations of the rule.
    expr -- Specify the expression of the rule.
    grafana_alert -- Specify the Grafana alert of the rule.
    labels -- Specify labels of the rule.
    record -- Specify recode value of the rule.
    for_id -- Specify the id of the rule if you update an existing rule. (default 0)
    """

    alert: str
    annotations: dict
    expr: str
    grafana_alert: dict
    labels: dict
    record: str
    for_id: int = 0
