# Table of Contents

* [other\_http](#other_http)
  * [OtherHTTP](#other_http.OtherHTTP)
    * [get\_frontend\_settings](#other_http.OtherHTTP.get_frontend_settings)
    * [renew\_login\_session\_based\_on\_remember\_cookie](#other_http.OtherHTTP.renew_login_session_based_on_remember_cookie)
    * [get\_health\_status](#other_http.OtherHTTP.get_health_status)
    * [get\_metrics](#other_http.OtherHTTP.get_metrics)
    * [get\_plugin\_metrics](#other_http.OtherHTTP.get_plugin_metrics)

<a id="other_http"></a>

# other\_http

<a id="other_http.OtherHTTP"></a>

## OtherHTTP Objects

```python
class OtherHTTP()
```

The class includes all necessary methods to access other Grafana API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="other_http.OtherHTTP.get_frontend_settings"></a>

#### get\_frontend\_settings

```python
def get_frontend_settings() -> dict
```

The method includes a functionality to get the frontend settings

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding frontend settings

<a id="other_http.OtherHTTP.renew_login_session_based_on_remember_cookie"></a>

#### renew\_login\_session\_based\_on\_remember\_cookie

```python
def renew_login_session_based_on_remember_cookie()
```

The method includes a functionality to renew the login session based on the remember cookie

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="other_http.OtherHTTP.get_health_status"></a>

#### get\_health\_status

```python
def get_health_status() -> dict
```

The method includes a functionality to get the health information

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the health information

<a id="other_http.OtherHTTP.get_metrics"></a>

#### get\_metrics

```python
def get_metrics(basic_auth_username: str = None,
                basic_auth_password: str = None) -> str
```

The method includes a functionality to get the Grafana metrics information

**Arguments**:

- `basic_auth_username` _str_ - Specify the optional basic auth username
- `basic_auth_password` _str_ - Specify the optional basic auth password
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _str_ - Returns the metrics information

<a id="other_http.OtherHTTP.get_plugin_metrics"></a>

#### get\_plugin\_metrics

```python
def get_plugin_metrics(plugin_id: str,
                       basic_auth_username: str = None,
                       basic_auth_password: str = None) -> str
```

The method includes a functionality to get the Grafana plugin metrics information

**Arguments**:

- `plugin_id` _str_ - Specify the plugin id
- `basic_auth_username` _str_ - Specify the optional basic auth username
- `basic_auth_password` _str_ - Specify the optional basic auth password
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _str_ - Returns the metrics information

