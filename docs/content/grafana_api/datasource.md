# Table of Contents

* [datasource](#datasource)
  * [Datasource](#datasource.Datasource)
    * [get\_all\_datasources](#datasource.Datasource.get_all_datasources)
    * [get\_datasource\_by\_id](#datasource.Datasource.get_datasource_by_id)
    * [get\_datasource\_by\_uid](#datasource.Datasource.get_datasource_by_uid)
    * [get\_datasource\_by\_name](#datasource.Datasource.get_datasource_by_name)
    * [get\_datasource\_id\_by\_name](#datasource.Datasource.get_datasource_id_by_name)
    * [create\_datasource](#datasource.Datasource.create_datasource)
    * [update\_datasource](#datasource.Datasource.update_datasource)
    * [delete\_datasource\_by\_id](#datasource.Datasource.delete_datasource_by_id)
    * [delete\_datasource\_by\_uid](#datasource.Datasource.delete_datasource_by_uid)
    * [delete\_datasource\_by\_name](#datasource.Datasource.delete_datasource_by_name)
    * [query\_datasource\_by\_id](#datasource.Datasource.query_datasource_by_id)
  * [DatasourcePermissions](#datasource.DatasourcePermissions)
    * [get\_datasource\_permissions\_by\_uid](#datasource.DatasourcePermissions.get_datasource_permissions_by_uid)
    * [update\_datasource\_user\_access\_by\_uid](#datasource.DatasourcePermissions.update_datasource_user_access_by_uid)
    * [update\_datasource\_team\_access\_by\_uid](#datasource.DatasourcePermissions.update_datasource_team_access_by_uid)
    * [update\_datasource\_basic\_role\_access\_by\_uid](#datasource.DatasourcePermissions.update_datasource_basic_role_access_by_uid)
  * [DatasourceLegacyPermissions](#datasource.DatasourceLegacyPermissions)
    * [enable\_datasource\_permissions](#datasource.DatasourceLegacyPermissions.enable_datasource_permissions)
    * [disable\_datasource\_permissions](#datasource.DatasourceLegacyPermissions.disable_datasource_permissions)
    * [get\_datasource\_permissions](#datasource.DatasourceLegacyPermissions.get_datasource_permissions)
    * [add\_datasource\_permissions](#datasource.DatasourceLegacyPermissions.add_datasource_permissions)
    * [delete\_datasource\_permissions](#datasource.DatasourceLegacyPermissions.delete_datasource_permissions)
  * [DatasourceQueryResourceCaching](#datasource.DatasourceQueryResourceCaching)
    * [get\_datasource\_cache](#datasource.DatasourceQueryResourceCaching.get_datasource_cache)
    * [enable\_datasource\_cache](#datasource.DatasourceQueryResourceCaching.enable_datasource_cache)
    * [disable\_datasource\_cache](#datasource.DatasourceQueryResourceCaching.disable_datasource_cache)
    * [clean\_datasource\_cache](#datasource.DatasourceQueryResourceCaching.clean_datasource_cache)
    * [update\_datasource\_cache](#datasource.DatasourceQueryResourceCaching.update_datasource_cache)
  * [DatasourceLabelBasedAccessControl](#datasource.DatasourceLabelBasedAccessControl)
    * [get\_lbac\_rules\_for\_datasource](#datasource.DatasourceLabelBasedAccessControl.get_lbac_rules_for_datasource)
    * [update\_lbac\_rules\_for\_datasource](#datasource.DatasourceLabelBasedAccessControl.update_lbac_rules_for_datasource)

<a id="datasource"></a>

# datasource

<a id="datasource.Datasource"></a>

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

<a id="datasource.Datasource.get_all_datasources"></a>

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

<a id="datasource.Datasource.get_datasource_by_id"></a>

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

<a id="datasource.Datasource.get_datasource_by_uid"></a>

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

<a id="datasource.Datasource.get_datasource_by_name"></a>

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

<a id="datasource.Datasource.get_datasource_id_by_name"></a>

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

<a id="datasource.Datasource.create_datasource"></a>

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

<a id="datasource.Datasource.update_datasource"></a>

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

<a id="datasource.Datasource.delete_datasource_by_id"></a>

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

<a id="datasource.Datasource.delete_datasource_by_uid"></a>

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

<a id="datasource.Datasource.delete_datasource_by_name"></a>

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

<a id="datasource.Datasource.query_datasource_by_id"></a>

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

<a id="datasource.DatasourcePermissions"></a>

## DatasourcePermissions Objects

```python
class DatasourcePermissions()
```

The class includes all necessary methods to access the Grafana datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="datasource.DatasourcePermissions.get_datasource_permissions_by_uid"></a>

#### get\_datasource\_permissions\_by\_uid

```python
def get_datasource_permissions_by_uid(uid: str) -> list
```

The method includes a functionality to get the datasource permissions specified by the datasource uid. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources.permissions:read
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the datasource permissions

<a id="datasource.DatasourcePermissions.update_datasource_user_access_by_uid"></a>

#### update\_datasource\_user\_access\_by\_uid

```python
def update_datasource_user_access_by_uid(
        uid: str, id: int, datasource_user_permission: DatasourcePermission)
```

The method includes a functionality to update the datasource permission specified by the datasource uid and the user id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
- `id` _int_ - Specify the id of the user
- `datasource_user_permission` _DatasourcePermission_ - Specify the datasource user permission
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="datasource.DatasourcePermissions.update_datasource_team_access_by_uid"></a>

#### update\_datasource\_team\_access\_by\_uid

```python
def update_datasource_team_access_by_uid(
        uid: str, id: int, datasource_team_permission: DatasourcePermission)
```

The method includes a functionality to update the datasource permission specified by the datasource uid and the team id. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
- `id` _int_ - Specify the id of the team
- `datasource_team_permission` _DatasourcePermission_ - Specify the datasource team permission
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="datasource.DatasourcePermissions.update_datasource_basic_role_access_by_uid"></a>

#### update\_datasource\_basic\_role\_access\_by\_uid

```python
def update_datasource_basic_role_access_by_uid(
        uid: str, build_in_role_name: str,
        datasource_team_permission: DatasourcePermission)
```

The method includes a functionality to update the datasource permission specified by the datasource uid and the build in role name. The functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
- `build_in_role_name` _str_ - Specify the build in role name
- `datasource_team_permission` _DatasourcePermission_ - Specify the datasource team permission
  
  Required Permissions:
- `Action` - datasources.permissions:write
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="datasource.DatasourceLegacyPermissions"></a>

## DatasourceLegacyPermissions Objects

```python
class DatasourceLegacyPermissions()
```

The class includes all necessary methods to access the Grafana legacy datasource permissions API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="datasource.DatasourceLegacyPermissions.enable_datasource_permissions"></a>

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

<a id="datasource.DatasourceLegacyPermissions.disable_datasource_permissions"></a>

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

<a id="datasource.DatasourceLegacyPermissions.get_datasource_permissions"></a>

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

<a id="datasource.DatasourceLegacyPermissions.add_datasource_permissions"></a>

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

<a id="datasource.DatasourceLegacyPermissions.delete_datasource_permissions"></a>

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

<a id="datasource.DatasourceQueryResourceCaching"></a>

## DatasourceQueryResourceCaching Objects

```python
class DatasourceQueryResourceCaching()
```

The class includes all necessary methods to access the Grafana datasource query and resource caching API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana ENTERPRISE feature

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="datasource.DatasourceQueryResourceCaching.get_datasource_cache"></a>

#### get\_datasource\_cache

```python
def get_datasource_cache(uid: str) -> dict
```

The method includes a functionality to get the datasource cache config specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources.caching:write
- `Scope` - datasources:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="datasource.DatasourceQueryResourceCaching.enable_datasource_cache"></a>

#### enable\_datasource\_cache

```python
def enable_datasource_cache(uid: str) -> dict
```

The method includes a functionality to enable the datasource cache specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources.caching:read
- `Scope` - datasources:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="datasource.DatasourceQueryResourceCaching.disable_datasource_cache"></a>

#### disable\_datasource\_cache

```python
def disable_datasource_cache(uid: str) -> dict
```

The method includes a functionality to disable the datasource cache specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources.caching:write
- `Scope` - datasources:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="datasource.DatasourceQueryResourceCaching.clean_datasource_cache"></a>

#### clean\_datasource\_cache

```python
def clean_datasource_cache(uid: str) -> dict
```

The method includes a functionality to clean the datasource cache of all data sources with caching enabled. The uid of the datasource will only be used to return the configuration for that data source

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources.caching:write
- `Scope` - datasources:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="datasource.DatasourceQueryResourceCaching.update_datasource_cache"></a>

#### update\_datasource\_cache

```python
def update_datasource_cache(uid: str,
                            datasource_cache: DatasourceCache) -> dict
```

The method includes a functionality to update the datasource cache specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
- `datasource_cache` _DatasourceCache_ - Specif the datasource cache object
  
  Required Permissions:
- `Action` - datasources.caching:write
- `Scope` - datasources:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

<a id="datasource.DatasourceLabelBasedAccessControl"></a>

## DatasourceLabelBasedAccessControl Objects

```python
class DatasourceLabelBasedAccessControl()
```

The class includes all necessary methods to access the Grafana datasource label based access control for teams API endpoints. It's required that the API token got the corresponding datasource access rights. Please check the used methods docstring for the necessary access rights. The functionality is a Grafana Cloud feature. Only cloud Loki data sources are supported

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="datasource.DatasourceLabelBasedAccessControl.get_lbac_rules_for_datasource"></a>

#### get\_lbac\_rules\_for\_datasource

```python
def get_lbac_rules_for_datasource(uid: str) -> list
```

The method includes a functionality to get all datasource label based access control rules for team specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources:read
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all LBAC rules

<a id="datasource.DatasourceLabelBasedAccessControl.update_lbac_rules_for_datasource"></a>

#### update\_lbac\_rules\_for\_datasource

```python
def update_lbac_rules_for_datasource(uid: str) -> dict
```

The method includes a functionality to enable the datasource cache specified by the datasource uid

**Arguments**:

- `uid` _str_ - Specify the uid of the datasource
  
  Required Permissions:
- `Action` - datasources:write, datasources.permissions:write
- `Scope` - [datasources:*, datasources:uid:*, datasources:uid:<id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a datasource

