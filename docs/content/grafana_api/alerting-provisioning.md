# Table of Contents

* [alerting\_provisioning](#alerting_provisioning)
  * [AlertingProvisioning](#alerting_provisioning.AlertingProvisioning)
    * [get\_alertmanager\_alerts](#alerting_provisioning.AlertingProvisioning.get_alertmanager_alerts)

<a id="alerting_provisioning"></a>

# alerting\_provisioning

<a id="alerting_provisioning.AlertingProvisioning"></a>

## AlertingProvisioning Objects

```python
class AlertingProvisioning()
```

The class includes all necessary methods to access the Grafana alerting provisioning API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="alerting_provisioning.AlertingProvisioning.get_alertmanager_alerts"></a>

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

