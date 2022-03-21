# Table of Contents

* [grafana\_api.alerting\_notifications](#grafana_api.alerting_notifications)
  * [AlertingNotifications](#grafana_api.alerting_notifications.AlertingNotifications)
    * [get\_all\_notification\_channels](#grafana_api.alerting_notifications.AlertingNotifications.get_all_notification_channels)
    * [get\_all\_notification\_channels\_lookup](#grafana_api.alerting_notifications.AlertingNotifications.get_all_notification_channels_lookup)
    * [get\_notification\_channel\_by\_uid](#grafana_api.alerting_notifications.AlertingNotifications.get_notification_channel_by_uid)
    * [get\_notification\_channel\_by\_id](#grafana_api.alerting_notifications.AlertingNotifications.get_notification_channel_by_id)
    * [create\_notification\_channel](#grafana_api.alerting_notifications.AlertingNotifications.create_notification_channel)
    * [update\_notification\_channel\_by\_uid](#grafana_api.alerting_notifications.AlertingNotifications.update_notification_channel_by_uid)
    * [update\_notification\_channel\_by\_id](#grafana_api.alerting_notifications.AlertingNotifications.update_notification_channel_by_id)
    * [delete\_notification\_channel\_by\_uid](#grafana_api.alerting_notifications.AlertingNotifications.delete_notification_channel_by_uid)
    * [delete\_notification\_channel\_by\_id](#grafana_api.alerting_notifications.AlertingNotifications.delete_notification_channel_by_id)
    * [test\_notification\_channel](#grafana_api.alerting_notifications.AlertingNotifications.test_notification_channel)

<a id="grafana_api.alerting_notifications"></a>

# grafana\_api.alerting\_notifications

<a id="grafana_api.alerting_notifications.AlertingNotifications"></a>

## AlertingNotifications Objects

```python
class AlertingNotifications()
```

The class includes all necessary methods to access the Grafana alerting notifications API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="grafana_api.alerting_notifications.AlertingNotifications.get_all_notification_channels"></a>

#### get\_all\_notification\_channels

```python
def get_all_notification_channels() -> list
```

The method includes a functionality to get all alerting notification channels

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all notification channels

<a id="grafana_api.alerting_notifications.AlertingNotifications.get_all_notification_channels_lookup"></a>

#### get\_all\_notification\_channels\_lookup

```python
def get_all_notification_channels_lookup() -> list
```

The method includes a functionality to lookup and get reduced information of all alerting notification channels

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all notification channels as reduced information

<a id="grafana_api.alerting_notifications.AlertingNotifications.get_notification_channel_by_uid"></a>

#### get\_notification\_channel\_by\_uid

```python
def get_notification_channel_by_uid(uid: str) -> dict
```

The method includes a functionality to get an alerting notification channel specified by the uid

**Arguments**:

- `uid` _str_ - Specify the uid of the notification channel
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the specified notification channel

<a id="grafana_api.alerting_notifications.AlertingNotifications.get_notification_channel_by_id"></a>

#### get\_notification\_channel\_by\_id

```python
def get_notification_channel_by_id(id: int) -> dict
```

The method includes a functionality to get an alerting notification channel specified by the id

**Arguments**:

- `id` _int_ - Specify the id of the notification channel
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the specified notification channel

<a id="grafana_api.alerting_notifications.AlertingNotifications.create_notification_channel"></a>

#### create\_notification\_channel

```python
def create_notification_channel(notification_channel: dict) -> dict
```

The method includes a functionality to create an alerting notification channel specified by the notification channel dict

**Arguments**:

- `notification_channel` _dict_ - Specify the channel of the notification
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the newly created notification channel

<a id="grafana_api.alerting_notifications.AlertingNotifications.update_notification_channel_by_uid"></a>

#### update\_notification\_channel\_by\_uid

```python
def update_notification_channel_by_uid(uid: str,
                                       notification_channel: dict) -> dict
```

The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the uid

**Arguments**:

- `uid` _str_ - Specify the uid of the notification channel
- `notification_channel` _dict_ - Specify the channel of the notification
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the updated notification channel

<a id="grafana_api.alerting_notifications.AlertingNotifications.update_notification_channel_by_id"></a>

#### update\_notification\_channel\_by\_id

```python
def update_notification_channel_by_id(id: int,
                                      notification_channel: dict) -> dict
```

The method includes a functionality to update an alerting notification channel specified by the notification channel dict and the id

**Arguments**:

- `id` _int_ - Specify the id of the notification channel
- `notification_channel` _dict_ - Specify the channel of the notification
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the updated notification channel

<a id="grafana_api.alerting_notifications.AlertingNotifications.delete_notification_channel_by_uid"></a>

#### delete\_notification\_channel\_by\_uid

```python
def delete_notification_channel_by_uid(uid: str)
```

The method includes a functionality to delete an alerting notification channel specified by the uid

**Arguments**:

- `uid` _uid_ - Specify the uid of the notification channel
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting_notifications.AlertingNotifications.delete_notification_channel_by_id"></a>

#### delete\_notification\_channel\_by\_id

```python
def delete_notification_channel_by_id(id: int)
```

The method includes a functionality to delete an alerting notification channel specified by the id

**Arguments**:

- `id` _int_ - Specify the id of the notification channel
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.alerting_notifications.AlertingNotifications.test_notification_channel"></a>

#### test\_notification\_channel

```python
def test_notification_channel(notification_channel: dict)
```

The method includes a functionality to test an alerting notification channel specified by the notification_channel

**Arguments**:

- `notification_channel` _dict_ - Specify the channel of the notification
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

