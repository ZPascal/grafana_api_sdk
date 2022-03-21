# Table of Contents

* [grafana\_api.alerting](#grafana_api.alerting)
  * [Alerting](#grafana_api.alerting.Alerting)
    * [get\_alertmanager\_alerts](#grafana_api.alerting.Alerting.get_alertmanager_alerts)
    * [create\_or\_update\_alertmanager\_alerts](#grafana_api.alerting.Alerting.create_or_update_alertmanager_alerts)
    * [get\_alertmanager\_group\_alerts](#grafana_api.alerting.Alerting.get_alertmanager_group_alerts)
    * [delete\_alertmanager\_silence\_by\_id](#grafana_api.alerting.Alerting.delete_alertmanager_silence_by_id)
    * [get\_alertmanager\_silence\_by\_id](#grafana_api.alerting.Alerting.get_alertmanager_silence_by_id)
    * [get\_alertmanager\_silences](#grafana_api.alerting.Alerting.get_alertmanager_silences)
    * [create\_or\_update\_alertmanager\_silence](#grafana_api.alerting.Alerting.create_or_update_alertmanager_silence)
    * [get\_alertmanager\_status](#grafana_api.alerting.Alerting.get_alertmanager_status)
    * [delete\_alertmanager\_config](#grafana_api.alerting.Alerting.delete_alertmanager_config)
    * [get\_alertmanager\_config](#grafana_api.alerting.Alerting.get_alertmanager_config)
    * [create\_or\_update\_alertmanager\_config](#grafana_api.alerting.Alerting.create_or_update_alertmanager_config)
    * [test\_alertmanager\_receivers](#grafana_api.alerting.Alerting.test_alertmanager_receivers)
    * [get\_prometheus\_alerts](#grafana_api.alerting.Alerting.get_prometheus_alerts)
    * [get\_prometheus\_rules](#grafana_api.alerting.Alerting.get_prometheus_rules)
    * [get\_ruler\_rules](#grafana_api.alerting.Alerting.get_ruler_rules)
    * [delete\_ruler\_namespace](#grafana_api.alerting.Alerting.delete_ruler_namespace)
    * [get\_ruler\_groups\_by\_namespace](#grafana_api.alerting.Alerting.get_ruler_groups_by_namespace)
    * [create\_or\_update\_ruler\_group\_by\_namespace](#grafana_api.alerting.Alerting.create_or_update_ruler_group_by_namespace)
    * [delete\_ruler\_group](#grafana_api.alerting.Alerting.delete_ruler_group)
    * [get\_ruler\_group](#grafana_api.alerting.Alerting.get_ruler_group)
    * [test\_rule](#grafana_api.alerting.Alerting.test_rule)
    * [test\_recipient\_rule](#grafana_api.alerting.Alerting.test_recipient_rule)
    * [delete\_ngalert\_organization\_configuration](#grafana_api.alerting.Alerting.delete_ngalert_organization_configuration)
    * [get\_ngalert\_organization\_configuration](#grafana_api.alerting.Alerting.get_ngalert_organization_configuration)
    * [create\_or\_update\_ngalert\_organization\_configuration](#grafana_api.alerting.Alerting.create_or_update_ngalert_organization_configuration)
    * [get\_ngalert\_alertmanagers\_by\_organization](#grafana_api.alerting.Alerting.get_ngalert_alertmanagers_by_organization)

<a id="grafana_api.alerting"></a>

# grafana\_api.alerting

<a id="grafana_api.alerting.Alerting"></a>

## Alerting Objects

```python
class Alerting()
```

The class includes all necessary methods to access the Grafana alerting API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="grafana_api.alerting.Alerting.get_alertmanager_alerts"></a>

#### get\_alertmanager\_alerts

```python
def get_alertmanager_alerts(recipient: any = "grafana") -> list
```

The method includes a functionality to get the Alertmanager alerts specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager alerts

<a id="grafana_api.alerting.Alerting.create_or_update_alertmanager_alerts"></a>

#### create\_or\_update\_alertmanager\_alerts

```python
def create_or_update_alertmanager_alerts(alerts: list,
                                         recipient: any = "grafana")
```

The method includes a functionality to create or update the Alertmanager alerts specified by the recipient and the alerts list

**Arguments**:

- `alerts` _list_ - Specify a list of the alert objects
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_alertmanager_group_alerts"></a>

#### get\_alertmanager\_group\_alerts

```python
def get_alertmanager_group_alerts(recipient: any = "grafana") -> list
```

The method includes a functionality to get the Alertmanager group alerts specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager group alerts

<a id="grafana_api.alerting.Alerting.delete_alertmanager_silence_by_id"></a>

#### delete\_alertmanager\_silence\_by\_id

```python
def delete_alertmanager_silence_by_id(silence_id: str,
                                      recipient: any = "grafana")
```

The method includes a functionality to delete the Alertmanager silence specified by the silence id and the recipient

**Arguments**:

- `silence_id` _str_ - Specify the silence id of the alerts
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_alertmanager_silence_by_id"></a>

#### get\_alertmanager\_silence\_by\_id

```python
def get_alertmanager_silence_by_id(silence_id: str,
                                   recipient: any = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager silence specified by the silence id and the recipient

**Arguments**:

- `silence_id` _str_ - Specify the silence id of the alerts
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of Alertmanager silence alert

<a id="grafana_api.alerting.Alerting.get_alertmanager_silences"></a>

#### get\_alertmanager\_silences

```python
def get_alertmanager_silences(recipient: any = "grafana") -> list
```

The method includes a functionality to get all Alertmanager silences specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Alertmanager silence alerts

<a id="grafana_api.alerting.Alerting.create_or_update_alertmanager_silence"></a>

#### create\_or\_update\_alertmanager\_silence

```python
def create_or_update_alertmanager_silence(silence: Silence,
                                          recipient: any = "grafana") -> dict
```

The method includes a functionality to create or update the Alertmanager silence specified by the silence object and the recipient

**Arguments**:

  silence -> Specify the silence object
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of newly created silence alert

<a id="grafana_api.alerting.Alerting.get_alertmanager_status"></a>

#### get\_alertmanager\_status

```python
def get_alertmanager_status(recipient: str = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager status specified by the recipient

**Arguments**:

- `recipient` _str_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the Alertmanager status

<a id="grafana_api.alerting.Alerting.delete_alertmanager_config"></a>

#### delete\_alertmanager\_config

```python
def delete_alertmanager_config(recipient: any = "grafana")
```

The method includes a functionality to delete the Alertmanager config specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_alertmanager_config"></a>

#### get\_alertmanager\_config

```python
def get_alertmanager_config(recipient: any = "grafana") -> dict
```

The method includes a functionality to get the Alertmanager config specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the Alertmanager config

<a id="grafana_api.alerting.Alerting.create_or_update_alertmanager_config"></a>

#### create\_or\_update\_alertmanager\_config

```python
def create_or_update_alertmanager_config(
        alertmanager_config: AlertmanagerConfig,
        recipient: any = "grafana",
        template_files: dict = None)
```

The method includes a functionality to create or update the Alertmanager config specified by the Alertmanager config object, recipient and template_files

**Arguments**:

- `alertmanager_config` _AlertmanagerConfig_ - Specify the Alertmanager config object
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
- `template_files(dict)` - Specify the optional template files (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.test_alertmanager_receivers"></a>

#### test\_alertmanager\_receivers

```python
def test_alertmanager_receivers(alert: dict,
                                receivers: list,
                                recipient: any = "grafana")
```

The method includes a functionality to test the Alertmanager receivers specified by the alert dict, receivers object and the recipient

**Arguments**:

- `alert` _dict_ - Specify the alert dict
- `receivers` _list_ - Specify the list of AlertmanagerReceivers objects
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_prometheus_alerts"></a>

#### get\_prometheus\_alerts

```python
def get_prometheus_alerts(recipient: any = "grafana") -> dict
```

The method includes a functionality to get all prometheus alerts specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the prometheus alerts

<a id="grafana_api.alerting.Alerting.get_prometheus_rules"></a>

#### get\_prometheus\_rules

```python
def get_prometheus_rules(recipient: any = "grafana") -> dict
```

The method includes a functionality to get all prometheus rules specified by the recipient

**Arguments**:

- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the prometheus rules

<a id="grafana_api.alerting.Alerting.get_ruler_rules"></a>

#### get\_ruler\_rules

```python
def get_ruler_rules(recipient: str = "grafana") -> dict
```

The method includes a functionality to get all ruler rules specified by the recipient

**Arguments**:

- `recipient` _str_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the ruler rules

<a id="grafana_api.alerting.Alerting.delete_ruler_namespace"></a>

#### delete\_ruler\_namespace

```python
def delete_ruler_namespace(namespace: str, recipient: any = "grafana")
```

The method includes a functionality to delete a ruler namespace specified by the namespace name and the recipient

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_ruler_groups_by_namespace"></a>

#### get\_ruler\_groups\_by\_namespace

```python
def get_ruler_groups_by_namespace(namespace: str,
                                  recipient: any = "grafana") -> dict
```

The method includes a functionality to get all ruler groups specified by the namespace name and the recipient

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of the ruler groups

<a id="grafana_api.alerting.Alerting.create_or_update_ruler_group_by_namespace"></a>

#### create\_or\_update\_ruler\_group\_by\_namespace

```python
def create_or_update_ruler_group_by_namespace(namespace: str,
                                              group_name: str,
                                              rules: list,
                                              recipient: any = "grafana",
                                              interval: int = 0)
```

The method includes a functionality to create or update a ruler group specified by the namespace name, a ruler group name, a ruler rule object list, the recipient and an interval

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `rules` _list_ - Specify the ruler rule object list
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
- `interval` _int_ - Specify the interval of the ruler (default 0)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.delete_ruler_group"></a>

#### delete\_ruler\_group

```python
def delete_ruler_group(namespace: str,
                       group_name: str,
                       recipient: any = "grafana")
```

The method includes a functionality to delete a ruler group specified by the namespace name, a ruler group name and the recipient

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_ruler_group"></a>

#### get\_ruler\_group

```python
def get_ruler_group(namespace: str,
                    group_name: str,
                    recipient: any = "grafana") -> dict
```

The method includes a functionality to get a ruler group specified by the namespace name, a ruler group name and the recipient

**Arguments**:

- `namespace` _str_ - Specify the namespace name
- `group_name` _str_ - Specify the ruler group name
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dict of all ruler groups

<a id="grafana_api.alerting.Alerting.test_rule"></a>

#### test\_rule

```python
def test_rule(data_query: list) -> dict
```

The method includes a functionality to test a rule specified by a list of datasource rule query objects

**Arguments**:

- `data_query` _list_ - Specify a list of datasource rule query objects
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _str_ - Returns the result of the specified query

<a id="grafana_api.alerting.Alerting.test_recipient_rule"></a>

#### test\_recipient\_rule

```python
def test_recipient_rule(expr: str,
                        condition: str,
                        data_query: list,
                        recipient: any = "grafana") -> dict
```

The method includes a functionality to test a recipient role specified by the expr, the condition, a list of data queries and the recipient

**Arguments**:

- `expr` _str_ - Specify a list of datasource rule query objects
- `condition` _str_ - Specify the condition
- `data_query` _list_ - Specify a list of datasource rule query objects
- `recipient` _any_ - Specify the recipient datasource id of the alerts (default grafana)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of the specified recipient rule

<a id="grafana_api.alerting.Alerting.delete_ngalert_organization_configuration"></a>

#### delete\_ngalert\_organization\_configuration

```python
def delete_ngalert_organization_configuration()
```

The method includes a functionality to delete the NGAlert organization admin configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting.Alerting.get_ngalert_organization_configuration"></a>

#### get\_ngalert\_organization\_configuration

```python
def get_ngalert_organization_configuration() -> dict
```

The method includes a functionality to get the NGAlert organization admin configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the NGAlert organization configuration

<a id="grafana_api.alerting.Alerting.create_or_update_ngalert_organization_configuration"></a>

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

<a id="grafana_api.alerting.Alerting.get_ngalert_alertmanagers_by_organization"></a>

#### get\_ngalert\_alertmanagers\_by\_organization

```python
def get_ngalert_alertmanagers_by_organization() -> dict
```

The method includes a functionality to get the discovered and dropped Alertmanagers of the user's organization and based on the specified configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the NGAlert Alertmanagers

