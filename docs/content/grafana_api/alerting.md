# Table of Contents

* [alerting](#alerting)
  * [Alerting](#alerting.Alerting)
    * [get\_alertmanager\_alerts](#alerting.Alerting.get_alertmanager_alerts)
    * [create\_or\_update\_alertmanager\_alerts](#alerting.Alerting.create_or_update_alertmanager_alerts)
    * [get\_alertmanager\_group\_alerts](#alerting.Alerting.get_alertmanager_group_alerts)
    * [delete\_alertmanager\_silence\_by\_id](#alerting.Alerting.delete_alertmanager_silence_by_id)
    * [get\_alertmanager\_silence\_by\_id](#alerting.Alerting.get_alertmanager_silence_by_id)
    * [get\_alertmanager\_silences](#alerting.Alerting.get_alertmanager_silences)
    * [create\_or\_update\_alertmanager\_silence](#alerting.Alerting.create_or_update_alertmanager_silence)
    * [get\_alertmanager\_status](#alerting.Alerting.get_alertmanager_status)
    * [delete\_alertmanager\_config](#alerting.Alerting.delete_alertmanager_config)
    * [get\_alertmanager\_config](#alerting.Alerting.get_alertmanager_config)
    * [create\_or\_update\_alertmanager\_config](#alerting.Alerting.create_or_update_alertmanager_config)
    * [test\_alertmanager\_receivers](#alerting.Alerting.test_alertmanager_receivers)
    * [get\_prometheus\_alerts](#alerting.Alerting.get_prometheus_alerts)
    * [get\_prometheus\_rules](#alerting.Alerting.get_prometheus_rules)
    * [get\_ruler\_rules](#alerting.Alerting.get_ruler_rules)
    * [delete\_ruler\_namespace](#alerting.Alerting.delete_ruler_namespace)
    * [get\_ruler\_groups\_by\_namespace](#alerting.Alerting.get_ruler_groups_by_namespace)
    * [create\_or\_update\_ruler\_group\_by\_namespace](#alerting.Alerting.create_or_update_ruler_group_by_namespace)
    * [delete\_ruler\_group](#alerting.Alerting.delete_ruler_group)
    * [get\_ruler\_group](#alerting.Alerting.get_ruler_group)
    * [test\_rule](#alerting.Alerting.test_rule)
    * [test\_datasource\_uid\_rule](#alerting.Alerting.test_datasource_uid_rule)
    * [test\_backtest\_rule](#alerting.Alerting.test_backtest_rule)
    * [delete\_ngalert\_organization\_configuration](#alerting.Alerting.delete_ngalert_organization_configuration)
    * [get\_ngalert\_organization\_configuration](#alerting.Alerting.get_ngalert_organization_configuration)
    * [create\_or\_update\_ngalert\_organization\_configuration](#alerting.Alerting.create_or_update_ngalert_organization_configuration)
    * [get\_ngalert\_alertmanagers\_by\_organization](#alerting.Alerting.get_ngalert_alertmanagers_by_organization)

<a id="alerting"></a>

# alerting

<a id="alerting.Alerting"></a>

## Alerting Objects

```python
class Alerting()
```

The class includes all necessary methods to access the Grafana alerting API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="alerting.Alerting.get_alertmanager_alerts"></a>

#### get\_alertmanager\_alerts

```python
def get_alertmanager_alerts(datasource_uid: str = "grafana") -> list
```

The method includes a functionality to get the Alertmanager alerts specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager alerts

<a id="alerting.Alerting.create_or_update_alertmanager_alerts"></a>

#### create\_or\_update\_alertmanager\_alerts

```python
def create_or_update_alertmanager_alerts(alerts: list,
                                         datasource_uid: str = "grafana")
```

The method includes a functionality to create or update the Alertmanager alerts specified by the datasource_uid and the alerts list

**Arguments**:

- `alerts` _list_ - Specify a list of the alert objects
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_alertmanager_group_alerts"></a>

#### get\_alertmanager\_group\_alerts

```python
def get_alertmanager_group_alerts(datasource_uid: str = "grafana") -> list
```

The method includes a functionality to get the Alertmanager group alerts specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager group alerts

<a id="alerting.Alerting.delete_alertmanager_silence_by_id"></a>

#### delete\_alertmanager\_silence\_by\_id

```python
def delete_alertmanager_silence_by_id(silence_id: str,
                                      datasource_uid: str = "grafana")
```

The method includes a functionality to delete the Alertmanager silence specified by the silence id and the datasource_uid

**Arguments**:

- `silence_id` _str_ - Specify the silence id of the alerts
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_alertmanager_silence_by_id"></a>

#### get\_alertmanager\_silence\_by\_id

```python
def get_alertmanager_silence_by_id(silence_id: str,
                                   datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager silence specified by the silence id and the datasource_uid

**Arguments**:

- `silence_id` _str_ - Specify the silence id of the alerts
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of Alertmanager silence alert

<a id="alerting.Alerting.get_alertmanager_silences"></a>

#### get\_alertmanager\_silences

```python
def get_alertmanager_silences(datasource_uid: str = "grafana") -> list
```

The method includes a functionality to get all Alertmanager silences specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager silence alerts

<a id="alerting.Alerting.create_or_update_alertmanager_silence"></a>

#### create\_or\_update\_alertmanager\_silence

```python
def create_or_update_alertmanager_silence(silence: Silence,
                                          datasource_uid: str = "grafana"
                                          ) -> dict
```

The method includes a functionality to create or update the Alertmanager silence specified by the silence object and the datasource_uid

**Arguments**:

  silence -> Specify the silence object
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of newly created silence alert

<a id="alerting.Alerting.get_alertmanager_status"></a>

#### get\_alertmanager\_status

```python
def get_alertmanager_status(datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager status specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the Alertmanager status

<a id="alerting.Alerting.delete_alertmanager_config"></a>

#### delete\_alertmanager\_config

```python
def delete_alertmanager_config(datasource_uid: str = "grafana")
```

The method includes a functionality to delete the Alertmanager config specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_alertmanager_config"></a>

#### get\_alertmanager\_config

```python
def get_alertmanager_config(datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager config specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the Alertmanager config

<a id="alerting.Alerting.create_or_update_alertmanager_config"></a>

#### create\_or\_update\_alertmanager\_config

```python
def create_or_update_alertmanager_config(
        alertmanager_config: AlertmanagerConfig,
        datasource_uid: str = "grafana",
        template_files: dict = None)
```

The method includes a functionality to create or update the Alertmanager config specified by the Alertmanager config object, datasource_uid and template_files

**Arguments**:

- `alertmanager_config` _AlertmanagerConfig_ - Specify the Alertmanager config object
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
- `template_files(dict)` - Specify the optional template files (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.test_alertmanager_receivers"></a>

#### test\_alertmanager\_receivers

```python
def test_alertmanager_receivers(alert: dict,
                                receivers: list,
                                datasource_uid: str = "grafana")
```

The method includes a functionality to test the Alertmanager receivers specified by the alert dict, receivers object and the datasource_uid

**Arguments**:

- `alert` _dict_ - Specify the alert dict
- `receivers` _list_ - Specify the list of AlertmanagerReceivers objects
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_prometheus_alerts"></a>

#### get\_prometheus\_alerts

```python
def get_prometheus_alerts(datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get all prometheus alerts specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the prometheus alerts

<a id="alerting.Alerting.get_prometheus_rules"></a>

#### get\_prometheus\_rules

```python
def get_prometheus_rules(datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get all prometheus rules specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the prometheus rules

<a id="alerting.Alerting.get_ruler_rules"></a>

#### get\_ruler\_rules

```python
def get_ruler_rules(datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get all ruler rules specified by the datasource_uid

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the ruler rules

<a id="alerting.Alerting.delete_ruler_namespace"></a>

#### delete\_ruler\_namespace

```python
def delete_ruler_namespace(namespace: str, datasource_uid: str = "grafana")
```

The method includes a functionality to delete a ruler namespace specified by the namespace name and the datasource_uid

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_ruler_groups_by_namespace"></a>

#### get\_ruler\_groups\_by\_namespace

```python
def get_ruler_groups_by_namespace(namespace: str,
                                  datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get all ruler groups specified by the namespace name and the datasource_uid

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the ruler groups

<a id="alerting.Alerting.create_or_update_ruler_group_by_namespace"></a>

#### create\_or\_update\_ruler\_group\_by\_namespace

```python
def create_or_update_ruler_group_by_namespace(namespace: str,
                                              group_name: str,
                                              rules: list,
                                              datasource_uid: str = "grafana",
                                              interval: int = 0)
```

The method includes a functionality to create or update a ruler group specified by the namespace name, a ruler group name, a ruler rule object list, the datasource_uid and an interval

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `rules` _list_ - Specify the ruler rule object list
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
- `interval` _int_ - Specify the interval of the ruler (default 0)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.delete_ruler_group"></a>

#### delete\_ruler\_group

```python
def delete_ruler_group(namespace: str,
                       group_name: str,
                       datasource_uid: str = "grafana")
```

The method includes a functionality to delete a ruler group specified by the namespace name, a ruler group name and the datasource_uid

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_ruler_group"></a>

#### get\_ruler\_group

```python
def get_ruler_group(namespace: str,
                    group_name: str,
                    datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to get a ruler group specified by the namespace name, a ruler group name and the datasource_uid

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of all ruler groups

<a id="alerting.Alerting.test_rule"></a>

#### test\_rule

```python
def test_rule(data_queries: list) -> dict
```

The method includes a functionality to test a rule specified by a list of datasource rule query objects

**Arguments**:

- `data_queries` _list_ - Specify a list of datasource rule query objects
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _str_ - Returns the result of the specified query

<a id="alerting.Alerting.test_datasource_uid_rule"></a>

#### test\_datasource\_uid\_rule

```python
def test_datasource_uid_rule(expr: str,
                             condition: str,
                             data_queries: list,
                             datasource_uid: str = "grafana") -> dict
```

The method includes a functionality to test a datasource uid rule specified by the expr, the condition, a list of data queries and the datasource_uid

**Arguments**:

- `expr` _str_ - Specify a list of datasource rule query objects
- `condition` _str_ - Specify the condition
- `data_queries` _list_ - Specify a list of datasource rule query objects
- `datasource_uid` _str_ - Specify the datasource uid or recipient of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of the specified datasource_uid rule

<a id="alerting.Alerting.test_backtest_rule"></a>

#### test\_backtest\_rule

```python
def test_backtest_rule(condition: str, data_queries: list) -> dict
```

The method includes a functionality to test a rule specified by the condition and a list of data queries

**Arguments**:

- `condition` _str_ - Specify the condition
- `data_queries` _list_ - Specify a list of datasource rule query objects
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of the specified rule

<a id="alerting.Alerting.delete_ngalert_organization_configuration"></a>

#### delete\_ngalert\_organization\_configuration

```python
def delete_ngalert_organization_configuration()
```

The method includes a functionality to delete the NGAlert organization admin configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_ngalert_organization_configuration"></a>

#### get\_ngalert\_organization\_configuration

```python
def get_ngalert_organization_configuration() -> dict
```

The method includes a functionality to get the NGAlert organization admin configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the NGAlert organization configuration

<a id="alerting.Alerting.create_or_update_ngalert_organization_configuration"></a>

#### create\_or\_update\_ngalert\_organization\_configuration

```python
def create_or_update_ngalert_organization_configuration(
        alert_managers: list, alertmanagers_choice: str = "all")
```

The method includes a functionality to create or update the NGAlert organization admin configuration

**Arguments**:

- `alert_managers` _list_ - Specify the list of alert manager names
- `alertmanagers_choice` _str_ - Specify the Alertmanagers choice (default all)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting.Alerting.get_ngalert_alertmanagers_by_organization"></a>

#### get\_ngalert\_alertmanagers\_by\_organization

```python
def get_ngalert_alertmanagers_by_organization() -> dict
```

The method includes a functionality to get the discovered and dropped Alertmanagers of the user's organization and based on the specified configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the NGAlert Alertmanagers

