# Table of Contents

* [organisation](#organisation)
  * [Organisation](#organisation.Organisation)
    * [get\_current\_organization](#organisation.Organisation.get_current_organization)
    * [get\_all\_users\_by\_the\_current\_organization](#organisation.Organisation.get_all_users_by_the_current_organization)
    * [get\_all\_users\_by\_the\_current\_organization\_lookup](#organisation.Organisation.get_all_users_by_the_current_organization_lookup)
    * [update\_organization\_user\_role\_by\_user\_id](#organisation.Organisation.update_organization_user_role_by_user_id)
    * [delete\_organization\_user\_by\_user\_id](#organisation.Organisation.delete_organization_user_by_user_id)
    * [update\_current\_organization](#organisation.Organisation.update_current_organization)
    * [add\_new\_user\_to\_current\_organization](#organisation.Organisation.add_new_user_to_current_organization)
  * [OrganisationAdmin](#organisation.OrganisationAdmin)
    * [get\_organization\_by\_id](#organisation.OrganisationAdmin.get_organization_by_id)
    * [get\_organization\_by\_name](#organisation.OrganisationAdmin.get_organization_by_name)
    * [get\_organizations](#organisation.OrganisationAdmin.get_organizations)
    * [create\_organization](#organisation.OrganisationAdmin.create_organization)
    * [update\_organization](#organisation.OrganisationAdmin.update_organization)
    * [delete\_organization](#organisation.OrganisationAdmin.delete_organization)
    * [get\_organization\_users](#organisation.OrganisationAdmin.get_organization_users)
    * [add\_organization\_user](#organisation.OrganisationAdmin.add_organization_user)
    * [update\_organization\_user](#organisation.OrganisationAdmin.update_organization_user)
    * [delete\_organization\_user](#organisation.OrganisationAdmin.delete_organization_user)

<a id="organisation"></a>

# organisation

<a id="organisation.Organisation"></a>

## Organisation Objects

```python
class Organisation()
```

The class includes all necessary methods to access the Grafana organisation API endpoint

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="organisation.Organisation.get_current_organization"></a>

#### get\_current\_organization

```python
def get_current_organization() -> dict
```

The method includes a functionality to get the current organization

Required Permissions:
Action: orgs:read
Scope: N/A

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the current organization

<a id="organisation.Organisation.get_all_users_by_the_current_organization"></a>

#### get\_all\_users\_by\_the\_current\_organization

```python
def get_all_users_by_the_current_organization() -> list
```

The method includes a functionality to get all users from the current organization

Required Permissions:
Action: org.users:read
Scope: users:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the users of the current organization

<a id="organisation.Organisation.get_all_users_by_the_current_organization_lookup"></a>

#### get\_all\_users\_by\_the\_current\_organization\_lookup

```python
def get_all_users_by_the_current_organization_lookup() -> list
```

The method includes a functionality to get the lookup information of all users from the current organization

Required Permissions:
Action: org.users:read
Scope: users:*

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the users of the current organization

<a id="organisation.Organisation.update_organization_user_role_by_user_id"></a>

#### update\_organization\_user\_role\_by\_user\_id

```python
def update_organization_user_role_by_user_id(user_id: int, role: str)
```

The method includes a functionality to update the current organization user by the user id

**Arguments**:

- `user_id` _int_ - Specify the id of the user
- `role` _str_ - Specify the role of the user
  
  Required Permissions:
- `Action` - org.users.role:update
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.Organisation.delete_organization_user_by_user_id"></a>

#### delete\_organization\_user\_by\_user\_id

```python
def delete_organization_user_by_user_id(user_id: int)
```

The method includes a functionality to delete the current organization user by the user id

**Arguments**:

- `user_id` _int_ - Specify the id of the user
  
  Required Permissions:
- `Action` - org.users:remove
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.Organisation.update_current_organization"></a>

#### update\_current\_organization

```python
def update_current_organization(name: str)
```

The method includes a functionality to update the current organization

**Arguments**:

- `name` _str_ - Specify the new name of the current organization
  
  Required Permissions:
- `Action` - orgs:write
- `Scope` - N/A
  
  Raises
- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.Organisation.add_new_user_to_current_organization"></a>

#### add\_new\_user\_to\_current\_organization

```python
def add_new_user_to_current_organization(login_or_email: str,
                                         role: str) -> int
```

The method includes a functionality to add a new user to the current organization

**Arguments**:

- `login_or_email` _str_ - Specify the added user
- `role` _str_ - Specify the added role for the user
  
  Required Permissions:
- `Action` - org.users:add
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `user_id` _int_ - Returns the id of the created user

<a id="organisation.OrganisationAdmin"></a>

## OrganisationAdmin Objects

```python
class OrganisationAdmin()
```

The class includes all necessary methods to access the Grafana organisation Admin API endpoint. Be aware that all functionalities inside the class only working with basic authentication (username and password)

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="organisation.OrganisationAdmin.get_organization_by_id"></a>

#### get\_organization\_by\_id

```python
def get_organization_by_id(org_id: int) -> dict
```

The method includes a functionality to get an organization by the id

**Arguments**:

- `org_id` _int_ - Specify the organization id
  
  Required Permissions:
- `Action` - orgs:read
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the organization as dict

<a id="organisation.OrganisationAdmin.get_organization_by_name"></a>

#### get\_organization\_by\_name

```python
def get_organization_by_name(name: str) -> dict
```

The method includes a functionality to get an organization by the name

**Arguments**:

- `name` _str_ - Specify the organization name
  
  Required Permissions:
- `Action` - orgs:read
- `Scope` - N/A
- `Note` - Needs to be assigned globally.
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the organization as dict

<a id="organisation.OrganisationAdmin.get_organizations"></a>

#### get\_organizations

```python
def get_organizations() -> list
```

The method includes a functionality to get all organizations

Required Permissions:
Action: orgs:read
Scope: N/A
Note: Needs to be assigned globally.

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all organizations as list

<a id="organisation.OrganisationAdmin.create_organization"></a>

#### create\_organization

```python
def create_organization(name: str) -> int
```

The method includes a functionality to create an organization

**Arguments**:

- `name` _str_ - Specify the organization name
  
  Required Permissions:
- `Action` - orgs:create
- `Scope` - N/A
- `Note` - Needs to be assigned globally.
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `org_id` _int_ - Returns the id of the created organization

<a id="organisation.OrganisationAdmin.update_organization"></a>

#### update\_organization

```python
def update_organization(org_id: int, name: str)
```

The method includes a functionality to update an organization

**Arguments**:

- `org_id` _int_ - Specify the organization id
- `name` _str_ - Specify the organization name
  
  Required Permissions:
- `Action` - orgs:write
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.OrganisationAdmin.delete_organization"></a>

#### delete\_organization

```python
def delete_organization(org_id: int)
```

The method includes a functionality to delete an organization

**Arguments**:

- `org_id` _int_ - Specify the organization id
  
  Required Permissions:
- `Action` - orgs:delete
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.OrganisationAdmin.get_organization_users"></a>

#### get\_organization\_users

```python
def get_organization_users(org_id: int) -> list
```

The method includes a functionality to get all organization users specified by the organization id

**Arguments**:

- `org_id` _int_ - Specify the organization id
  
  Required Permissions:
- `Action` - org.users:read
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all organization users as list

<a id="organisation.OrganisationAdmin.add_organization_user"></a>

#### add\_organization\_user

```python
def add_organization_user(org_id: int, login_or_email: str, role: str) -> int
```

The method includes a functionality to add a user to an organization

**Arguments**:

- `org_id` _int_ - Specify the organization id
- `login_or_email` _str_ - Specify the added user
- `role` _str_ - Specify the added role for the user
  
  Required Permissions:
- `Action` - org.users:add
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `user_id` _int_ - Returns the added user id

<a id="organisation.OrganisationAdmin.update_organization_user"></a>

#### update\_organization\_user

```python
def update_organization_user(org_id: int, user_id: int, role: str)
```

The method includes a functionality to update organization user specified by the organization id, the user_id and the role

**Arguments**:

- `org_id` _int_ - Specify the organization id
- `user_id` _int_ - Specify the user id
- `role` _str_ - Specify the added role for the user
  
  Required Permissions:
- `Action` - org.users.role:update
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="organisation.OrganisationAdmin.delete_organization_user"></a>

#### delete\_organization\_user

```python
def delete_organization_user(org_id: int, user_id: int)
```

The method includes a functionality to remove an organization users specified by the organization id and the user id

**Arguments**:

- `org_id` _int_ - Specify the organization id
- `user_id` _int_ - Specify the user id
  
  Required Permissions:
- `Action` - org.users:remove
- `Scope` - users:*
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

