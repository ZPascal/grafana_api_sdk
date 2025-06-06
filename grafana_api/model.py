import ssl
import httpx
from enum import Enum
from typing import List, TypeVar, Union
from dataclasses import dataclass, field

Self = TypeVar("Self", bound="Route")

# The constant includes all necessary error messages that can occurs, if you establish a connection to the Grafana API.
ERROR_MESSAGES: list = ["invalid API key", "Invalid API key", "Expired API key"]


class APIEndpoints(Enum):
    """The class includes all necessary API endpoint strings to connect the Grafana API"""

    api_prefix: str = "/api"
    version_1: str = "v1"

    SEARCH: str = f"{api_prefix}/search"
    DASHBOARDS: str = f"{api_prefix}/dashboards"
    FOLDERS: str = f"{api_prefix}/folders"
    LEGACY_ALERTS: str = f"{api_prefix}/alerts"
    ALERT_NOTIFICATIONS: str = f"{api_prefix}/alert-notifications"
    ALERTS_ALERTMANAGER: str = f"{api_prefix}/alertmanager"
    ALERTS_PROMETHEUS: str = f"{api_prefix}/prometheus"
    ALERTS_RULER: str = f"{api_prefix}/ruler"
    ALERTS_TESTING: str = f"{api_prefix}/{version_1}"
    ALERTS_NGALERT: str = f"{api_prefix}/{version_1}/ngalert"
    ALERTING_PROVISIONING: str = f"{api_prefix}/{version_1}/provisioning"
    DATASOURCES: str = f"{api_prefix}/datasources"
    DATASOURCE_QUERY: str = f"{api_prefix}/tsdb/query"
    DATASOURCE_PERMISSIONS: str = f"{api_prefix}/access-control/datasources"
    SHORT_URLS: str = f"{api_prefix}/short-urls"
    ORGANISATION: str = f"{api_prefix}/org"
    ORGANISATIONS: str = f"{api_prefix}/orgs"
    USER: str = f"{api_prefix}/user"
    USERS: str = f"{api_prefix}/users"
    SNAPSHOTS: str = f"{api_prefix}/snapshots"
    DASHBOARD_SNAPSHOTS: str = f"{api_prefix}/dashboard/snapshots"
    PLAYLISTS: str = f"{api_prefix}/playlists"
    TEAMS: str = f"{api_prefix}/teams"
    QUERY_HISTORY: str = f"{api_prefix}/query-history"
    REPORTING: str = f"{api_prefix}/reports"
    LICENSING: str = f"{api_prefix}/licensing"
    FRONTEND: str = f"{api_prefix}/frontend"
    LOGIN: str = f"{api_prefix}/login"
    AUTHENTICATION: str = f"{api_prefix}/auth/keys"
    EXTERNAL_GROUPS: str = f"{api_prefix}/teams"
    USER_PREFERENCES: str = f"{api_prefix}/user/preferences"
    ORG_PREFERENCES: str = f"{api_prefix}/org/preferences"
    ANNOTATIONS: str = f"{api_prefix}/annotations"
    ADMIN: str = f"{api_prefix}/admin"
    SERVICE_ACCOUNTS: str = f"{api_prefix}/serviceaccounts"
    RBAC: str = f"{api_prefix}/access-control"
    LIBRARY: str = f"{api_prefix}/library-elements"
    SSO_SETTINGS: str = f"{api_prefix}/{version_1}/sso-settings"


class RequestsMethods(Enum):
    """The class includes all necessary method values to establish an HTTP/ HTTPS connection to the Grafana API endpoints"""

    GET: str = "GET"
    PUT: str = "PUT"
    POST: str = "POST"
    PATCH: str = "PATCH"
    DELETE: str = "DELETE"


class SortDirection(Enum):
    ASC = "alpha-asc"
    DESC = "alpha-desc"


