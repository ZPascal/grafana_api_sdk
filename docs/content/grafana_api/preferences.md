# Table of Contents

* [preferences](#preferences)
  * [Preferences](#preferences.Preferences)
    * [get\_current\_user\_preferences](#preferences.Preferences.get_current_user_preferences)
    * [update\_current\_user\_preferences](#preferences.Preferences.update_current_user_preferences)
    * [get\_current\_org\_preferences](#preferences.Preferences.get_current_org_preferences)
    * [update\_current\_org\_preferences](#preferences.Preferences.update_current_org_preferences)

<a id="preferences"></a>

# preferences

<a id="preferences.Preferences"></a>

## Preferences Objects

```python
class Preferences()
```

The class includes all necessary methods to access the Grafana preferences API endpoints.

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="preferences.Preferences.get_current_user_preferences"></a>

#### get\_current\_user\_preferences

```python
def get_current_user_preferences() -> dict
```

The method includes a functionality to get the current user preferences

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the current user preferences

<a id="preferences.Preferences.update_current_user_preferences"></a>

#### update\_current\_user\_preferences

```python
def update_current_user_preferences(theme: str = None,
                                    timezone: str = None,
                                    home_dashboard_id: int = 0,
                                    home_dashboard_uid: str = None)
```

The method includes a functionality to update the current user preferences

**Arguments**:

- `theme` _str_ - Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
- `home_dashboard_id` _int_ - Specify the dashboard id of the home folder (default 0)
- `home_dashboard_uid` _str_ - Specify the home team dashboard by uid (default None)
- `timezone` _str_ - Specify the timezone e.g. utc, browser, or an empty string for the default (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="preferences.Preferences.get_current_org_preferences"></a>

#### get\_current\_org\_preferences

```python
def get_current_org_preferences() -> dict
```

The method includes a functionality to get the current org preferences

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the current user preferences

<a id="preferences.Preferences.update_current_org_preferences"></a>

#### update\_current\_org\_preferences

```python
def update_current_org_preferences(theme: str = None,
                                   home_dashboard_id: int = 0,
                                   home_dashboard_uid: str = None,
                                   timezone: str = None)
```

The method includes a functionality to update the current org preferences

**Arguments**:

- `theme` _str_ - Specify the theme e.g. light, dark, or an empty string for the default theme (default None)
- `home_dashboard_id` _int_ - Specify the dashboard id of the home folder (default 0)
- `home_dashboard_uid` _str_ - Specify the home team dashboard by uid (default None)
- `timezone` _str_ - Specify the timezone e.g. utc, browser, or an empty string for the default (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

