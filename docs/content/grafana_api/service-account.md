# Table of Contents

* [service\_account](#service_account)
  * [ServiceAccount](#service_account.ServiceAccount)
    * [search\_service\_account](#service_account.ServiceAccount.search_service_account)
    * [get\_service\_account\_by\_id](#service_account.ServiceAccount.get_service_account_by_id)
    * [create\_service\_account](#service_account.ServiceAccount.create_service_account)
    * [update\_service\_account](#service_account.ServiceAccount.update_service_account)
    * [delete\_service\_account](#service_account.ServiceAccount.delete_service_account)
    * [get\_service\_account\_tokens\_by\_id](#service_account.ServiceAccount.get_service_account_tokens_by_id)
    * [create\_service\_account\_token\_by\_id](#service_account.ServiceAccount.create_service_account_token_by_id)
    * [delete\_service\_account\_token\_by\_id](#service_account.ServiceAccount.delete_service_account_token_by_id)
    * [migrate\_api\_keys\_to\_service\_accounts](#service_account.ServiceAccount.migrate_api_keys_to_service_accounts)
    * [migrate\_api\_key\_to\_service\_account](#service_account.ServiceAccount.migrate_api_key_to_service_account)
    * [get\_service\_account\_migration\_status](#service_account.ServiceAccount.get_service_account_migration_status)
    * [hide\_the\_api\_keys\_tab](#service_account.ServiceAccount.hide_the_api_keys_tab)
    * [revert\_service\_account\_token\_to\_api\_key](#service_account.ServiceAccount.revert_service_account_token_to_api_key)

<a id="service_account"></a>

# service\_account

<a id="service_account.ServiceAccount"></a>

## ServiceAccount Objects

```python
class ServiceAccount()
```

The class includes all necessary methods to access the Grafana service account API endpoints. Be aware that the functionality inside the class only works with basic authentication (username and password) and that the authenticated user is a Grafana Admin

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="service_account.ServiceAccount.search_service_account"></a>

#### search\_service\_account

```python
def search_service_account(results_per_page: int = 1000,
                           pages: int = 1,
                           query: str = None) -> dict
```

The method includes a functionality to get the service accounts specified by the optional pagination functionality

Required Permissions:
Action: serviceaccounts:read
Scope: global:serviceaccounts:*

**Arguments**:

- `results_per_page` _int_ - Specify the results_per_page as integer (default 1000)
- `pages` _int_ - Specify the pages as integer (default 1)
- `query` _str_ - Specify the query (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the service accounts

<a id="service_account.ServiceAccount.get_service_account_by_id"></a>

#### get\_service\_account\_by\_id

```python
def get_service_account_by_id(id: int) -> dict
```

The method includes a functionality to get a service account specified by the id

Required Permissions:
Action: serviceaccounts:read
Scope: serviceaccounts:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the service account

<a id="service_account.ServiceAccount.create_service_account"></a>

#### create\_service\_account

```python
def create_service_account(name: str, role: str) -> dict
```

The method includes a functionality to create a service account

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Arguments**:

- `name` _str_ - Specify the name of the service account
- `role` _str_ - Specify the role of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the created service account

<a id="service_account.ServiceAccount.update_service_account"></a>

#### update\_service\_account

```python
def update_service_account(id: int, name: str, role: str) -> dict
```

The method includes a functionality to update a service account specified by the id, name and role

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
- `name` _str_ - Specify the name of the service account
- `role` _str_ - Specify the role of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the service account

<a id="service_account.ServiceAccount.delete_service_account"></a>

#### delete\_service\_account

```python
def delete_service_account(id: int)
```

The method includes a functionality to delete a service account specified by the id

Required Permissions:
Action: serviceaccounts:delete
Scope: serviceaccounts:id:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="service_account.ServiceAccount.get_service_account_tokens_by_id"></a>

#### get\_service\_account\_tokens\_by\_id

```python
def get_service_account_tokens_by_id(id: int) -> list
```

The method includes a functionality to get a service account tokens specified by the id

Required Permissions:
Action: serviceaccounts:read
Scope: serviceaccounts:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the service account tokens

<a id="service_account.ServiceAccount.create_service_account_token_by_id"></a>

#### create\_service\_account\_token\_by\_id

```python
def create_service_account_token_by_id(id: int, name: str, role: str) -> dict
```

The method includes a functionality to create a service account token specified by the id

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
- `name` _str_ - Specify the name of the service account
- `role` _str_ - Specify the role of the service account
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the service account token

<a id="service_account.ServiceAccount.delete_service_account_token_by_id"></a>

#### delete\_service\_account\_token\_by\_id

```python
def delete_service_account_token_by_id(id: int, token_id: int)
```

The method includes a functionality to delete a service account token specified by the id

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
  token_id (int):
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="service_account.ServiceAccount.migrate_api_keys_to_service_accounts"></a>

#### migrate\_api\_keys\_to\_service\_accounts

```python
def migrate_api_keys_to_service_accounts()
```

The method includes a functionality to migrate all api keys to service accounts

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="service_account.ServiceAccount.migrate_api_key_to_service_account"></a>

#### migrate\_api\_key\_to\_service\_account

```python
def migrate_api_key_to_service_account(key_id: int)
```

The method includes a functionality to migrate an api key to a service account specified by the key id

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Arguments**:

- `key_id` _int_ - Specify the api key id of the api key
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="service_account.ServiceAccount.get_service_account_migration_status"></a>

#### get\_service\_account\_migration\_status

```python
def get_service_account_migration_status() -> bool
```

The method includes a functionality to get the corresponding api key migration status

Required Permissions:
Action: serviceaccounts:read
Scope: global:serviceaccounts:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the api key migration status

<a id="service_account.ServiceAccount.hide_the_api_keys_tab"></a>

#### hide\_the\_api\_keys\_tab

```python
def hide_the_api_keys_tab()
```

The method includes a functionality to hide the api keys tab inside the UI

Required Permissions:
Action: serviceaccounts:write
Scope: serviceaccounts:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="service_account.ServiceAccount.revert_service_account_token_to_api_key"></a>

#### revert\_service\_account\_token\_to\_api\_key

```python
def revert_service_account_token_to_api_key(id: int, key_id: int)
```

The method includes a functionality to revert a service account and transform it to the legacy api token specified by the service account id and the key id

Required Permissions:
Action: serviceaccounts:delete
Scope: serviceaccounts:id:*

**Arguments**:

- `id` _int_ - Specify the id of the service account
- `key_id` _int_ - Specify the api key id of the api key
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

