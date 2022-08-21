from enum import Enum
from typing import NamedTuple

# The constant includes all necessary error messages that can occurs, if you establish a connection to the Grafana API.
ERROR_MESSAGES: list = ["invalid API key"]


class APIEndpoints(Enum):
    """The class includes all necessary API endpoint strings to connect the Grafana API"""

    api_prefix = "/api"

    SEARCH = f"{api_prefix}/search"
    DASHBOARDS = f"{api_prefix}/dashboards"
    FOLDERS = f"{api_prefix}/folders"
    LEGACY_ALERTS = f"{api_prefix}/alerts"
    ALERT_NOTIFICATIONS = f"{api_prefix}/alert-notifications"
    ALERTS_ALERTMANAGER = f"{api_prefix}/alertmanager"
    ALERTS_PROMETHEUS = f"{api_prefix}/prometheus"
    ALERTS_RULER = f"{api_prefix}/ruler"
    ALERTS_TESTING = f"{api_prefix}/v1"
    ALERTS_NGALERT = f"{api_prefix}/v1/ngalert"
    DATASOURCES = f"{api_prefix}/datasources"
    DATASOURCE_QUERY = f"{api_prefix}/tsdb/query"
    SHORT_URLS = f"{api_prefix}/short-urls"
    ORGANISATION = f"{api_prefix}/org"
    ORGANISATIONS = f"{api_prefix}/orgs"
    USER = f"{api_prefix}/user"
    USERS = f"{api_prefix}/users"
    SNAPSHOTS = f"{api_prefix}/snapshots"
    DASHBOARD_SNAPSHOTS = f"{api_prefix}/dashboard/snapshots"
    PLAYLISTS = f"{api_prefix}/playlists"
    TEAMS = f"{api_prefix}/teams"
    QUERY_HISTORY = f"{api_prefix}/query-history"
    REPORTING = f"{api_prefix}/reports/email"
    LICENSING = f"{api_prefix}/licensing"
    FRONTEND = f"{api_prefix}/frontend"
    LOGIN = f"{api_prefix}/login"
    AUTHENTICATION = f"{api_prefix}/auth/keys"
    EXTERNAL_GROUPS = f"{api_prefix}/teams"
    USER_PREFERENCES = f"{api_prefix}/user/preferences"
    ORG_PREFERENCES = f"{api_prefix}/org/preferences"
    ANNOTATIONS = f"{api_prefix}/annotations"
    ADMIN = f"{api_prefix}/admin"
    SERVICE_ACCOUNTS = f"{api_prefix}/serviceaccounts"
    RBAC = f"{api_prefix}/access-control"


class RequestsMethods(Enum):
    """The class includes all necessary methods to establish an HTTP/ HTTPS connection to the Grafana API endpoints"""

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class APIModel(NamedTuple):
    """The class includes all necessary variables to establish a connection to the Grafana API endpoints

    Args:
        host (str): Specify the host of the Grafana system
        token (str): Specify the access token of the Grafana system
        username (str): Specify the username of the Grafana system
        password (str): Specify the password of the Grafana system
    """

    host: str
    token: str = None
    username: str = None
    password: str = None


class DatasourceQuery(NamedTuple):
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


class DatasourceRuleQuery(NamedTuple):
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


class Alert(NamedTuple):
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


class Silence(NamedTuple):
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


class AlertmanagerConfig(NamedTuple):
    """The class includes all necessary variables to generate an Alertmanager config object that is necessary to communicate and set up the Grafana Alertmanager endpoint

    Args:
        global_config (dict): Specify the global config of the Alertmanager
        inhibit_rules (list): Specify the inhibit rules of the Alertmanager
        mute_time_intervals (list): Specify the mute time intervals of the Alertmanager
        receivers (list):  Specify the receivers of the Alertmanager
        route (dict): Specify the route of the Alertmanager
        templates (list): Specify an Alertmanager template
    """

    global_config: dict
    inhibit_rules: list
    mute_time_intervals: list
    receivers: list
    route: dict
    templates: list


class AlertmanagerReceivers(NamedTuple):
    """The class includes all necessary variables to generate an Alertmanager receivers object that is necessary to communicate and set up the Grafana Alertmanager receivers endpoint

    Args:
        name (str): Specify the name of the receiver
        email_configs (list): Specify the email configuration of the receiver's
        grafana_managed_receiver_configs (list): Specify the Grafana managed receiver configuration of the receiver's
        opsgenie_configs (list):  Specify the ops genie configuration of the receiver's
        pagerduty_configs (dict): Specify the pager duty configuration of the receiver's
        pushover_configs (list): Specify the push over configuration of the receiver's
        slack_configs (list): Specify the Slack configuration of the receiver's
        victorops_configs (list): Specify the victor ops configuration of the receiver's
        webhook_configs (list): Specify the webhook configuration of the receiver's
        wechat_configs (list): Specify the wechaty configuration of the receiver's
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


class UserObject(NamedTuple):
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


class PlaylistObject(NamedTuple):
    """The class includes all necessary variables to generate a playlist object

    Args:
        name (str): Specify the name of the playlist
        interval (str): Specify the interval of the playlist
        items (list): Specify a list of PlaylistItemObjects
    """

    name: str
    interval: str
    items: list


class PlaylistItemObject(NamedTuple):
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


class TeamObject(NamedTuple):
    """The class includes all necessary variables to generate a team object that is necessary to create a team

    Args:
        name (str): Specify the name of the team
        email (str): Specify the email of the team
        org_id (int): Specify the org_id of the team
    """

    name: str
    email: str
    org_id: int


class QueryDatasourceObject(NamedTuple):
    """The class includes all necessary variables to generate a query datasource object that is necessary to create a query history object

    Args:
        type (str): Specify the type of the datasource query
        uid (str): Specify the uid of the datasource query
    """

    type: str
    uid: str


class QueryObject(NamedTuple):
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


class FindAnnotationObject(NamedTuple):
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


class AnnotationObject(NamedTuple):
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


class AnnotationGraphiteObject(NamedTuple):
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


class GlobalUser(NamedTuple):
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


class CustomRole(NamedTuple):
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
    permissions: list = None


class RolePermission(NamedTuple):
    """The class includes all necessary variables to generate a role permission object

    Args:
        action (str): Specify the custom role action definition
        scope (str): Specify the scope definition. If not present, no scope will be mapped to the permission (default None)
    """

    action: str
    scope: str = None
