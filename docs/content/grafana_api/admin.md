# Table of Contents

* [admin](#admin)
  * [Admin](#admin.Admin)
    * [get\_settings](#admin.Admin.get_settings)
    * [update\_settings](#admin.Admin.update_settings)
    * [get\_stats](#admin.Admin.get_stats)
    * [get\_preview\_report](#admin.Admin.get_preview_report)
    * [create\_global\_user](#admin.Admin.create_global_user)
    * [update\_user\_password](#admin.Admin.update_user_password)
    * [update\_user\_permissions](#admin.Admin.update_user_permissions)
    * [delete\_global\_user](#admin.Admin.delete_global_user)
    * [pause\_all\_alerts](#admin.Admin.pause_all_alerts)
    * [unpause\_all\_alerts](#admin.Admin.unpause_all_alerts)
    * [get\_user\_auth\_token](#admin.Admin.get_user_auth_token)
    * [revoke\_user\_auth\_token](#admin.Admin.revoke_user_auth_token)
    * [logout\_user](#admin.Admin.logout_user)
    * [reload\_dashboards\_provisioning\_configuration](#admin.Admin.reload_dashboards_provisioning_configuration)
    * [reload\_datasources\_provisioning\_configuration](#admin.Admin.reload_datasources_provisioning_configuration)
    * [reload\_plugins\_provisioning\_configuration](#admin.Admin.reload_plugins_provisioning_configuration)
    * [reload\_notifications\_provisioning\_configuration](#admin.Admin.reload_notifications_provisioning_configuration)
    * [reload\_access\_controls\_provisioning\_configuration](#admin.Admin.reload_access_controls_provisioning_configuration)
    * [reload\_ldap\_configuration](#admin.Admin.reload_ldap_configuration)
    * [rotate\_data\_encryption\_keys](#admin.Admin.rotate_data_encryption_keys)

<a id="admin"></a>

# admin

<a id="admin.Admin"></a>

## Admin Objects

```python
class Admin()
```

The class includes all necessary methods to access the Grafana admin API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="admin.Admin.get_settings"></a>

#### get\_settings

```python
def get_settings() -> dict
```

The method includes a functionality to get the settings

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding settings

<a id="admin.Admin.update_settings"></a>

#### update\_settings

```python
def update_settings(updates: dict = None, removals: dict = None)
```

The method includes a functionality to update the settings. Be aware that the functionality is a Grafana v8.0+ feature and you can find detailed information about the dict values here: https://grafana.com/docs/grafana/latest/developers/http_api/admin/`update`-settings

**Arguments**:

- `updates` _dict_ - Specify the updates object
- `removals` _dict_ - Specify the removals object
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.get_stats"></a>

#### get\_stats

```python
def get_stats() -> dict
```

The method includes a functionality to get the admin statistics

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding statistics

<a id="admin.Admin.get_preview_report"></a>

#### get\_preview\_report

```python
def get_preview_report() -> dict
```

The method includes a functionality to get a preview report

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the preview report

<a id="admin.Admin.create_global_user"></a>

#### create\_global\_user

```python
def create_global_user(user: GlobalUser) -> int
```

The method includes a functionality to create a global user

**Arguments**:

- `user` _GlobalUser_ - Specify the global user object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _int_ - Returns the corresponding user id

<a id="admin.Admin.update_user_password"></a>

#### update\_user\_password

```python
def update_user_password(id: int, password: str)
```

The method includes a functionality to update the global user password

**Arguments**:

- `id` _int_ - Specify the user id
- `password` _str_ - Specify the user new password
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.update_user_permissions"></a>

#### update\_user\_permissions

```python
def update_user_permissions(id: int, is_grafana_admin: bool = None)
```

The method includes a functionality to update the global user permissions

**Arguments**:

- `id` _int_ - Specify the user id
- `is_grafana_admin` _bool_ - Specify if the user is admin or not
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.delete_global_user"></a>

#### delete\_global\_user

```python
def delete_global_user(id: int)
```

The method includes a functionality to delete a global user

**Arguments**:

- `id` _int_ - Specify the user id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.pause_all_alerts"></a>

#### pause\_all\_alerts

```python
def pause_all_alerts()
```

The method includes a functionality to pause all alerts

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.unpause_all_alerts"></a>

#### unpause\_all\_alerts

```python
def unpause_all_alerts()
```

The method includes a functionality to unpause all alerts

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.get_user_auth_token"></a>

#### get\_user\_auth\_token

```python
def get_user_auth_token(id: int) -> list
```

The method includes a functionality to get the corresponding user auth token

**Arguments**:

- `id` _int_ - Specify the user id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the corresponding user auth tokens

<a id="admin.Admin.revoke_user_auth_token"></a>

#### revoke\_user\_auth\_token

```python
def revoke_user_auth_token(id: int, auth_token_id: int)
```

The method includes a functionality to get the corresponding user auth token

**Arguments**:

- `id` _int_ - Specify the user id
- `auth_token_id` _int_ - Specify the auth token id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.logout_user"></a>

#### logout\_user

```python
def logout_user(id: int)
```

The method includes a functionality to log out the corresponding user

**Arguments**:

- `id` _int_ - Specify the user id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_dashboards_provisioning_configuration"></a>

#### reload\_dashboards\_provisioning\_configuration

```python
def reload_dashboards_provisioning_configuration()
```

The method includes a functionality to reload the dashboards provisioning configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_datasources_provisioning_configuration"></a>

#### reload\_datasources\_provisioning\_configuration

```python
def reload_datasources_provisioning_configuration()
```

The method includes a functionality to reload the datasources provisioning configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_plugins_provisioning_configuration"></a>

#### reload\_plugins\_provisioning\_configuration

```python
def reload_plugins_provisioning_configuration()
```

The method includes a functionality to reload the plugins provisioning configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_notifications_provisioning_configuration"></a>

#### reload\_notifications\_provisioning\_configuration

```python
def reload_notifications_provisioning_configuration()
```

The method includes a functionality to reload the notifications provisioning configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_access_controls_provisioning_configuration"></a>

#### reload\_access\_controls\_provisioning\_configuration

```python
def reload_access_controls_provisioning_configuration()
```

The method includes a functionality to reload the access-controls provisioning configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.reload_ldap_configuration"></a>

#### reload\_ldap\_configuration

```python
def reload_ldap_configuration()
```

The method includes a functionality to reload the ldap configuration

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="admin.Admin.rotate_data_encryption_keys"></a>

#### rotate\_data\_encryption\_keys

```python
def rotate_data_encryption_keys()
```

The method includes a functionality to rotate the data encryption keys

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