@dataclass
class APIModel:
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Args:
        host (str): Specify the host of the Grafana system
        token (str): Specify the access token of the Grafana system
        username (str): Specify the username of the Grafana system
        password (str): Specify the password of the Grafana system
        timeout (float): Specify the timeout of the Grafana system
        headers (dict): Specify the headers of the Grafana system
        http2_support (bool): Specify if you want to use HTTP/2
        ssl_context (ssl.SSLContext): Specify the custom ssl context of the Grafana system
        num_pools (int): Specify the number of the connection pool
        retries (any): Specify the number of the retries. Please use False as parameter to disable the retries
        follow_redirects (bool): Specify if redirections should be followed (default True)
    """

    host: str
    token: str = None
    username: str = None
    password: str = None
    headers: dict = None
    timeout: float = 10.0
    http2_support: bool = False
    ssl_context: ssl.SSLContext = httpx.create_ssl_context()
    num_pools: int = 10
    retries: any = 10
    follow_redirects: bool = True


@dataclass
class DatasourceQuery:
    """The class includes all necessary variables to specify a query for the datasource search endpoint

    Args:
        datasource_id (int): Specify the id of the data source
        raw_sql (str): Specify the raw SQL string to search inside the Grafana system
        ref_id (str): Specify a reference id of the search command (default A)
        interval_ms (int): Specify the time interval in milliseconds of output format (default 1000)
        max_data_points (int): Specify maximum amount of data points that dashboard panel can render (default 100)
        output_format (str): Specify the output format of the query (default time_series)
    """

    datasource_id: int
    raw_sql: str
    ref_id: str = "A"
    interval_ms: int = 1000
    max_data_points: int = 100
    output_format: str = "time_series"


@dataclass
class DatasourceRuleQuery:
    """The class includes all necessary variables to specify a query for the datasource rule search endpoint

    Args:
        datasource_uid (str): Specify the uid of the data source
        model (dict): Specify the model of the search command
        query_type (str): Specify the query time of the search command
        ref_id (str): Specify a reference id of the search command
        relative_time_range (dict): Specify the related time range of the search command
    """

    datasource_uid: str
    model: dict
    query_type: str
    ref_id: str
    relative_time_range: dict


@dataclass
class DatasourcePermission:
    """The class includes the necessary variables to generate a datasource permission object that is necessary to communicate with the Grafana datasource permissions endpoint

    Args:
        permission (Union[str, None]): Specify the datasource permission. Can be query, edit, admin or None. To remove a permission, set the permission value to None

    Raises:
        ValueError: Missed specifying a necessary value

    Returns:
        permission (str): Returns the datasource permission
    """

    def __init__(self, permission: Union[str, None]):
        if permission is None:
            self.permission: str = ""
        elif permission.lower() == "query":
            self.permission: str = "Query"
        elif permission.lower() == "edit":
            self.permission: str = "Edit"
        elif permission.lower() == "admin":
            self.permission: str = "Admin"
        else:
            raise ValueError


@dataclass
class Alert:
    """The class includes all necessary variables to generate an alert object that is necessary to communicate with the Grafana alert endpoint

    Args:
        starts_at (str): Specify the start date of the alert
        ends_at (str): Specify end date of the alert
        annotations (dict): Specify the annotations of the alert
        generator_url (str):  Specify the url of the generator endpoint
        labels (dict): Specify labels of the alert
    """

    starts_at: str
    ends_at: str
    annotations: dict
    generator_url: str
    labels: dict


@dataclass
class AlertRuleQueryModelCondition:
    """The class includes all necessary variables to generate an alert rule query model condition object that is necessary to communicate with the Grafana alert provisioning endpoint
    Args:
        evaluator_params (list): Specify the evaluator parameters
        evaluator_type (str): Specify the evaluator type
        operator_type (str): Specify the operator type
        query_params (list): Specify the query parameters
        reducer_params (list): Specify the reducer parameters
        reducer_type (str): Specify the reducer type
        type (str): Specify the type
    """

    evaluator_params: list
    evaluator_type: str
    operator_type: str
    query_params: list
    reducer_params: list
    reducer_type: str
    type: str


@dataclass
class AlertRuleQueryModel:
    """The class includes all necessary variables to generate an alert rule query model object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        conditions (list): Specify the conditions list based on the AlertRuleQueryModelCondition objects
        datasource (dict): Specify the datasource dictionary
        expression (str): Specify the expression string
        hide (bool): Specify the if the query should be hided
        interval_ms (int): Specify the interval in ms
        max_data_points (int): Specify the max data points
        ref_id (str): Specify the unique identifier of the alert rule query model
        type (str): Specify the corresponding type
    """

    conditions: List[AlertRuleQueryModelCondition]
    datasource: dict
    expression: str
    hide: bool
    interval_ms: int
    max_data_points: int
    ref_id: str
    type: str


@dataclass
class AlertQuery:
    """The class includes all necessary variables to generate an alert query object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        datasource_uid (str): Specify the datasource uid
        model (AlertRuleQueryModel): Specify the model as AlertRuleQueryModel
        query_type (str): Specify the query type
        ref_id (str): Specify the unique identifier of the alert query
        relative_time_range_from (int): Specify the relative from time range
        relative_time_range_to (int): Specify the relative to time range
    """

    datasource_uid: str
    model: AlertRuleQueryModel
    query_type: str
    ref_id: str
    relative_time_range_from: int
    relative_time_range_to: int


@dataclass
class AlertRule:
    """The class includes all necessary variables to generate an alert rule object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        condition (str): Specify the condition
        data (list): Specify the data as AlertQuery list
        exec_err_state (str): Specify the execution error state
        folder_uid (str): Specify the folder uid
        no_data_state (str): Specify the no data state
        org_id (int): Specify the org id
        rule_group (str):  Specify the rule group of the alert rule
        title (str): Specify the title of the alert rule
        uid (str): Specify the uid of the alert rule
        for_time (int): Specify the for duration as integer
        annotations (dict): Specify the annotations dictionary (default None)
        updated (str): Specify the updated date time as string (default None)
        provenance (str): Specify the provenance (default None)
        id (int): Specify the alert rule id (default 0)
        labels (dict): Specify the labels as dictionary (default None)
    """

    condition: str
    data: List[AlertQuery]
    exec_err_state: str
    folder_uid: str
    no_data_state: str
    org_id: int
    rule_group: str
    title: str
    uid: str
    for_time: str
    annotations: dict = None
    updated: str = None
    provenance: str = None
    id: int = 0
    labels: dict = None


@dataclass
class EmbeddedContactPoint:
    """The class includes all necessary variables to generate an embedded contact point object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        name (str): Specify the name of the embedded contact point
        type (str): Specify the type of the embedded contact point
        settings (dict): Specify the settings of the embedded contact point
        disable_resolve_message (bool): Specify if the resolve message should be disabled (default None)
        provenance (str): Specify the provenance (default None)
        uid (str): Specify the uid of the embedded contact point (default None)
    """

    name: str
    type: str
    settings: dict
    disable_resolve_message: bool = None
    provenance: str = None
    uid: str = None


class MatchType(Enum):
    """The class includes all necessary values to set the corresponding match type"""

    MatchEqual: int = 0
    MatchNotEqual: int = 1
    MatchRegexp: int = 2
    MatchNotRegexp: int = 3


@dataclass
class Matcher:
    """The class includes all necessary variables to generate an alert rule route matcher object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        name (str): Specify the name of the matcher
        type (MatchType): Specify the type of the matcher
        value (str): Specify the value of the matcher
    """

    name: str
    type: MatchType
    value: str


@dataclass
class Route:
    """The class includes all necessary variables to generate an alert rule route that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        continue_parameter (bool): Specify the continue parameter
        group_by_str (List[str]): Specify the list of group by strings
        receiver (str): Specify the receiver
        provenance (str): Specify the provenance
        object_matchers (List[Matcher]):  Specify the list of object matchers (default None)
        group_interval (str): Specify the group time interval (default None)
        group_wait (str): Specify the group wait time (default None)
        repeat_interval (str): Specify the repeat interval (default None)
        routes (List[Route]): Specify the list of routes (default None)
        mute_time_intervals (List[str]): Specify the mute time interval as list (default None)
    """

    continue_parameter: bool
    group_by_str: List[str]
    receiver: str
    provenance: str
    object_matchers: List[Matcher] = None
    group_interval: str = None
    group_wait: str = None
    repeat_interval: str = None
    routes: List[Self] = None
    mute_time_intervals: List[str] = None


@dataclass
class TimeRange:
    """The class includes all necessary variables to generate a time range object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        start_time (str): Specify the start time e.g. 14:00
        start_time (str): Specify the end time e.g. 15:00
    """

    start_time: str
    end_time: str


@dataclass
class TimeInterval:
    """The class includes all necessary variables to generate a time interval object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        days_of_month (List[str]): Specify the days of month list (default None)
        months (List[str]):  Specify the months list (default None)
        times (TimeRange):  Specify the times list (default None)
        weekdays (List[str]):  Specify the weekdays list (default None)
        years (List[str]):  Specify the year range list (default None)
    """

    days_of_month: List[str] = None
    months: List[str] = None
    times: List[TimeRange] = None
    weekdays: List[str] = None
    years: List[str] = None


@dataclass
class MuteTimeInterval:
    """The class includes all necessary variables to generate a mute time interval object that is necessary to communicate with the Grafana alert provisioning endpoint

    Args:
        name (str): Specify the name of the mute time interval.
        time_intervals (List[TimeInterval]): Specify the list of time interval objects
    """

    name: str = None
    time_intervals: List[TimeInterval] = None


@dataclass
class Silence:
    """The class includes all necessary variables to generate a silence object that is necessary to communicate with the Grafana silence endpoint

    Args:
        starts_at (str): Specify the start date of the silence
        created_by (str): Specify the name of the silence creator
        ends_at (str): Specify end date of the silence
        comment (str):  Specify a custom comment for the silence
        id (str): Specify an id for the silence
        matchers (dict): Specify matchers for the silence
    """

    starts_at: str
    created_by: str
    ends_at: str
    comment: str
    id: str
    matchers: dict


@dataclass
class AlertmanagerConfig:
    """The class includes all necessary variables to generate an Alertmanager config object that is necessary to communicate and set up the Grafana Alertmanager endpoint

    Args:
        global_config (Union[dict, None]): Specify the global config of the Alertmanager
        inhibit_rules (Union[list, None]): Specify the inhibit rules of the Alertmanager
        mute_time_intervals (Union[list, None]): Specify the mute time intervals of the Alertmanager
        receivers (list):  Specify the receiver's of the Alertmanager
        route (dict): Specify the route of the Alertmanager
        templates (Union[list, None]): Specify an Alertmanager template
    """

    global_config: Union[dict, None]
    inhibit_rules: Union[list, None]
    mute_time_intervals: Union[list, None]
    receivers: list
    route: dict
    templates: Union[list, None]


@dataclass
class AlertmanagerReceivers:
    """The class includes all necessary variables to generate an Alertmanager receiver's object that is necessary to communicate and set up the Grafana Alertmanager receivers endpoint

    Args:
        name (str): Specify the name of the receiver
        email_configs (Union[list, None]): Specify the email configuration of the receiver's
        grafana_managed_receiver_configs (list): Specify the Grafana managed receiver configuration of the receiver's
        opsgenie_configs (Union[list, None]):  Specify the ops genie configuration of the receiver's
        pagerduty_configs (Union[list, None]): Specify the pager duty configuration of the receiver's
        pushover_configs (Union[list, None]): Specify the push over configuration of the receiver's
        slack_configs (Union[list, None]): Specify the Slack configuration of the receiver's
        sns_configs (Union[list, None]): Specify the SNS configuration of the receiver's
        victorops_configs (Union[list, None]): Specify the victor ops configuration of the receiver's
        webhook_configs (Union[list, None]): Specify the webhook configuration of the receiver's
        wechat_configs (Union[list, None]): Specify the wechaty configuration of the receiver's
    """

    name: str
    email_configs: Union[list, None]
    grafana_managed_receiver_configs: list
    opsgenie_configs: Union[list, None]
    pagerduty_configs: Union[list, None]
    pushover_configs: Union[list, None]
    slack_configs: Union[list, None]
    sns_configs: Union[list, None]
    victorops_configs: Union[list, None]
    webhook_configs: Union[list, None]
    wechat_configs: Union[list, None]


@dataclass
class RulerRule:
    """The class includes all necessary variables to generate a Ruler rule object that is necessary to communicate and set up a Grafana Ruler rule

    Args:
        alert (str): Specify the name of the rule
        annotations (dict): Specify the annotations of the rule
        expr (str): Specify the expression of the rule
        grafana_alert (dict):  Specify the Grafana alert of the rule
        labels (dict): Specify labels of the rule
        record (str): Specify recode value of the rule
        for_id (int): Specify the id of the rule if you update an existing rule (default 0)
    """

    alert: str
    annotations: dict
    expr: str
    grafana_alert: dict
    labels: dict
    record: str
    for_id: int = 0


@dataclass
class UserObject:
    """The class includes all necessary variables to generate a User object that is necessary to update a Grafana User

    Args:
        email (str): Specify the name of the rule
        name (str): Specify the annotations of the rule
        login (str): Specify the expression of the rule
        theme (str):  Specify the Grafana alert of the rule
    """

    email: str
    name: str
    login: str
    theme: str


@dataclass
class PlaylistObject:
    """The class includes all necessary variables to generate a playlist object

    Args:
        name (str): Specify the name of the playlist
        interval (str): Specify the interval of the playlist
        items (list): Specify a list of PlaylistItemObjects
    """

    name: str
    interval: str
    items: list


@dataclass
class PlaylistItemObject:
    """The class includes all necessary variables to generate a playlist item object that is necessary to update a playlist

    Args:
        type (str): Specify the type of the playlist item
        value (str): Specify the value of the playlist item
        order (int): Specify the order of the playlist item
        title (str): Specify the title of the playlist item
    """

    type: str
    value: str
    order: int
    title: str


@dataclass
class TeamObject:
    """The class includes all necessary variables to generate a team object that is necessary to create a team

    Args:
        name (str): Specify the name of the team
        email (str): Specify the email of the team
        org_id (int): Specify the org_id of the team
    """

    name: str
    email: str
    org_id: int


@dataclass
class QueryDatasourceObject:
    """The class includes all necessary variables to generate a query datasource object that is necessary to create a query history object

    Args:
        type (str): Specify the type of the datasource query
        uid (str): Specify the uid of the datasource query
    """

    type: str
    uid: str


@dataclass
class QueryObject:
    """The class includes all necessary variables to generate a query object that is necessary to create a query history

    Args:
        ref_id (str): Specify the ref_id of the query history
        key (str): Specify the key of the query history
        scenario_id (str): Specify the scenario_id of the query history
        datasource (QueryDatasourceObject): Specify the datasource of the type QueryDatasourceObject
    """

    ref_id: str
    key: str
    scenario_id: str
    datasource: QueryDatasourceObject


@dataclass
class CorrelationObject:
    """The class includes all necessary variables to generate a find annotation object

    Args:
        source_datasource_uid (str): Specify the source datasource uid (default None)
        target_datasource_uid (str): Specify the target datasource uid (default None)
        label (str): Specify the label (default 100)
        description (str): Specify the description (default None)
        config_type (str): Specify the config type (default None)
        config_field (str): Specify the config field (default None)
        config_target (str): Specify the config target (default None)
    """

    source_datasource_uid: str = None
    target_datasource_uid: str = None
    label: str = None
    description: str = None
    config_type: str = None
    config_field: str = None
    config_target: dict = field(default_factory=dict)


@dataclass
class FindAnnotationObject:
    """The class includes all necessary variables to generate a find annotation object

    Args:
        from_value (int): Specify the optional from value (default None)
        to_value (int): Specify the optional to value (default None)
        limit (int): Specify the optional limit (default 100)
        alert_id (int): Specify the optional alert id (default None)
        dashboard_id (int): Specify the optional dashboard id (default None)
        panel_id (int): Specify the optional panel_id (default None)
        user_id (int): Specify the optional user id (default None)
        type (str): Specify the optional type e.g. alert or annotation (default None)
        tags (list): Specify the optional tags (default None)
    """

    from_value: int = None
    to_value: int = None
    limit: int = 100
    alert_id: int = None
    dashboard_id: int = None
    panel_id: int = None
    user_id: int = None
    type: str = None
    tags: list = None


@dataclass
class AnnotationObject:
    """The class includes all necessary variables to generate an annotation object

    Args:
        time (int): Specify the time as number in milliseconds
        time_end (int): Specify the end time as number in milliseconds
        tags (list): Specify the organization annotation tags from a data source that are not connected specifically to a dashboard or panel
        text (str): Specify the annotation description message
        dashboard_uid (str): Specify the optional dashboard_uid (default None)
        panel_id (int): Specify the optional panel_id (default None)
    """

    time: int
    time_end: int
    tags: list
    text: str
    dashboard_uid: str = None
    panel_id: int = None


@dataclass
class AnnotationGraphiteObject:
    """The class includes all necessary variables to generate a Graphite annotation object

    Args:
        what (str): Specify the event of the annotation
        tags (list): Specify the organization annotation tags from a data source that are not connected specifically to a dashboard or panel
        when (int): Specify the optional time as number in milliseconds
        data (str): Specify the optional annotation description message
    """

    what: str
    tags: list
    when: int = None
    data: str = None


@dataclass
class GlobalUser:
    """The class includes all necessary variables to generate a global user object

    Args:
        name (str): Specify the name of the user
        email (str): Specify the email of the user
        login (str): Specify the login type of the user
        password (str): Specify the password of the user
        org_id (int): Specify the optional org id of the user (default None)
    """

    name: str
    email: str
    login: str
    password: str
    org_id: int = None


@dataclass
class RolePermission:
    """The class includes all necessary variables to generate a role permission object

    Args:
        action (str): Specify the custom role action definition
        scope (str): Specify the scope definition. If not present, no scope will be mapped to the permission (default None)
    """

    action: str
    scope: str = None


@dataclass
class CustomRole:
    """The class includes all necessary variables to generate a custom role object

    Args:
        name (str): Specify the name of the role
        uid (str): Specify the optional uid of the role (default None)
        global_role (bool): Specify the if the role is global or not. If set to False, the default org id of the authenticated user will be used from the request (default False)
        version (int): Specify the optional version of the role (default None)
        description (str): Specify the optional description of the role (default None)
        display_name (str): Specify the optional display_name of the role (default None)
        group (str): Specify the optional org group of the role (default None)
        hidden (bool): Specify whether the role is hidden or not.  If set to True, then the role does not show in the role picker. It will not be listed by API endpoints unless explicitly specified (default False)
        permissions (list): Specify the optional permissions of the role as a list of the RolePermission objects (default None)
    """

    name: str
    uid: str = None
    global_role: bool = False
    version: int = None
    description: str = None
    display_name: str = None
    group: str = None
    hidden: bool = False
    permissions: List[RolePermission] = None


@dataclass
class DatasourceCache:
    """The class includes all necessary variables to generate a datasource cache object

    Args:
        datasource_id (int): Specify the datasource id
        datasource_uid (str): Specify the datasource uid
        enabled (bool): Specify if caching should be enabled for the datasource
        use_default_ttl (bool): Specify if the configured default TTL (Time-To-Live) should be used for both query and resource caching, instead of the user-specified values
        ttl_queries_ms (int): Specify the TTL to use for query caching, in milliseconds
        ttl_resources_ms (int): Specify the TTL to use for resource caching, in milliseconds
    """

    datasource_id: int
    datasource_uid: str
    enabled: bool
    use_default_ttl: bool
    ttl_queries_ms: int
    ttl_resources_ms: int


@dataclass
class PublicDashboard:
    """The class includes all necessary variables to generate a public dashboard object

    Args:
        uid (str): Specify the optional unique identifier when creating a public dashboard. If it’s none, it will generate a new uid (default None)
        access_token (str): Specify the optional unique access token. If it’s none, it will generate a new access token (default None)
        time_selection_enabled (bool): Specify the optional enablement of the time picker inside the public dashboard (default False)
        is_enabled (bool): Specify the optional enablement of the public dashboard (default False)
        annotations_enabled (bool): Specify the optional enablement of the annotations inside the public dashboard (default False)
        share (str): Specify the optional share mode of the public dashboard (default public)
    """

    uid: str = None
    access_token: str = None
    time_selection_enabled: bool = False
    is_enabled: bool = False
    annotations_enabled: bool = False
    share: str = "public"


@dataclass
class SSOSetting:
    """The class includes all necessary variables to generate an SSO setting object

    Args:
        api_url (str): Specify the SSO api url
        client_id (str): Specify the SSO client id
        client_secret (str): Specify the SSO client secret
        enabled (bool): Specify if the SSO provider is enabled or not
        scopes (str): Specify the SSO scopes
    """

    api_url: str
    client_id: str
    client_secret: str
    enabled: bool
    scopes: str


@dataclass
class DashboardSchema:
    """The class includes all necessary variables to generate a dashboard schema object that is used for the reporting functionality

    Args:
        dashboard_uid (str): Specify the dashboard uid
        time_range_from (str): Specify the dashboard time range from
        time_range_to (str): Specify the dashboard time range to
        report_variables (dict): Specify the key-value pairs containing the template variables for this report, in dict format. If the value is None, the template variables from the reports dashboard will be used (default None)
    """

    dashboard_uid: str
    time_range_from: str
    time_range_to: str
    report_variables: dict = None


@dataclass
class Report:
    """The class includes all necessary variables to generate a report object

    Args:
        name (str): Specify the name of the report that is used as an email subject
        recipients (str): Specify the comma-separated list of emails to which to send the report to
        reply_to (str): Specify the comma-separated list of emails used in a reply-to field of the report email
        message (str): Specify the text message used for the body of the report email
        start_date (str): Specify the distribution starts from this date
        end_date (str): Specify the distribution end from this date
        time_zone (str): Specify the time zone used to schedule report execution
        orientation (str): Specify if the orientation should be portrait or landscape
        layout (str): Specify if the layout should be grid or simple
        enable_dashboard_url (str): Specify if the dashboard url should be added to the bottom of the report email
        dashboards (List[DashboardSchema]): Specify the dashboards for which the reports should be generated
        frequency (str): Specify how often the report should be sent. Can be once, hourly, daily, weekly, monthly, last or custom. The value last schedules the report for the last day of the month. The value custom schedules the report to be sent on a custom interval. It requires interval_frequency and interval_amount to be specified e.g. every 2 weeks, where 2 is an interval_amount and weeks is an interval_frequency (default last)
        interval_frequency (str): Specify the type of the custom interval hours, days, weeks, months (default None)
        interval_amount (int): Specify the interval amount of the custom type (default 0)
        workdays_only (bool): Specify if the report only on Monday-Friday should be sent. Applicable to hourly and daily types of schedule (default None)
        formats (List[str]): Specify what kind of attachment to generate for the report. Available report formats are csv, pdf and image. The type csv attaches a CSV file for each table panel and the type image embeds an image of a dashboard into the emails body (default List["pdf"])
    """

    name: str
    recipients: str
    reply_to: str
    message: str
    start_date: str
    end_date: str
    time_zone: str
    orientation: str
    layout: str
    enable_dashboard_url: bool
    dashboards: List[DashboardSchema]
    frequency: str = "last"
    interval_frequency: str = None
    interval_amount: int = 0
    workdays_only: bool = None
    formats: List[str] = field(default_factory=lambda: ["pdf"])


@dataclass
class ReportBrandingSettings:
    """The class includes all necessary variables to generate a report branding settings object

    Args:
        report_logo_url (str): Specify the url of an image used as a logo on every page of the report
        email_logo_url (str): Specify the url of an image used as a logo in the email
        email_footer_mode (str): Specify the email footer mode. Can be sent-by or none. The value sent-by adds a 'Sent by email footer text' footer link to the email. Requires specifying values in the email_footer_text and email_footer_link fields. The value none suppresses adding a 'Sent by' footer link to the email
        email_footer_text (str): Specify the text of a URL added to the email 'Sent by' footer (default None)
        email_footer_link (str): Specify the url address value added to the email 'Sent by' footer (default None)
    """

    report_logo_url: str
    email_logo_url: str
    email_footer_mode: str
    email_footer_text: str = None
    email_footer_link: str = None
