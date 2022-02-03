from enum import Enum

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


class APIModel:
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Keyword arguments:
    host -> Specify the host of the Grafana system
    token -> Specify the access token of the Grafana system
    """

    def __init__(
        self,
        host: str = None,
        token: str = None,
    ):
        self.host = host
        self.token = token


class DatasourceQuery:
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

    def __init__(
            self,
            datasource_id: int,
            raw_sql: str,
            ref_id: str = "A",
            interval_ms: int = 1000,
            max_data_points: int = 100,
            output_format: str = "time_series",
    ):
        self.datasource_id = datasource_id
        self.raw_sql = raw_sql
        self.ref_id = ref_id
        self.interval_ms = interval_ms
        self.max_data_points = max_data_points
        self.output_format = output_format


class Alert:
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

    def __init__(
            self,
            starts_at: str,
            ends_at: str,
            annotations: dict,
            generator_url: str,
            labels: dict,
    ):
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.annotations = annotations
        self.generator_url = generator_url
        self.labels = labels


class Silence:
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

    def __init__(
            self,
            starts_at: str,
            created_by: str,
            ends_at: str,
            comment: str,
            id: str,
            matchers: dict,
    ):
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.created_by = created_by
        self.comment = comment
        self.id = id
        self.matchers = matchers


class AlertmanagerConfig:
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

    def __init__(
            self,
            global_config: dict,
            inhibit_rules: list,
            mute_time_intervals: list,
            receivers: list,
            route: dict,
            templates: list,
    ):
        self.global_config = global_config
        self.inhibit_rules = inhibit_rules
        self.mute_time_intervals = mute_time_intervals
        self.receivers = receivers
        self.route = route
        self.templates = templates


class AlertmanagerReceivers:
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

    def __init__(
            self,
            name: str,
            email_configs: list,
            grafana_managed_receiver_configs: list,
            opsgenie_configs: list,
            pagerduty_configs: list,
            pushover_configs: list,
            slack_configs: list,
            sns_configs: list,
            victorops_configs: list,
            webhook_configs: list,
            wechat_configs: list,
    ):
        self.name = name
        self.email_configs = email_configs
        self.grafana_managed_receiver_configs = grafana_managed_receiver_configs
        self.opsgenie_configs = opsgenie_configs
        self.pagerduty_configs = pagerduty_configs
        self.pushover_configs = pushover_configs
        self.slack_configs = slack_configs
        self.sns_configs = sns_configs
        self.victorops_configs = victorops_configs
        self.webhook_configs = webhook_configs
        self.wechat_configs = wechat_configs
