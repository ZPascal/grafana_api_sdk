# Table of Contents

* [api](#api)
  * [Api](#api.Api)
    * [call\_the\_api](#api.Api.call_the_api)

<a id="api"></a>

# api

<a id="api.Api"></a>

## Api Objects

```python
class Api()
```

The class includes all necessary methods to make API calls to the Grafana API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="api.Api.call_the_api"></a>

#### call\_the\_api

```python
def call_the_api(api_call: str,
                 method: RequestsMethods = RequestsMethods.GET,
                 json_complete: str = None,
                 timeout: float = None,
                 org_id_header: int = None) -> any
```

The method execute a defined API call against the Grafana endpoints

**Arguments**:

- `api_call` _str_ - Specify the API call endpoint
- `method` _RequestsMethods_ - Specify the used method (default GET)
- `json_complete` _str_ - Specify the inserted JSON as string
- `timeout` _float_ - Specify the timeout for the corresponding API call
- `org_id_header` _int_ - Specify the optional organization id for the corresponding API call
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _any_ - Returns the value of the api call

