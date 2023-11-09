# Table of Contents

* [team](#team)
  * [Team](#team.Team)
    * [search\_team](#team.Team.search_team)
    * [get\_team\_by\_id](#team.Team.get_team_by_id)
    * [add\_team](#team.Team.add_team)
    * [update\_team](#team.Team.update_team)
    * [delete\_team\_by\_id](#team.Team.delete_team_by_id)
    * [get\_team\_members](#team.Team.get_team_members)
    * [add\_team\_member](#team.Team.add_team_member)
    * [delete\_team\_member](#team.Team.delete_team_member)
    * [get\_team\_preferences](#team.Team.get_team_preferences)
    * [update\_team\_preferences](#team.Team.update_team_preferences)
    * [get\_external\_groups](#team.Team.get_external_groups)
    * [add\_external\_group](#team.Team.add_external_group)
    * [remove\_external\_group](#team.Team.remove_external_group)

<a id="team"></a>

# team

<a id="team.Team"></a>

## Team Objects

```python
class Team()
```

The class includes all necessary methods to access the Grafana team API endpoints. Be aware that all functionalities inside the class only working with the corresponding access rights, please check the following page for details: https://grafana.com/docs/grafana/latest/http_api/team/`team`-api & https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/`team`-sync-api

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="team.Team.search_team"></a>

#### search\_team

```python
def search_team(results_per_page: int = 1000,
                pages: int = 1,
                query: str = None) -> dict
```

The method includes a functionality to get the organization teams specified by the optional pagination functionality

Required Permissions:
Action: teams:read
Scope: teams:*

**Arguments**:

- `results_per_page` _int_ - Specify the results_per_page as integer (default 1000)
- `pages` _int_ - Specify the pages as integer (default 1)
- `query` _str_ - Specify the query (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the organization teams

<a id="team.Team.get_team_by_id"></a>

#### get\_team\_by\_id

```python
def get_team_by_id(id: int) -> dict
```

The method includes a functionality to get the organization team specified by the id

Required Permissions:
Action: teams:read
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the id of the team
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the organization team

<a id="team.Team.add_team"></a>

#### add\_team

```python
def add_team(team: TeamObject) -> int
```

The method includes a functionality to add an organization team specified by the TeamObject

Required Permissions:
Action: teams:create
Scope: N/A

**Arguments**:

- `team` _TeamObject_ - Specify the team
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `team_id` _int_ - Returns the team id

<a id="team.Team.update_team"></a>

#### update\_team

```python
def update_team(id: int, name: str, email: str)
```

The method includes a functionality to update an organization team specified by the team_id, name and email

Required Permissions:
Action: teams:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `name` _str_ - Specify the team name
- `email` _str_ - Specify the team email
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.delete_team_by_id"></a>

#### delete\_team\_by\_id

```python
def delete_team_by_id(id: int)
```

The method includes a functionality to delete an organization team specified by the team_id

Required Permissions:
Action: teams:delete
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.get_team_members"></a>

#### get\_team\_members

```python
def get_team_members(id: int) -> list
```

The method includes a functionality to get all organization team users specified by the team_id

Required Permissions:
Action: teams.permissions:read
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the organization team members

<a id="team.Team.add_team_member"></a>

#### add\_team\_member

```python
def add_team_member(id: int, user_id: int)
```

The method includes a functionality to add an organization team user specified by the team_id and the user_id

Required Permissions:
Action: teams.permissions:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `user_id` _int_ - Specify the user id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.delete_team_member"></a>

#### delete\_team\_member

```python
def delete_team_member(id: int, user_id: int)
```

The method includes a functionality to delete an organization team user specified by the team_id and the user_id

Required Permissions:
Action: teams.permissions:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `user_id` _int_ - Specify the user id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.get_team_preferences"></a>

#### get\_team\_preferences

```python
def get_team_preferences(id: int) -> dict
```

The method includes a functionality to get the organization team preferences specified by the team_id

Required Permissions:
Action: teams:read
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the organization team preferences

<a id="team.Team.update_team_preferences"></a>

#### update\_team\_preferences

```python
def update_team_preferences(id: int,
                            theme: str = None,
                            timezone: str = None,
                            home_dashboard_id: int = 0,
                            home_dashboard_uid: str = None)
```

The method includes a functionality to update the organization team preferences specified by the team_id, theme, timezone and home_dashboard_id or home_dashboard_uid

Required Permissions:
Action: teams:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `theme` _str_ - Specify the team theme e.g. light or dark (default Grafana None)
- `timezone` _str_ - Specify the team timezone e.g. utc or browser (default Grafana None)
- `home_dashboard_id` _int_ - Specify the home team dashboard by id (default 0)
- `home_dashboard_uid` _str_ - Specify the home team dashboard by uid (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.get_external_groups"></a>

#### get\_external\_groups

```python
def get_external_groups(id: int) -> list
```

The method includes a functionality to get the team groups specified by the team_id. The functionality is a Grafana ENTERPRISE feature

Required Permissions:
Action: teams.permissions:read
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the organization team groups

<a id="team.Team.add_external_group"></a>

#### add\_external\_group

```python
def add_external_group(id: int, team_group: str)
```

The method includes a functionality to add a group to the team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

Required Permissions:
Action: teams.permissions:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `team_group` _str_ - Specify the team group
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="team.Team.remove_external_group"></a>

#### remove\_external\_group

```python
def remove_external_group(id: int, team_group: str)
```

The method includes a functionality to remove a group from a team specified by the team_id and the team_group. The functionality is a Grafana ENTERPRISE feature

Required Permissions:
Action: teams.permissions:write
Scope: teams:*

**Arguments**:

- `id` _int_ - Specify the team id
- `team_group` _str_ - Specify the team group
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

