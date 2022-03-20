<a id="grafana_api.legacy_alerting"></a>

# grafana\_api.legacy\_alerting

<a id="grafana_api.legacy_alerting.Alerting"></a>

## Alerting Objects

```python
class Alerting()
```

The class includes all necessary methods to access the Grafana legacy alerting API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="grafana_api.legacy_alerting.Alerting.get_alerts"></a>

#### get\_alerts

```python
def get_alerts(custom_querystring: str = None) -> list
```

The method includes a functionality to get the legacy alerts

**Arguments**:

- `custom_querystring` _str_ - Specify the custom querystring (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of all alerts

<a id="grafana_api.legacy_alerting.Alerting.get_alerts_by_dashboard_ids"></a>

#### get\_alerts\_by\_dashboard\_ids

```python
def get_alerts_by_dashboard_ids(dashboard_ids: list) -> list
```

The method includes a functionality to get legacy alerts specified by the dashboard ids

**Arguments**:

- `dashboard_ids` _list_ - Specify the list of dashboard ids
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of alerts

<a id="grafana_api.legacy_alerting.Alerting.get_alert_by_id"></a>

#### get\_alert\_by\_id

```python
def get_alert_by_id(id: int) -> dict
```

The method includes a functionality to get the legacy alert specified by the alert id

**Arguments**:

- `id` _int_ - Specify the id of the legacy alert
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns an alert

<a id="grafana_api.legacy_alerting.Alerting.pause_alert_by_id"></a>

#### pause\_alert\_by\_id

```python
def pause_alert_by_id(id: int, paused: bool = True)
```

The method includes a functionality to pause/ unpause a legacy alert specified by the alert id

**Arguments**:

- `id` _int_ - Specify the id of the legacy alert
- `paused` _bool_ - Specify the pause/ unpause parameter (default True)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

