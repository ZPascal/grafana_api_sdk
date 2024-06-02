# Table of Contents

* [sso\_settings](#sso_settings)
  * [SSOSettings](#sso_settings.SSOSettings)
    * [get\_sso\_settings](#sso_settings.SSOSettings.get_sso_settings)
    * [get\_sso\_settings\_by\_provider](#sso_settings.SSOSettings.get_sso_settings_by_provider)
    * [update\_sso\_settings](#sso_settings.SSOSettings.update_sso_settings)
    * [delete\_sso\_settings](#sso_settings.SSOSettings.delete_sso_settings)

<a id="sso_settings"></a>

# sso\_settings

<a id="sso_settings.SSOSettings"></a>

## SSOSettings Objects

```python
class SSOSettings()
```

The class includes all necessary methods to access the Grafana sso settings API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="sso_settings.SSOSettings.get_sso_settings"></a>

#### get\_sso\_settings

```python
def get_sso_settings() -> list
```

The method includes a functionality to get the SSO settings for all providers

Required Permissions:
Action: settings:read
Scope: settings:auth.{provider}:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the all SSO settings

<a id="sso_settings.SSOSettings.get_sso_settings_by_provider"></a>

#### get\_sso\_settings\_by\_provider

```python
def get_sso_settings_by_provider(provider: str) -> dict
```

The method includes a functionality to get the SSO settings for the specified provider

**Arguments**:

- `provider` _str_ - Specify the provider
  
  Required Permissions:
- `Action` - settings:read
- `Scope` - settings:auth.{provider}:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding provider SSO settings

<a id="sso_settings.SSOSettings.update_sso_settings"></a>

#### update\_sso\_settings

```python
def update_sso_settings(provider: str, sso_setting: SSOSetting)
```

The method includes a functionality to update the SSO settings specified by the provider

**Arguments**:

- `provider` _str_ - Specify the provider
- `sso_setting` _SSOSetting_ - Specify the SSO setting
  
  Required Permissions:
- `Action` - settings:write
- `Scope` - settings:auth.{provider}:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="sso_settings.SSOSettings.delete_sso_settings"></a>

#### delete\_sso\_settings

```python
def delete_sso_settings(provider: str)
```

The method includes a functionality to delete the SSO settings specified by the provider

**Arguments**:

- `provider` _str_ - Specify the provider
  
  Required Permissions:
- `Action` - settings:write
- `Scope` - settings:auth.{provider}:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

