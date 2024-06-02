# Table of Contents

* [model](#model)
  * [APIEndpoints](#model.APIEndpoints)
  * [RequestsMethods](#model.RequestsMethods)
  * [APIModel](#model.APIModel)
  * [DatasourceQuery](#model.DatasourceQuery)
  * [DatasourceRuleQuery](#model.DatasourceRuleQuery)
  * [Alert](#model.Alert)
  * [AlertRuleQueryModelCondition](#model.AlertRuleQueryModelCondition)
  * [AlertRuleQueryModel](#model.AlertRuleQueryModel)
  * [AlertQuery](#model.AlertQuery)
  * [AlertRule](#model.AlertRule)
  * [EmbeddedContactPoint](#model.EmbeddedContactPoint)
  * [MatchType](#model.MatchType)
  * [Matcher](#model.Matcher)
  * [Route](#model.Route)
  * [TimeRange](#model.TimeRange)
  * [TimeInterval](#model.TimeInterval)
  * [MuteTimeInterval](#model.MuteTimeInterval)
  * [Silence](#model.Silence)
  * [AlertmanagerConfig](#model.AlertmanagerConfig)
  * [AlertmanagerReceivers](#model.AlertmanagerReceivers)
  * [RulerRule](#model.RulerRule)
  * [UserObject](#model.UserObject)
  * [PlaylistObject](#model.PlaylistObject)
  * [PlaylistItemObject](#model.PlaylistItemObject)
  * [TeamObject](#model.TeamObject)
  * [QueryDatasourceObject](#model.QueryDatasourceObject)
  * [QueryObject](#model.QueryObject)
  * [CorrelationObject](#model.CorrelationObject)
  * [FindAnnotationObject](#model.FindAnnotationObject)
  * [AnnotationObject](#model.AnnotationObject)
  * [AnnotationGraphiteObject](#model.AnnotationGraphiteObject)
  * [GlobalUser](#model.GlobalUser)
  * [RolePermission](#model.RolePermission)
  * [CustomRole](#model.CustomRole)
  * [DatasourceCache](#model.DatasourceCache)
  * [PublicDashboard](#model.PublicDashboard)
  * [SSOSetting](#model.SSOSetting)
  * [DashboardSchema](#model.DashboardSchema)
  * [Report](#model.Report)
  * [ReportBrandingSettings](#model.ReportBrandingSettings)

<a id="model"></a>

# model

<a id="model.APIEndpoints"></a>

## APIEndpoints Objects

```python
class APIEndpoints(Enum)
```

The class includes all necessary API endpoint strings to connect the Grafana API

<a id="model.RequestsMethods"></a>

## RequestsMethods Objects

```python
class RequestsMethods(Enum)
```

The class includes all necessary method values to establish an HTTP/ HTTPS connection to the Grafana API endpoints

<a id="model.APIModel"></a>

## APIModel Objects

```python
@dataclass
class APIModel()
```

The class includes all necessary variables to establish a connection to the Grafana API endpoints

**Arguments**:

- `host` _str_ - Specify the host of the Grafana system
- `token` _str_ - Specify the access token of the Grafana system
- `username` _str_ - Specify the username of the Grafana system
- `password` _str_ - Specify the password of the Grafana system
- `timeout` _float_ - Specify the timeout of the Grafana system
- `http2_support` _bool_ - Specify if you want to use HTTP/2
- `ssl_context` _ssl.SSLContext_ - Specify the custom ssl context of the Grafana system
- `num_pools` _int_ - Specify the number of the connection pool
- `retries` _any_ - Specify the number of the retries. Please use False as parameter to disable the retries

<a id="model.DatasourceQuery"></a>

## DatasourceQuery Objects

```python
@dataclass
class DatasourceQuery()
```

The class includes all necessary variables to specify a query for the datasource search endpoint

**Arguments**:

- `datasource_id` _int_ - Specify the id of the data source
- `raw_sql` _str_ - Specify the raw SQL string to search inside the Grafana system
- `ref_id` _str_ - Specify a reference id of the search command (default A)
- `interval_ms` _int_ - Specify the time interval in milliseconds of output format (default 1000)
- `max_data_points` _int_ - Specify maximum amount of data points that dashboard panel can render (default 100)
- `output_format` _str_ - Specify the output format of the query (default time_series)

<a id="model.DatasourceRuleQuery"></a>

## DatasourceRuleQuery Objects

```python
@dataclass
class DatasourceRuleQuery()
```

The class includes all necessary variables to specify a query for the datasource rule search endpoint

**Arguments**:

- `datasource_uid` _str_ - Specify the uid of the data source
- `model` _dict_ - Specify the model of the search command
- `query_type` _str_ - Specify the query time of the search command
- `ref_id` _str_ - Specify a reference id of the search command
- `relative_time_range` _dict_ - Specify the related time range of the search command

<a id="model.Alert"></a>

## Alert Objects

```python
@dataclass
class Alert()
```

The class includes all necessary variables to generate an alert object that is necessary to communicate with the Grafana alert endpoint

**Arguments**:

- `starts_at` _str_ - Specify the start date of the alert
- `ends_at` _str_ - Specify end date of the alert
- `annotations` _dict_ - Specify the annotations of the alert
- `generator_url` _str_ - Specify the url of the generator endpoint
- `labels` _dict_ - Specify labels of the alert

<a id="model.AlertRuleQueryModelCondition"></a>

## AlertRuleQueryModelCondition Objects

```python
@dataclass
class AlertRuleQueryModelCondition()
```

The class includes all necessary variables to generate an alert rule query model condition object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `evaluator_params` _list_ - Specify the evaluator parameters
- `evaluator_type` _str_ - Specify the evaluator type
- `operator_type` _str_ - Specify the operator type
- `query_params` _list_ - Specify the query parameters
- `reducer_params` _list_ - Specify the reducer parameters
- `reducer_type` _str_ - Specify the reducer type
- `type` _str_ - Specify the type

<a id="model.AlertRuleQueryModel"></a>

## AlertRuleQueryModel Objects

```python
@dataclass
class AlertRuleQueryModel()
```

The class includes all necessary variables to generate an alert rule query model object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `conditions` _list_ - Specify the conditions list based on the AlertRuleQueryModelCondition objects
- `datasource` _dict_ - Specify the datasource dictionary
- `expression` _str_ - Specify the expression string
- `hide` _bool_ - Specify the if the query should be hided
- `interval_ms` _int_ - Specify the interval in ms
- `max_data_points` _int_ - Specify the max data points
- `ref_id` _str_ - Specify the unique identifier of the alert rule query model
- `type` _str_ - Specify the corresponding type

<a id="model.AlertQuery"></a>

## AlertQuery Objects

```python
@dataclass
class AlertQuery()
```

The class includes all necessary variables to generate an alert query object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid
- `model` _AlertRuleQueryModel_ - Specify the model as AlertRuleQueryModel
- `query_type` _str_ - Specify the query type
- `ref_id` _str_ - Specify the unique identifier of the alert query
- `relative_time_range_from` _int_ - Specify the relative from time range
- `relative_time_range_to` _int_ - Specify the relative to time range

<a id="model.AlertRule"></a>

## AlertRule Objects

```python
@dataclass
class AlertRule()
```

The class includes all necessary variables to generate an alert rule object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `condition` _str_ - Specify the condition
- `data` _list_ - Specify the data as AlertQuery list
- `exec_err_state` _str_ - Specify the execution error state
- `folder_uid` _str_ - Specify the folder uid
- `no_data_state` _str_ - Specify the no data state
- `org_id` _int_ - Specify the org id
- `rule_group` _str_ - Specify the rule group of the alert rule
- `title` _str_ - Specify the title of the alert rule
- `uid` _str_ - Specify the uid of the alert rule
- `for_time` _int_ - Specify the for duration as integer
- `annotations` _dict_ - Specify the annotations dictionary (default None)
- `updated` _str_ - Specify the updated date time as string (default None)
- `provenance` _str_ - Specify the provenance (default None)
- `id` _int_ - Specify the alert rule id (default 0)
- `labels` _dict_ - Specify the labels as dictionary (default None)

<a id="model.EmbeddedContactPoint"></a>

## EmbeddedContactPoint Objects

```python
@dataclass
class EmbeddedContactPoint()
```

The class includes all necessary variables to generate an embedded contact point object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `name` _str_ - Specify the name of the embedded contact point
- `type` _str_ - Specify the type of the embedded contact point
- `settings` _dict_ - Specify the settings of the embedded contact point
- `disable_resolve_message` _bool_ - Specify if the resolve message should be disabled (default None)
- `provenance` _str_ - Specify the provenance (default None)
- `uid` _str_ - Specify the uid of the embedded contact point (default None)

<a id="model.MatchType"></a>

## MatchType Objects

```python
class MatchType(Enum)
```

The class includes all necessary values to set the corresponding match type

<a id="model.Matcher"></a>

## Matcher Objects

```python
@dataclass
class Matcher()
```

The class includes all necessary variables to generate an alert rule route matcher object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `name` _str_ - Specify the name of the matcher
- `type` _MatchType_ - Specify the type of the matcher
- `value` _str_ - Specify the value of the matcher

<a id="model.Route"></a>

## Route Objects

```python
@dataclass
class Route()
```

The class includes all necessary variables to generate an alert rule route that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `continue_parameter` _bool_ - Specify the continue parameter
- `group_by_str` _List[str]_ - Specify the list of group by strings
- `receiver` _str_ - Specify the receiver
- `provenance` _str_ - Specify the provenance
- `object_matchers` _List[Matcher]_ - Specify the list of object matchers (default None)
- `group_interval` _str_ - Specify the group time interval (default None)
- `group_wait` _str_ - Specify the group wait time (default None)
- `repeat_interval` _str_ - Specify the repeat interval (default None)
- `routes` _List[Route]_ - Specify the list of routes (default None)
- `mute_time_intervals` _List[str]_ - Specify the mute time interval as list (default None)

<a id="model.TimeRange"></a>

## TimeRange Objects

```python
@dataclass
class TimeRange()
```

The class includes all necessary variables to generate a time range object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `start_time` _str_ - Specify the start time e.g. 14:00
- `start_time` _str_ - Specify the end time e.g. 15:00

<a id="model.TimeInterval"></a>

## TimeInterval Objects

```python
@dataclass
class TimeInterval()
```

The class includes all necessary variables to generate a time interval object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `days_of_month` _List[str]_ - Specify the days of month list (default None)
- `months` _List[str]_ - Specify the months list (default None)
- `times` _TimeRange_ - Specify the times list (default None)
- `weekdays` _List[str]_ - Specify the weekdays list (default None)
- `years` _List[str]_ - Specify the year range list (default None)

<a id="model.MuteTimeInterval"></a>

## MuteTimeInterval Objects

```python
@dataclass
class MuteTimeInterval()
```

The class includes all necessary variables to generate a mute time interval object that is necessary to communicate with the Grafana alert provisioning endpoint

**Arguments**:

- `name` _str_ - Specify the name of the mute time interval.
- `time_intervals` _List[TimeInterval]_ - Specify the list of time interval objects

<a id="model.Silence"></a>

## Silence Objects

```python
@dataclass
class Silence()
```

The class includes all necessary variables to generate a silence object that is necessary to communicate with the Grafana silence endpoint

**Arguments**:

- `starts_at` _str_ - Specify the start date of the silence
- `created_by` _str_ - Specify the name of the silence creator
- `ends_at` _str_ - Specify end date of the silence
- `comment` _str_ - Specify a custom comment for the silence
- `id` _str_ - Specify an id for the silence
- `matchers` _dict_ - Specify matchers for the silence

<a id="model.AlertmanagerConfig"></a>

## AlertmanagerConfig Objects

```python
@dataclass
class AlertmanagerConfig()
```

The class includes all necessary variables to generate an Alertmanager config object that is necessary to communicate and set up the Grafana Alertmanager endpoint

**Arguments**:

- `global_config` _dict_ - Specify the global config of the Alertmanager
- `inhibit_rules` _list_ - Specify the inhibit rules of the Alertmanager
- `mute_time_intervals` _list_ - Specify the mute time intervals of the Alertmanager
- `receivers` _list_ - Specify the receiver's of the Alertmanager
- `route` _dict_ - Specify the route of the Alertmanager
- `templates` _list_ - Specify an Alertmanager template

<a id="model.AlertmanagerReceivers"></a>

## AlertmanagerReceivers Objects

```python
@dataclass
class AlertmanagerReceivers()
```

The class includes all necessary variables to generate an Alertmanager receiver's object that is necessary to communicate and set up the Grafana Alertmanager receivers endpoint

**Arguments**:

- `name` _str_ - Specify the name of the receiver
- `email_configs` _list_ - Specify the email configuration of the receiver's
- `grafana_managed_receiver_configs` _list_ - Specify the Grafana managed receiver configuration of the receiver's
- `opsgenie_configs` _list_ - Specify the ops genie configuration of the receiver's
- `pagerduty_configs` _dict_ - Specify the pager duty configuration of the receiver's
- `pushover_configs` _list_ - Specify the push over configuration of the receiver's
- `slack_configs` _list_ - Specify the Slack configuration of the receiver's
- `victorops_configs` _list_ - Specify the victor ops configuration of the receiver's
- `webhook_configs` _list_ - Specify the webhook configuration of the receiver's
- `wechat_configs` _list_ - Specify the wechaty configuration of the receiver's

<a id="model.RulerRule"></a>

## RulerRule Objects

```python
@dataclass
class RulerRule()
```

The class includes all necessary variables to generate a Ruler rule object that is necessary to communicate and set up a Grafana Ruler rule

**Arguments**:

- `alert` _str_ - Specify the name of the rule
- `annotations` _dict_ - Specify the annotations of the rule
- `expr` _str_ - Specify the expression of the rule
- `grafana_alert` _dict_ - Specify the Grafana alert of the rule
- `labels` _dict_ - Specify labels of the rule
- `record` _str_ - Specify recode value of the rule
- `for_id` _int_ - Specify the id of the rule if you update an existing rule (default 0)

<a id="model.UserObject"></a>

## UserObject Objects

```python
@dataclass
class UserObject()
```

The class includes all necessary variables to generate a User object that is necessary to update a Grafana User

**Arguments**:

- `email` _str_ - Specify the name of the rule
- `name` _str_ - Specify the annotations of the rule
- `login` _str_ - Specify the expression of the rule
- `theme` _str_ - Specify the Grafana alert of the rule

<a id="model.PlaylistObject"></a>

## PlaylistObject Objects

```python
@dataclass
class PlaylistObject()
```

The class includes all necessary variables to generate a playlist object

**Arguments**:

- `name` _str_ - Specify the name of the playlist
- `interval` _str_ - Specify the interval of the playlist
- `items` _list_ - Specify a list of PlaylistItemObjects

<a id="model.PlaylistItemObject"></a>

## PlaylistItemObject Objects

```python
@dataclass
class PlaylistItemObject()
```

The class includes all necessary variables to generate a playlist item object that is necessary to update a playlist

**Arguments**:

- `type` _str_ - Specify the type of the playlist item
- `value` _str_ - Specify the value of the playlist item
- `order` _int_ - Specify the order of the playlist item
- `title` _str_ - Specify the title of the playlist item

<a id="model.TeamObject"></a>

## TeamObject Objects

```python
@dataclass
class TeamObject()
```

The class includes all necessary variables to generate a team object that is necessary to create a team

**Arguments**:

- `name` _str_ - Specify the name of the team
- `email` _str_ - Specify the email of the team
- `org_id` _int_ - Specify the org_id of the team

<a id="model.QueryDatasourceObject"></a>

## QueryDatasourceObject Objects

```python
@dataclass
class QueryDatasourceObject()
```

The class includes all necessary variables to generate a query datasource object that is necessary to create a query history object

**Arguments**:

- `type` _str_ - Specify the type of the datasource query
- `uid` _str_ - Specify the uid of the datasource query

<a id="model.QueryObject"></a>

## QueryObject Objects

```python
@dataclass
class QueryObject()
```

The class includes all necessary variables to generate a query object that is necessary to create a query history

**Arguments**:

- `ref_id` _str_ - Specify the ref_id of the query history
- `key` _str_ - Specify the key of the query history
- `scenario_id` _str_ - Specify the scenario_id of the query history
- `datasource` _QueryDatasourceObject_ - Specify the datasource of the type QueryDatasourceObject

<a id="model.CorrelationObject"></a>

## CorrelationObject Objects

```python
@dataclass
class CorrelationObject()
```

The class includes all necessary variables to generate a find annotation object

**Arguments**:

- `source_datasource_uid` _str_ - Specify the source datasource uid (default None)
- `target_datasource_uid` _str_ - Specify the target datasource uid (default None)
- `label` _str_ - Specify the label (default 100)
- `description` _str_ - Specify the description (default None)
- `config_type` _str_ - Specify the config type (default None)
- `config_field` _str_ - Specify the config field (default None)
- `config_target` _str_ - Specify the config target (default None)

<a id="model.FindAnnotationObject"></a>

## FindAnnotationObject Objects

```python
@dataclass
class FindAnnotationObject()
```

The class includes all necessary variables to generate a find annotation object

**Arguments**:

- `from_value` _int_ - Specify the optional from value (default None)
- `to_value` _int_ - Specify the optional to value (default None)
- `limit` _int_ - Specify the optional limit (default 100)
- `alert_id` _int_ - Specify the optional alert id (default None)
- `dashboard_id` _int_ - Specify the optional dashboard id (default None)
- `panel_id` _int_ - Specify the optional panel_id (default None)
- `user_id` _int_ - Specify the optional user id (default None)
- `type` _str_ - Specify the optional type e.g. alert or annotation (default None)
- `tags` _list_ - Specify the optional tags (default None)

<a id="model.AnnotationObject"></a>

## AnnotationObject Objects

```python
@dataclass
class AnnotationObject()
```

The class includes all necessary variables to generate an annotation object

**Arguments**:

- `time` _int_ - Specify the time as number in milliseconds
- `time_end` _int_ - Specify the end time as number in milliseconds
- `tags` _list_ - Specify the organization annotation tags from a data source that are not connected specifically to a dashboard or panel
- `text` _str_ - Specify the annotation description message
- `dashboard_uid` _str_ - Specify the optional dashboard_uid (default None)
- `panel_id` _int_ - Specify the optional panel_id (default None)

<a id="model.AnnotationGraphiteObject"></a>

## AnnotationGraphiteObject Objects

```python
@dataclass
class AnnotationGraphiteObject()
```

The class includes all necessary variables to generate a Graphite annotation object

**Arguments**:

- `what` _str_ - Specify the event of the annotation
- `tags` _list_ - Specify the organization annotation tags from a data source that are not connected specifically to a dashboard or panel
- `when` _int_ - Specify the optional time as number in milliseconds
- `data` _str_ - Specify the optional annotation description message

<a id="model.GlobalUser"></a>

## GlobalUser Objects

```python
@dataclass
class GlobalUser()
```

The class includes all necessary variables to generate a global user object

**Arguments**:

- `name` _str_ - Specify the name of the user
- `email` _str_ - Specify the email of the user
- `login` _str_ - Specify the login type of the user
- `password` _str_ - Specify the password of the user
- `org_id` _int_ - Specify the optional org id of the user (default None)

<a id="model.RolePermission"></a>

## RolePermission Objects

```python
@dataclass
class RolePermission()
```

The class includes all necessary variables to generate a role permission object

**Arguments**:

- `action` _str_ - Specify the custom role action definition
- `scope` _str_ - Specify the scope definition. If not present, no scope will be mapped to the permission (default None)

<a id="model.CustomRole"></a>

## CustomRole Objects

```python
@dataclass
class CustomRole()
```

The class includes all necessary variables to generate a custom role object

**Arguments**:

- `name` _str_ - Specify the name of the role
- `uid` _str_ - Specify the optional uid of the role (default None)
- `global_role` _bool_ - Specify the if the role is global or not. If set to False, the default org id of the authenticated user will be used from the request (default False)
- `version` _int_ - Specify the optional version of the role (default None)
- `description` _str_ - Specify the optional description of the role (default None)
- `display_name` _str_ - Specify the optional display_name of the role (default None)
- `group` _str_ - Specify the optional org group of the role (default None)
- `hidden` _bool_ - Specify whether the role is hidden or not.  If set to True, then the role does not show in the role picker. It will not be listed by API endpoints unless explicitly specified (default False)
- `permissions` _list_ - Specify the optional permissions of the role as a list of the RolePermission objects (default None)

<a id="model.DatasourceCache"></a>

## DatasourceCache Objects

```python
@dataclass
class DatasourceCache()
```

The class includes all necessary variables to generate a datasource cache object

**Arguments**:

- `datasource_id` _int_ - Specify the datasource id
- `datasource_uid` _str_ - Specify the datasource uid
- `enabled` _bool_ - Specify if caching should be enabled for the datasource
- `use_default_ttl` _bool_ - Specify if the configured default TTL (Time-To-Live) should be used for both query and resource caching, instead of the user-specified values
- `ttl_queries_ms` _int_ - Specify the TTL to use for query caching, in milliseconds
- `ttl_resources_ms` _int_ - Specify the TTL to use for resource caching, in milliseconds

<a id="model.PublicDashboard"></a>

## PublicDashboard Objects

```python
@dataclass
class PublicDashboard()
```

The class includes all necessary variables to generate a public dashboard object

**Arguments**:

- `uid` _str_ - Specify the optional unique identifier when creating a public dashboard. If it’s none, it will generate a new uid (default None)
- `access_token` _str_ - Specify the optional unique access token. If it’s none, it will generate a new access token (default None)
- `time_selection_enabled` _bool_ - Specify the optional enablement of the time picker inside the public dashboard (default False)
- `is_enabled` _bool_ - Specify the optional enablement of the public dashboard (default False)
- `annotations_enabled` _bool_ - Specify the optional enablement of the annotations inside the public dashboard (default False)
- `share` _str_ - Specify the optional share mode of the public dashboard (default public)

<a id="model.SSOSetting"></a>

## SSOSetting Objects

```python
@dataclass
class SSOSetting()
```

The class includes all necessary variables to generate an SSO setting object

**Arguments**:

- `api_url` _str_ - Specify the SSO api url
- `client_id` _str_ - Specify the SSO client id
- `client_secret` _str_ - Specify the SSO client secret
- `enabled` _bool_ - Specify if the SSO provider is enabled or not
- `scopes` _str_ - Specify the SSO scopes

<a id="model.DashboardSchema"></a>

## DashboardSchema Objects

```python
@dataclass
class DashboardSchema()
```

The class includes all necessary variables to generate a dashboard schema object that is used for the reporting functionality

**Arguments**:

- `dashboard_uid` _str_ - Specify the dashboard uid
- `time_range_from` _str_ - Specify the dashboard time range from
- `time_range_to` _str_ - Specify the dashboard time range to
- `report_variables` _dict_ - Specify the key-value pairs containing the template variables for this report, in dict format. If the value is None, the template variables from the reports dashboard will be used (default None)

<a id="model.Report"></a>

## Report Objects

```python
@dataclass
class Report()
```

The class includes all necessary variables to generate a report object

**Arguments**:

- `name` _str_ - Specify the name of the report that is used as an email subject
- `recipients` _str_ - Specify the comma-separated list of emails to which to send the report to
- `reply_to` _str_ - Specify the comma-separated list of emails used in a reply-to field of the report email
- `message` _str_ - Specify the text message used for the body of the report email
- `start_date` _str_ - Specify the distribution starts from this date
- `end_date` _str_ - Specify the distribution end from this date
- `time_zone` _str_ - Specify the time zone used to schedule report execution
- `orientation` _str_ - Specify if the orientation should be portrait or landscape
- `layout` _str_ - Specify if the layout should be grid or simple
- `enable_dashboard_url` _str_ - Specify if the dashboard url should be added to the bottom of the report email
- `dashboards` _List[DashboardSchema]_ - Specify the dashboards for which the reports should be generated
- `frequency` _str_ - Specify how often the report should be sent. Can be once, hourly, daily, weekly, monthly, last or custom. The value last schedules the report for the last day of the month. The value custom schedules the report to be sent on a custom interval. It requires interval_frequency and interval_amount to be specified e.g. every 2 weeks, where 2 is an interval_amount and weeks is an interval_frequency (default last)
- `interval_frequency` _str_ - Specify the type of the custom interval hours, days, weeks, months (default None)
- `interval_amount` _int_ - Specify the interval amount of the custom type (default 0)
- `workdays_only` _bool_ - Specify if the report only on Monday-Friday should be sent. Applicable to hourly and daily types of schedule (default None)
- `formats` _List[str]_ - Specify what kind of attachment to generate for the report. Available report formats are csv, pdf and image. The type csv attaches a CSV file for each table panel and the type image embeds an image of a dashboard into the emails body (default List["pdf"])

<a id="model.ReportBrandingSettings"></a>

## ReportBrandingSettings Objects

```python
@dataclass
class ReportBrandingSettings()
```

The class includes all necessary variables to generate a report branding settings object

**Arguments**:

- `report_logo_url` _str_ - Specify the url of an image used as a logo on every page of the report
- `email_logo_url` _str_ - Specify the url of an image used as a logo in the email
- `email_footer_mode` _str_ - Specify the email footer mode. Can be sent-by or none. The value sent-by adds a 'Sent by email footer text' footer link to the email. Requires specifying values in the email_footer_text and email_footer_link fields. The value none suppresses adding a 'Sent by' footer link to the email
- `email_footer_text` _str_ - Specify the text of a URL added to the email 'Sent by' footer (default None)
- `email_footer_link` _str_ - Specify the url address value added to the email 'Sent by' footer (default None)

