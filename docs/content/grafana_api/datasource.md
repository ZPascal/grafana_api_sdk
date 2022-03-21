# Table of Contents

* [grafana\_api.datasource](#grafana_api.datasource)
  * [Datasource](#grafana_api.datasource.Datasource)
    * [get\_all\_datasources](#grafana_api.datasource.Datasource.get_all_datasources)
    * [get\_datasource\_by\_id](#grafana_api.datasource.Datasource.get_datasource_by_id)
    * [get\_datasource\_by\_uid](#grafana_api.datasource.Datasource.get_datasource_by_uid)
    * [get\_datasource\_by\_name](#grafana_api.datasource.Datasource.get_datasource_by_name)
    * [get\_datasource\_id\_by\_name](#grafana_api.datasource.Datasource.get_datasource_id_by_name)
    * [create\_datasource](#grafana_api.datasource.Datasource.create_datasource)
    * [update\_datasource](#grafana_api.datasource.Datasource.update_datasource)
    * [delete\_datasource\_by\_id](#grafana_api.datasource.Datasource.delete_datasource_by_id)
    * [delete\_datasource\_by\_uid](#grafana_api.datasource.Datasource.delete_datasource_by_uid)
    * [delete\_datasource\_by\_name](#grafana_api.datasource.Datasource.delete_datasource_by_name)
    * [query\_datasource\_by\_id](#grafana_api.datasource.Datasource.query_datasource_by_id)
    * [enable\_datasource\_permissions](#grafana_api.datasource.Datasource.enable_datasource_permissions)
    * [disable\_datasource\_permissions](#grafana_api.datasource.Datasource.disable_datasource_permissions)
    * [get\_datasource\_permissions](#grafana_api.datasource.Datasource.get_datasource_permissions)
    * [add\_datasource\_permissions](#grafana_api.datasource.Datasource.add_datasource_permissions)
    * [delete\_datasource\_permissions](#grafana_api.datasource.Datasource.delete_datasource_permissions)

<a id="grafana_api.datasource"></a>

# grafana\_api.datasource

<a id="grafana_api.datasource.Datasource"></a>

## Datasource Objects

```python
class Datasource()
```

The class includes all necessary methods to access the Grafana datasource API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="grafana_api.datasource.Datasource.get_all_datasources"></a>

#### get\_all\_datasources

```python
def get_all_datasources() -> list
```

The method includes a functionality to get all datasources

Required Permissions:
Action: datasources:read
Scope: datasources:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of all datasources

<a id="grafana_api.datasource.Datasource.get_datasource_by_id"></a>

#### get\_datasource\_by\_id

```python
def get_datasource_by_id(datasource_id: int) -> dict
```

The method includes a functionality to get the datasource specified by the datasource id

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
  
  Required Permissions:
- `Action` - datasources:read
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="grafana_api.datasource.Datasource.get_datasource_by_uid"></a>

#### get\_datasource\_by\_uid

```python
def get_datasource_by_uid(uid: str) -> dict
```

The method includes a functionality to get the datasource specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources:read
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<uid>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="grafana_api.datasource.Datasource.get_datasource_by_name"></a>

#### get\_datasource\_by\_name

```python
def get_datasource_by_name(name: str) -> dict
```

The method includes a functionality to get the datasource specified by the datasource name

**Arguments**:

- `name` _str_ - Specify the name of the datasource
  
  Required Permissions:
- `Action` - datasources:read
- `Scope` - [datasources:*, datasources:name:*, datasources:name:<name>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="grafana_api.datasource.Datasource.get_datasource_id_by_name"></a>

#### get\_datasource\_id\_by\_name

```python
def get_datasource_id_by_name(name: str) -> int
```

The method includes a functionality to get the datasource id specified by the datasource name

**Arguments**:

- `name` _str_ - Specify the name of the datasource
  
  Required Permissions:
- `Action` - datasources:read
- `Scope` - [datasources:*, datasources:name:*, datasources:name:<name>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _int_ - Returns a datasource id

<a id="grafana_api.datasource.Datasource.create_datasource"></a>

#### create\_datasource

```python
def create_datasource(data_source: dict)
```

The method includes a functionality to create a datasource specified by the datasource as dict

**Arguments**:

- `data_source` _dict_ - Specify the datasource as dict
  
  Required Permissions:
- `Action` - datasources:create
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.update_datasource"></a>

#### update\_datasource

```python
def update_datasource(datasource_id: int, data_source: dict)
```

The method includes a functionality to update a datasource specified by the datasource as dict and the datasource id

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
- `data_source` _dict_ - Specify the datasource as dict
  
  Required Permissions:
- `Action` - datasources:write
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.delete_datasource_by_id"></a>

#### delete\_datasource\_by\_id

```python
def delete_datasource_by_id(datasource_id: int)
```

The method includes a functionality to delete a datasource specified by the datasource id

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
  
  Required Permissions:
- `Action` - datasources:delete
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.delete_datasource_by_uid"></a>

#### delete\_datasource\_by\_uid

```python
def delete_datasource_by_uid(uid: str)
```

The method includes a functionality to delete a datasource specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources:delete
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<uid>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.delete_datasource_by_name"></a>

#### delete\_datasource\_by\_name

```python
def delete_datasource_by_name(name: str)
```

The method includes a functionality to delete a datasource specified by the datasource name

**Arguments**:

- `name` _str_ - Specify the name of the datasource
  
  Required Permissions:
- `Action` - datasources:delete
- `Scope` - [datasources:*, datasources:name:*, datasources:name:<name>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.query_datasource_by_id"></a>

#### query\_datasource\_by\_id

```python
def query_datasource_by_id(time: str, to: str,
                           datasource_queries: list) -> dict
```

The method includes a functionality to execute a queries inside the datasource itself specified by the datasource id

**Arguments**:

- `from` _str_ - Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
- `to` _str_ - Specify the name of the absolute in epoch timestamps in milliseconds or relative using Grafana time units. For example, now-1h
- `datasource_queries` _list_ - Specify a list of execution queries based on the DatasourceQuery class
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of the specified query

<a id="grafana_api.datasource.Datasource.enable_datasource_permissions"></a>

#### enable\_datasource\_permissions

```python
def enable_datasource_permissions(datasource_id: int)
```

The method includes a functionality to enable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.disable_datasource_permissions"></a>

#### disable\_datasource\_permissions

```python
def disable_datasource_permissions(datasource_id: int)
```

The method includes a functionality to disable datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.get_datasource_permissions"></a>

#### get\_datasource\_permissions

```python
def get_datasource_permissions(datasource_id: int) -> dict
```

The method includes a functionality to get the datasource permissions specified by the datasource id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
  
  Required Permissions:
- `Action` - datasources.permissions:read
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the datasource permissions

<a id="grafana_api.datasource.Datasource.add_datasource_permissions"></a>

#### add\_datasource\_permissions

```python
def add_datasource_permissions(datasource_id: int,
                               datasource_permission: dict)
```

The method includes a functionality to add datasource permission specified by the datasource id and the datasource permission dict. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
- `datasource_permission` _dict_ - Specify the permission of the datasource
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="grafana_api.datasource.Datasource.delete_datasource_permissions"></a>

#### delete\_datasource\_permissions

```python
def delete_datasource_permissions(datasource_id: int, permission_id: int)
```

The method includes a functionality to delete datasource permission specified by the datasource id and the permission id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `datasource_id` _int_ - Specify the id of the datasource
- `permission_id` _id_ - Specify the permission id
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:id:*, datasources:id:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

