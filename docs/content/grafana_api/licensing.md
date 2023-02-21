# Table of Contents

* [licensing](#licensing)
  * [Licensing](#licensing.Licensing)
    * [check\_license\_availability](#licensing.Licensing.check_license_availability)
    * [manually\_force\_license\_refresh](#licensing.Licensing.manually_force_license_refresh)
    * [remove\_license\_from\_database](#licensing.Licensing.remove_license_from_database)

<a id="licensing"></a>

# licensing

<a id="licensing.Licensing"></a>

## Licensing Objects

```python
class Licensing()
```

The class includes all necessary methods to access the Grafana licensing API endpoints. Be aware that the functionality is a Grafana ENTERPRISE v7.4+ feature

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="licensing.Licensing.check_license_availability"></a>

#### check\_license\_availability

```python
def check_license_availability()
```

The method includes a functionality to checks if a valid license is available

Required Permissions:
Action: licensing:read
Scope: N/A

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _bool_ - Returns the result if the license is available or not

<a id="licensing.Licensing.manually_force_license_refresh"></a>

#### manually\_force\_license\_refresh

```python
def manually_force_license_refresh()
```

The method includes a functionality to manually ask license issuer for a new token

Required Permissions:
Action: licensing:update
Scope: N/A

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of license refresh call

<a id="licensing.Licensing.remove_license_from_database"></a>

#### remove\_license\_from\_database

```python
def remove_license_from_database()
```

The method includes a functionality to removes the license stored in the Grafana database

Required Permissions:
Action: licensing:delete
Scope: N/A

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of license refresh call

