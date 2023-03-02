# Table of Contents

* [rbac](#rbac)
  * [RBAC](#rbac.RBAC)
    * [get\_status](#rbac.RBAC.get_status)
    * [get\_all\_roles](#rbac.RBAC.get_all_roles)
    * [get\_role](#rbac.RBAC.get_role)
    * [create\_role](#rbac.RBAC.create_role)
    * [update\_role](#rbac.RBAC.update_role)
    * [delete\_role](#rbac.RBAC.delete_role)
    * [get\_user\_assigned\_roles](#rbac.RBAC.get_user_assigned_roles)
    * [get\_user\_assigned\_permissions](#rbac.RBAC.get_user_assigned_permissions)
    * [add\_user\_role\_assignment](#rbac.RBAC.add_user_role_assignment)
    * [remove\_user\_role\_assignment](#rbac.RBAC.remove_user_role_assignment)
    * [update\_user\_role\_assignments](#rbac.RBAC.update_user_role_assignments)
    * [get\_service\_account\_assigned\_roles](#rbac.RBAC.get_service_account_assigned_roles)
    * [get\_service\_account\_assigned\_permissions](#rbac.RBAC.get_service_account_assigned_permissions)
    * [add\_service\_account\_role\_assignment](#rbac.RBAC.add_service_account_role_assignment)
    * [remove\_service\_account\_role\_assignment](#rbac.RBAC.remove_service_account_role_assignment)
    * [update\_service\_account\_role\_assignments](#rbac.RBAC.update_service_account_role_assignments)
    * [get\_team\_assigned\_roles](#rbac.RBAC.get_team_assigned_roles)
    * [add\_team\_role\_assignment](#rbac.RBAC.add_team_role_assignment)
    * [remove\_team\_role\_assignment](#rbac.RBAC.remove_team_role_assignment)
    * [update\_team\_role\_assignments](#rbac.RBAC.update_team_role_assignments)
    * [reset\_basic\_roles\_to\_their\_default](#rbac.RBAC.reset_basic_roles_to_their_default)

<a id="rbac"></a>

# rbac

<a id="rbac.RBAC"></a>

## RBAC Objects

```python
class RBAC()
```

The class includes all necessary methods to access the Grafana RBAC API endpoints. Be aware that the functionality is a Grafana ENTERPRISE feature

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="rbac.RBAC.get_status"></a>

#### get\_status

```python
def get_status() -> bool
```

The method includes a functionality to get the status if role-based access control is enabled or not

Required Permissions:
Action: status:accesscontrol
Scope: services:accesscontrol

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _bool_ - Return a flag indicating if the role-based access control is enabled or not

<a id="rbac.RBAC.get_all_roles"></a>

#### get\_all\_roles

```python
def get_all_roles(include_hidden_roles: bool = False) -> list
```

The method includes a functionality gets all existing roles. The response contains all global and organization local roles, for the organization which user is signed in

**Arguments**:

- `include_hidden_roles` _bool_ - Specify if the output contains the hidden roles or not (default False)
  
  Required Permissions:
- `Action` - roles:read
- `Scope` - roles:*
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return all global and organization local roles

<a id="rbac.RBAC.get_role"></a>

#### get\_role

```python
def get_role(uid: str) -> dict
```

The method includes a functionality get a role specified by the uid

**Arguments**:

- `uid` _str_ - Specify the uid of the role
  
  Required Permissions:
- `Action` - roles:read
- `Scope` - roles:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Return the corresponding role

<a id="rbac.RBAC.create_role"></a>

#### create\_role

```python
def create_role(role_definition: CustomRole) -> dict
```

The method includes a functionality create a new custom role and maps given permissions to that role. Note that roles with the same prefix as Fixed roles can’t be created

Args:
    role_definition (CustomRole): Specify the corresponding role definition

Required Permissions:
    Action: roles:write
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    api_call (dict): Return the newly created role


<a id="rbac.RBAC.update_role"></a>

#### update\_role

```python
def update_role(uid: str, role_definition: CustomRole) -> dict
```

The method includes a functionality to update the role with the given uid, and its permissions. The operation is idempotent and all permissions of the role will be replaced based on the request content. You need to increment the version of the role with each update, otherwise the request will fail

Args:
    uid (str): Specify the corresponding uid of the custom role
    role_definition (CustomRole): Specify the corresponding role definition

Required Permissions:
    Action: roles:write
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    api_call (dict): Return the updated role


<a id="rbac.RBAC.delete_role"></a>

#### delete\_role

```python
def delete_role(uid: str, force: bool = False, global_role: bool = False)
```

The method includes a functionality to delete a role with the given uid

Args:
    uid (str): Specify the corresponding uid of the custom role
    force (bool): Specify the corresponding if the role will be deleted with all it’s assignments or not (default False)
    global_role (bool): Specify the corresponding if the role is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

Required Permissions:
    Action: roles:delete
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.get_user_assigned_roles"></a>

#### get\_user\_assigned\_roles

```python
def get_user_assigned_roles(user_id: int,
                            include_hidden_roles: bool = False) -> list
```

The method includes a functionality to get the roles that have been directly assigned to a given user specified by the user id. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin), and it does not include roles that have been inherited from a team

**Arguments**:

- `user_id` _int_ - Specify the corresponding user_id of the user
- `include_hidden_roles` _bool_ - Specify if the output contains the hidden roles or not (default False)
  
  Required Permissions:
- `Action` - users.roles:read
- `Scope` - users:id:<user ID>
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return the corresponding user roles

<a id="rbac.RBAC.get_user_assigned_permissions"></a>

#### get\_user\_assigned\_permissions

```python
def get_user_assigned_permissions(user_id: int) -> list
```

The method includes a functionality to get the permissions that have been directly assigned to a given user specified by the user id

**Arguments**:

- `user_id` _int_ - Specify the corresponding user_id of the user
  
  Required Permissions:
- `Action` - users.permissions:read
- `Scope` - users:id:<user ID>
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return the corresponding user permissions

<a id="rbac.RBAC.add_user_role_assignment"></a>

#### add\_user\_role\_assignment

```python
def add_user_role_assignment(user_id: int,
                             role_uid: str,
                             global_assignment: bool = False)
```

The method includes a functionality to assign a role to a specific user

Args:
    user_id (int): Specify the corresponding user_id of the user
    role_uid (str): Specify the corresponding uid of the role
    global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

Required Permissions:
    Action: users.roles:add
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.remove_user_role_assignment"></a>

#### remove\_user\_role\_assignment

```python
def remove_user_role_assignment(user_id: int, role_uid: str)
```

The method includes a functionality to revoke a role to a specific user

Args:
    user_id (int): Specify the corresponding user_id of the user
    role_uid (str): Specify the corresponding uid of the role

Required Permissions:
    Action: users.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.update_user_role_assignments"></a>

#### update\_user\_role\_assignments

```python
def update_user_role_assignments(user_id: int,
                                 role_uids: list,
                                 include_hidden_roles: bool = False,
                                 global_assignment: bool = False)
```

The method includes a functionality to update the user role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

Args:
    user_id (int): Specify the corresponding user_id of the user
    role_uids (list): Specify the corresponding uids of the role
    include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
    global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

Required Permissions:
    Action: users.roles:add, users.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.get_service_account_assigned_roles"></a>

#### get\_service\_account\_assigned\_roles

```python
def get_service_account_assigned_roles(service_account_id: int,
                                       include_hidden_roles: bool = False
                                       ) -> list
```

The method includes a functionality to get the roles that have been directly assigned to a given service account. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin)

**Arguments**:

- `service_account_id` _int_ - Specify the corresponding service_account_id of the service account
- `include_hidden_roles` _bool_ - Specify if the output contains the hidden roles or not (default False)
  
  Required Permissions:
- `Action` - users.roles:read
- `Scope` - users:id:<service account ID>
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return the corresponding service account roles

<a id="rbac.RBAC.get_service_account_assigned_permissions"></a>

#### get\_service\_account\_assigned\_permissions

```python
def get_service_account_assigned_permissions(service_account_id: int) -> list
```

The method includes a functionality to get the permissions that a given service account has

**Arguments**:

- `service_account_id` _int_ - Specify the corresponding service_account_id of the service account
  
  Required Permissions:
- `Action` - users.permissions:read
- `Scope` - users:id:<service account ID>
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return the corresponding service account permissions

<a id="rbac.RBAC.add_service_account_role_assignment"></a>

#### add\_service\_account\_role\_assignment

```python
def add_service_account_role_assignment(service_account_id: int,
                                        role_uid: str,
                                        global_assignment: bool = False)
```

The method includes a functionality to assign a role to a specific service account

Args:
    service_account_id (int): Specify the corresponding service_account_id of the service account
    role_uid (str): Specify the corresponding uid of the role
    global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

Required Permissions:
    Action: users.roles:add
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.remove_service_account_role_assignment"></a>

#### remove\_service\_account\_role\_assignment

```python
def remove_service_account_role_assignment(service_account_id: int,
                                           role_uid: str)
```

The method includes a functionality to revoke a role to a specific service account

Args:
    service_account_id (int): Specify the corresponding service_account_id of the service account
    role_uid (str): Specify the corresponding uid of the role

Required Permissions:
    Action: users.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.update_service_account_role_assignments"></a>

#### update\_service\_account\_role\_assignments

```python
def update_service_account_role_assignments(service_account_id: int,
                                            role_uids: list,
                                            include_hidden_roles: bool = False,
                                            global_assignment: bool = False)
```

The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

Args:
    service_account_id (int): Specify the corresponding service_account_id of the service account
    role_uids (list): Specify the corresponding uids of the role
    include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
    global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

Required Permissions:
    Action: users.roles:add, users.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.get_team_assigned_roles"></a>

#### get\_team\_assigned\_roles

```python
def get_team_assigned_roles(team_id: int,
                            include_hidden_roles: bool = False) -> list
```

The method includes a functionality to get that have been directly assigned to a given team.

**Arguments**:

- `team_id` _int_ - Specify the corresponding team_id of the team
- `include_hidden_roles` _bool_ - Specify if the output contains the hidden roles or not (default False)
  
  Required Permissions:
- `Action` - teams.roles:read
- `Scope` - teams:id:<team ID>
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Return the corresponding team roles

<a id="rbac.RBAC.add_team_role_assignment"></a>

#### add\_team\_role\_assignment

```python
def add_team_role_assignment(team_id: int, role_uid: str)
```

The method includes a functionality to assign a role to a specific team

Args:
    team_id (int): Specify the corresponding team_id of the team
    role_uid (str): Specify the corresponding uid of the role

Required Permissions:
    Action: teams.roles:add
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.remove_team_role_assignment"></a>

#### remove\_team\_role\_assignment

```python
def remove_team_role_assignment(team_id: int, role_uid: str)
```

The method includes a functionality to revoke a role to a specific team

Args:
    team_id (int): Specify the corresponding team_id of the team
    role_uid (str): Specify the corresponding uid of the role

Required Permissions:
    Action: teams.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.update_team_role_assignments"></a>

#### update\_team\_role\_assignments

```python
def update_team_role_assignments(team_id: int,
                                 role_uids: list,
                                 include_hidden_roles: bool = False)
```

The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

Args:
    team_id (int): Specify the corresponding team_id of the team
    role_uids (list): Specify the corresponding uids of the role
    include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

Required Permissions:
    Action: teams.roles:add, teams.roles:remove
    Scope: permissions:type:delegate

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="rbac.RBAC.reset_basic_roles_to_their_default"></a>

#### reset\_basic\_roles\_to\_their\_default

```python
def reset_basic_roles_to_their_default()
```

The method includes a functionality to reset basic roles permissions to their default

Required Permissions:
    Action: roles:write
    Scope: permissions:type:escalate

Raises:
    Exception: Unspecified error by executing the API call

Returns:
    None


