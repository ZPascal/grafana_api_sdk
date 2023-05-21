# Table of Contents

* [alerting\_provisioning](#alerting_provisioning)
  * [AlertingProvisioning](#alerting_provisioning.AlertingProvisioning)
    * [get\_alert\_rule](#alerting_provisioning.AlertingProvisioning.get_alert_rule)
    * [add\_alert\_rule](#alerting_provisioning.AlertingProvisioning.add_alert_rule)
    * [update\_alert\_rule](#alerting_provisioning.AlertingProvisioning.update_alert_rule)
    * [update\_the\_interval\_of\_a\_alert\_rule\_group](#alerting_provisioning.AlertingProvisioning.update_the_interval_of_a_alert_rule_group)
    * [delete\_alert\_rule](#alerting_provisioning.AlertingProvisioning.delete_alert_rule)
    * [get\_all\_contact\_points](#alerting_provisioning.AlertingProvisioning.get_all_contact_points)
    * [add\_contact\_point](#alerting_provisioning.AlertingProvisioning.add_contact_point)
    * [update\_contact\_point](#alerting_provisioning.AlertingProvisioning.update_contact_point)
    * [delete\_contact\_point](#alerting_provisioning.AlertingProvisioning.delete_contact_point)
    * [get\_notification\_policies](#alerting_provisioning.AlertingProvisioning.get_notification_policies)
    * [add\_notification\_policies](#alerting_provisioning.AlertingProvisioning.add_notification_policies)
    * [get\_all\_mute\_timings](#alerting_provisioning.AlertingProvisioning.get_all_mute_timings)
    * [get\_mute\_timing](#alerting_provisioning.AlertingProvisioning.get_mute_timing)
    * [add\_mute\_timing](#alerting_provisioning.AlertingProvisioning.add_mute_timing)
    * [update\_mute\_timing](#alerting_provisioning.AlertingProvisioning.update_mute_timing)
    * [delete\_mute\_timing](#alerting_provisioning.AlertingProvisioning.delete_mute_timing)
    * [get\_all\_message\_templates](#alerting_provisioning.AlertingProvisioning.get_all_message_templates)
    * [get\_message\_template](#alerting_provisioning.AlertingProvisioning.get_message_template)
    * [create\_or\_update\_message\_template](#alerting_provisioning.AlertingProvisioning.create_or_update_message_template)
    * [delete\_message\_template](#alerting_provisioning.AlertingProvisioning.delete_message_template)

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

<a id="alerting_provisioning.AlertingProvisioning.get_alert_rule"></a>

#### get\_alert\_rule

```python
def get_alert_rule(uid: str) -> dict
```

The method includes a functionality to get the alert rule specified by the uid

**Arguments**:

- `uid` _str_ - Specify the alert rule uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the alert rule

<a id="alerting_provisioning.AlertingProvisioning.add_alert_rule"></a>

#### add\_alert\_rule

```python
def add_alert_rule(alert_rule: AlertRule, disable_provenance: bool = False)
```

The method includes a functionality to create a new alert rule

**Arguments**:

- `alert_rule` _AlertRule_ - Specify the alert rule
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.update_alert_rule"></a>

#### update\_alert\_rule

```python
def update_alert_rule(uid: str,
                      alert_rule: AlertRule,
                      disable_provenance: bool = False)
```

The method includes a functionality to update an existing alert rule

**Arguments**:

- `uid` _str_ - Specify the alert rule uid
- `alert_rule` _AlertRule_ - Specify the alert rule
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.update_the_interval_of_a_alert_rule_group"></a>

#### update\_the\_interval\_of\_a\_alert\_rule\_group

```python
def update_the_interval_of_a_alert_rule_group(
        folder_uid: str,
        group: str,
        alert_rule_group_interval: int,
        disable_provenance: bool = False)
```

The method includes a functionality to update the interval of a alert rule group

**Arguments**:

- `folder_uid` _str_ - Specify the folder uid
- `group` _str_ - Specify the group
- `alert_rule_group_interval` _int_ - Specify the alert rule group interval
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.delete_alert_rule"></a>

#### delete\_alert\_rule

```python
def delete_alert_rule(uid: str, disable_provenance: bool = False)
```

The method includes a functionality to delete an alert rule

**Arguments**:

- `uid` _str_ - Specify the alert rule uid
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.get_all_contact_points"></a>

#### get\_all\_contact\_points

```python
def get_all_contact_points() -> list
```

The method includes a functionality to get all contact points

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all contact points

<a id="alerting_provisioning.AlertingProvisioning.add_contact_point"></a>

#### add\_contact\_point

```python
def add_contact_point(embedded_contact_point: EmbeddedContactPoint,
                      disable_provenance: bool = False)
```

The method includes a functionality to create a contact point

**Arguments**:

- `embedded_contact_point` _EmbeddedContactPoint_ - Specify the embedded contact point
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.update_contact_point"></a>

#### update\_contact\_point

```python
def update_contact_point(uid: str,
                         embedded_contact_point: EmbeddedContactPoint,
                         disable_provenance: bool = False)
```

The method includes a functionality to update a contact point

**Arguments**:

- `uid` _str_ - Specify the uid of the contact point
- `embedded_contact_point` _EmbeddedContactPoint_ - Specify the embedded contact point
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.delete_contact_point"></a>

#### delete\_contact\_point

```python
def delete_contact_point(uid: str)
```

The method includes a functionality to delete a contact point

**Arguments**:

- `uid` _str_ - Specify the uid of the contact point
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.get_notification_policies"></a>

#### get\_notification\_policies

```python
def get_notification_policies() -> dict
```

The method includes a functionality to get the notification policy tree

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the notification policy tree

<a id="alerting_provisioning.AlertingProvisioning.add_notification_policies"></a>

#### add\_notification\_policies

```python
def add_notification_policies(route: Route, disable_provenance: bool = False)
```

The method includes a functionality to set the notification policy tree

**Arguments**:

- `route` _Route_ - Specify the alert rule routes
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.get_all_mute_timings"></a>

#### get\_all\_mute\_timings

```python
def get_all_mute_timings() -> list
```

The method includes a functionality to get all mute timings

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all mute timings

<a id="alerting_provisioning.AlertingProvisioning.get_mute_timing"></a>

#### get\_mute\_timing

```python
def get_mute_timing(name: str) -> dict
```

The method includes a functionality to get a mute timings specified by the name

**Arguments**:

- `name` _str_ - Specify the mute timing name
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the mute timing

<a id="alerting_provisioning.AlertingProvisioning.add_mute_timing"></a>

#### add\_mute\_timing

```python
def add_mute_timing(mute_time_interval: MuteTimeInterval,
                    disable_provenance: bool = False)
```

The method includes a functionality to create a mute timing

**Arguments**:

- `mute_time_interval` _MuteTimeInterval_ - Specify the mute time interval
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.update_mute_timing"></a>

#### update\_mute\_timing

```python
def update_mute_timing(name: str,
                       mute_time_interval: MuteTimeInterval,
                       disable_provenance: bool = False)
```

The method includes a functionality to update an existing mute timing

**Arguments**:

- `name` _str_ - Specify the mute timing name
- `mute_time_interval` _MuteTimeInterval_ - Specify the mute time interval
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.delete_mute_timing"></a>

#### delete\_mute\_timing

```python
def delete_mute_timing(name: str)
```

The method includes a functionality to delete a mute timings specified by the name

**Arguments**:

- `name` _str_ - Specify the mute timing name
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.get_all_message_templates"></a>

#### get\_all\_message\_templates

```python
def get_all_message_templates() -> list
```

The method includes a functionality to get all message templates

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all message templates

<a id="alerting_provisioning.AlertingProvisioning.get_message_template"></a>

#### get\_message\_template

```python
def get_message_template(name: str) -> dict
```

The method includes a functionality to get a message template specified by the name

**Arguments**:

- `name` _str_ - Specify the message template name
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the message template

<a id="alerting_provisioning.AlertingProvisioning.create_or_update_message_template"></a>

#### create\_or\_update\_message\_template

```python
def create_or_update_message_template(name: str,
                                      message_template: str,
                                      disable_provenance: bool = False)
```

The method includes a functionality to create or update a message template

**Arguments**:

- `name` _str_ - Specify the message template name
- `message_template` _str_ - Specify the message template
- `disable_provenance` _bool_ - Specify if the provenance header should be set or not (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="alerting_provisioning.AlertingProvisioning.delete_message_template"></a>

#### delete\_message\_template

```python
def delete_message_template(name: str)
```

The method includes a functionality to delete a message template

**Arguments**:

- `name` _str_ - Specify the message template name
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

