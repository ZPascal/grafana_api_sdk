from enum import Enum
from typing import NamedTuple

ERROR_MESSAGES: list = ["invalid API key"]


class APIEndpoints(Enum):
    # TODO Update the documentation
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

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
    # TODO Update the documentation
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


class APIModel(NamedTuple):
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    host -> Specify the host of the Grafana system
    token -> Specify the access token of the Grafana system
    """

    host: str
    token: str


class DatasourceQuery(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    datasource_id: int
    raw_sql: str
    ref_id: str = "A"
    interval_ms: int = 1000
    max_data_points: int = 100
    output_format: str = "time_series"


class DatasourceRuleQuery(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    datasource_uid: str
    model: dict
    query_type: str
    ref_id: str
    relative_time_range: dict


class Alert(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    starts_at: str
    ends_at: str
    annotations: dict
    generator_url: str
    labels: dict


class Silence(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    starts_at: str
    created_by: str
    ends_at: str
    comment: str
    id: str
    matchers: dict


class AlertmanagerConfig(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    global_config: dict
    inhibit_rules: list
    mute_time_intervals: list
    receivers: list
    route: dict
    templates: list


class AlertmanagerReceivers(NamedTuple):
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
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
    # TODO Update the documentation
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    datasource_id -> Specify the host of the Grafana system
    raw_sql -> Specify the access token of the Grafana system
    ref_id -> Specify the access token of the Grafana system
    interval_ms -> Specify the access token of the Grafana system
    max_data_points -> Specify the access token of the Grafana system
    output_format -> Specify the access token of the Grafana system
    """

    alert: str
    annotations: dict
    expr: str
    grafana_alert: dict
    labels: dict
    record: str
    for_id: int = 0
