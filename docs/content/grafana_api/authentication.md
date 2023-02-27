# Table of Contents

* [authentication](#authentication)
  * [Authentication](#authentication.Authentication)
    * [get\_api\_tokens](#authentication.Authentication.get_api_tokens)
    * [create\_api\_token](#authentication.Authentication.create_api_token)
    * [delete\_api\_token](#authentication.Authentication.delete_api_token)

<a id="authentication"></a>

# authentication

<a id="authentication.Authentication"></a>

## Authentication Objects

```python
class Authentication()
```

The class includes all necessary methods to access the Grafana authentication API endpoints.

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="authentication.Authentication.get_api_tokens"></a>

#### get\_api\_tokens

```python
def get_api_tokens(org_id_header: int = None) -> list
```

The method includes a functionality to get the corresponding api tokens of the organisation

**Arguments**:

- `org_id_header` _int_ - Specify the org id as header to execute call for that specific organisation
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the result of the API token call

<a id="authentication.Authentication.create_api_token"></a>

#### create\_api\_token

```python
def create_api_token(name: str,
                     role: str,
                     seconds_to_live: int = 0,
                     org_id_header: int = None) -> dict
```

The method includes a functionality to create a corresponding api tokens of the organisation specified by the name and role

**Arguments**:

- `name` _str_ - Specify the token name
- `role` _str_ - Specify the access level/Grafana Role for the token. Can be one of the following values: Viewer, Editor or Admin
- `seconds_to_live` _int_ - Specify the seconds of the token expiration in seconds. If it is a positive number an expiration date for the key is set. If it is null, zero or is omitted completely (unless api_key_max_seconds_to_live configuration option is set) the key will never expire (default 0)
- `org_id_header` _int_ - Specify the org id as header to execute call for that specific organisation
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the API token object

<a id="authentication.Authentication.delete_api_token"></a>

#### delete\_api\_token

```python
def delete_api_token(token_id: int, org_id_header: int = None)
```

The method includes a functionality to delete a corresponding api token specified by the token id

**Arguments**:

- `token_id` _int_ - Specify the token id
- `org_id_header` _int_ - Specify the org id as header to execute call for that specific organisation
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

