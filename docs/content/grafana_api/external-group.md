# Table of Contents

* [external\_group](#external_group)
  * [ExternalGroup](#external_group.ExternalGroup)
    * [get\_external\_groups](#external_group.ExternalGroup.get_external_groups)
    * [add\_external\_group](#external_group.ExternalGroup.add_external_group)
    * [remove\_external\_group](#external_group.ExternalGroup.remove_external_group)

<a id="external_group"></a>

# external\_group

<a id="external_group.ExternalGroup"></a>

## ExternalGroup Objects

```python
class ExternalGroup()
```

The class includes all necessary methods to access the Grafana external group API endpoints.

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="external_group.ExternalGroup.get_external_groups"></a>

#### get\_external\_groups

```python
def get_external_groups(team_id: int) -> list
```

The method includes a functionality to get the corresponding external groups specified by the team id

**Arguments**:

- `team_id` _int_ - Specify the team id
  
  Required Permissions:
- `Action` - teams.permissions:read
- `Scope` - teams:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the external groups

<a id="external_group.ExternalGroup.add_external_group"></a>

#### add\_external\_group

```python
def add_external_group(team_id: int, group_id: str)
```

The method includes a functionality to add the corresponding external groups specified by the team id and group id

**Arguments**:

- `team_id` _int_ - Specify the team id
- `group_id` _str_ - Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)
  
  Required Permissions:
- `Action` - teams.permissions:write
- `Scope` - teams:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the external groups

<a id="external_group.ExternalGroup.remove_external_group"></a>

#### remove\_external\_group

```python
def remove_external_group(team_id: int, group_id: str)
```

The method includes a functionality to remove the corresponding external groups specified by the team id and group id

**Arguments**:

- `team_id` _int_ - Specify the team id
- `group_id` _str_ - Specify the group id (e.g. cn=editors,ou=groups,dc=grafana,dc=org)
  
  Required Permissions:
- `Action` - teams.permissions:write
- `Scope` - teams:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the external groups

