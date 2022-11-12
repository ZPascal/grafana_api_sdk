# Table of Contents

* [model](#model)
  * [APIEndpoints](#model.APIEndpoints)
  * [RequestsMethods](#model.RequestsMethods)
  * [APIModel](#model.APIModel)
  * [DatasourceQuery](#model.DatasourceQuery)
  * [DatasourceRuleQuery](#model.DatasourceRuleQuery)
  * [Alert](#model.Alert)
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
  * [FindAnnotationObject](#model.FindAnnotationObject)
  * [AnnotationObject](#model.AnnotationObject)
  * [AnnotationGraphiteObject](#model.AnnotationGraphiteObject)
  * [GlobalUser](#model.GlobalUser)
  * [CustomRole](#model.CustomRole)
  * [RolePermission](#model.RolePermission)

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

The class includes all necessary methods to establish an HTTP/ HTTPS connection to the Grafana API endpoints

<a id="model.APIModel"></a>

## APIModel Objects

```python
class APIModel(NamedTuple)
```

The class includes all necessary variables to establish a connection to the Grafana API endpoints

**Arguments**:

- `host` _str_ - Specify the host of the Grafana system
- `token` _str_ - Specify the access token of the Grafana system
- `username` _str_ - Specify the username of the Grafana system
- `password` _str_ - Specify the password of the Grafana system

<a id="model.DatasourceQuery"></a>

## DatasourceQuery Objects

```python
class DatasourceQuery(NamedTuple)
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
class DatasourceRuleQuery(NamedTuple)
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
class Alert(NamedTuple)
```

The class includes all necessary variables to generate an alert object that is necessary to communicate with the Grafana alert endpoint

**Arguments**:

- `starts_at` _str_ - Specify the start date of the alert
- `ends_at` _str_ - Specify end date of the alert
- `annotations` _dict_ - Specify the annotations of the alert
- `generator_url` _str_ - Specify the url of the generator endpoint
- `labels` _dict_ - Specify labels of the alert

<a id="model.Silence"></a>

## Silence Objects

```python
class Silence(NamedTuple)
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
class AlertmanagerConfig(NamedTuple)
```

The class includes all necessary variables to generate an Alertmanager config object that is necessary to communicate and set up the Grafana Alertmanager endpoint

**Arguments**:

- `global_config` _dict_ - Specify the global config of the Alertmanager
- `inhibit_rules` _list_ - Specify the inhibit rules of the Alertmanager
- `mute_time_intervals` _list_ - Specify the mute time intervals of the Alertmanager
- `receivers` _list_ - Specify the receivers of the Alertmanager
- `route` _dict_ - Specify the route of the Alertmanager
- `templates` _list_ - Specify an Alertmanager template

<a id="model.AlertmanagerReceivers"></a>

## AlertmanagerReceivers Objects

```python
class AlertmanagerReceivers(NamedTuple)
```

The class includes all necessary variables to generate an Alertmanager receivers object that is necessary to communicate and set up the Grafana Alertmanager receivers endpoint

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
class RulerRule(NamedTuple)
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
class UserObject(NamedTuple)
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
class PlaylistObject(NamedTuple)
```

The class includes all necessary variables to generate a playlist object

**Arguments**:

- `name` _str_ - Specify the name of the playlist
- `interval` _str_ - Specify the interval of the playlist
- `items` _list_ - Specify a list of PlaylistItemObjects

<a id="model.PlaylistItemObject"></a>

## PlaylistItemObject Objects

```python
class PlaylistItemObject(NamedTuple)
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
class TeamObject(NamedTuple)
```

The class includes all necessary variables to generate a team object that is necessary to create a team

**Arguments**:

- `name` _str_ - Specify the name of the team
- `email` _str_ - Specify the email of the team
- `org_id` _int_ - Specify the org_id of the team

<a id="model.QueryDatasourceObject"></a>

## QueryDatasourceObject Objects

```python
class QueryDatasourceObject(NamedTuple)
```

The class includes all necessary variables to generate a query datasource object that is necessary to create a query history object

**Arguments**:

- `type` _str_ - Specify the type of the datasource query
- `uid` _str_ - Specify the uid of the datasource query

<a id="model.QueryObject"></a>

## QueryObject Objects

```python
class QueryObject(NamedTuple)
```

The class includes all necessary variables to generate a query object that is necessary to create a query history

**Arguments**:

- `ref_id` _str_ - Specify the ref_id of the query history
- `key` _str_ - Specify the key of the query history
- `scenario_id` _str_ - Specify the scenario_id of the query history
- `datasource` _QueryDatasourceObject_ - Specify the datasource of the type QueryDatasourceObject

<a id="model.FindAnnotationObject"></a>

## FindAnnotationObject Objects

```python
class FindAnnotationObject(NamedTuple)
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
class AnnotationObject(NamedTuple)
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
class AnnotationGraphiteObject(NamedTuple)
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
class GlobalUser(NamedTuple)
```

The class includes all necessary variables to generate a global user object

**Arguments**:

- `name` _str_ - Specify the name of the user
- `email` _str_ - Specify the email of the user
- `login` _str_ - Specify the login type of the user
- `password` _str_ - Specify the password of the user
- `org_id` _int_ - Specify the optional org id of the user (default None)

<a id="model.CustomRole"></a>

## CustomRole Objects

```python
class CustomRole(NamedTuple)
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

<a id="model.RolePermission"></a>

## RolePermission Objects

```python
class RolePermission(NamedTuple)
```

The class includes all necessary variables to generate a role permission object

**Arguments**:

- `action` _str_ - Specify the custom role action definition
- `scope` _str_ - Specify the scope definition. If not present, no scope will be mapped to the permission (default None)

