# Table of Contents

* [api](#api)
  * [Api](#api.Api)
    * [call\_the\_api](#api.Api.call_the_api)
    * [prepare\_api\_string](#api.Api.prepare_api_string)
    * [create\_the\_http\_api\_client](#api.Api.create_the_http_api_client)

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
                 org_id_header: int = None,
                 disable_provenance_header: bool = False,
                 response_status_code: bool = False) -> any
```

The method execute a defined API call against the Grafana endpoints

**Arguments**:

- `api_call` _str_ - Specify the API call endpoint
- `method` _RequestsMethods_ - Specify the used method (default GET)
- `json_complete` _str_ - Specify the inserted JSON as string
- `org_id_header` _int_ - Specify the optional organization id as header for the corresponding API call
- `disable_provenance_header` _bool_ - Specify the optional disable provenance as header for the corresponding API call (default False)
- `response_status_code` _bool_ - Specify if the response should include the original status code (default False)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _any_ - Returns the value of the api call

<a id="api.Api.prepare_api_string"></a>

#### prepare\_api\_string

```python
@staticmethod
def prepare_api_string(query_string: str) -> str
```

The method includes a functionality to prepare the api string for the queries

**Arguments**:

- `query_string` _str_ - Specify the corresponding query string
  

**Returns**:

- `query_string` _str_ - Returns the adjusted query string

<a id="api.Api.create_the_http_api_client"></a>

#### create\_the\_http\_api\_client

```python
def create_the_http_api_client(
        headers: dict = None) -> Union[httpx.Client, httpx.AsyncClient]
```

The method includes a functionality to create the corresponding HTTP client

**Arguments**:

- `headers` _dict_ - Specify the optional inserted headers (Default None)
  

**Returns**:

- `client` _Union[httpx.Client, httpx.AsyncClient]_ - Returns the corresponding client

