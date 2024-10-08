# Table of Contents

* [user](#user)
  * [User](#user.User)
    * [search\_users](#user.User.search_users)
    * [search\_users\_with\_paging](#user.User.search_users_with_paging)
    * [get\_user\_by\_id](#user.User.get_user_by_id)
    * [get\_user\_by\_username\_or\_email](#user.User.get_user_by_username_or_email)
    * [update\_user](#user.User.update_user)
    * [get\_user\_organizations](#user.User.get_user_organizations)
    * [get\_user\_teams](#user.User.get_user_teams)
    * [switch\_specific\_user\_context](#user.User.switch_specific_user_context)
  * [CurrentUser](#user.CurrentUser)
    * [get\_user](#user.CurrentUser.get_user)
    * [update\_password](#user.CurrentUser.update_password)
    * [switch\_current\_user\_context](#user.CurrentUser.switch_current_user_context)
    * [get\_user\_organizations](#user.CurrentUser.get_user_organizations)
    * [get\_user\_teams](#user.CurrentUser.get_user_teams)
    * [star\_a\_dashboard](#user.CurrentUser.star_a_dashboard)
    * [unstar\_a\_dashboard](#user.CurrentUser.unstar_a_dashboard)
    * [get\_auth\_tokens](#user.CurrentUser.get_auth_tokens)
    * [revoke\_auth\_token](#user.CurrentUser.revoke_auth_token)

<a id="user"></a>

# user

<a id="user.User"></a>

## User Objects

```python
class User()
```

The class includes all necessary methods to access the Grafana user API endpoints. Be aware that all functionalities inside the class only working with basic authentication (username and password) and that the authenticated user is a Grafana Admin.

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="user.User.search_users"></a>

#### search\_users

```python
def search_users(results_per_page: int = 1000,
                 page: int = 1,
                 sort: str = None) -> list
```

The method includes a functionality to get all Grafana system users specified by the optional results_per_page, page and sort option

Required Permissions:
Action: users:read
Scope: global.users:*

**Arguments**:

- `results_per_page` _int_ - Specify the results_per_page as integer (default 1000)
- `page` _int_ - Specify the page as integer (default 1)
- `sort` _str_ - Specify the sort option. Valid values are login-asc, login-desc, email-asc, email-desc, name-asc, name-desc, lastSeenAtAge-asc and lastSeenAtAge-desc. By default, if sort is not specified, the user list will be ordered by login, email in ascending order (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of Grafana users

<a id="user.User.search_users_with_paging"></a>

#### search\_users\_with\_paging

```python
def search_users_with_paging(results_per_page: int = 1000,
                             page: int = 1,
                             query: str = None,
                             sort: str = None) -> dict
```

The method includes a functionality to get all Grafana system users specified by the optional results_per_page, page, query, sort and general paging functionality

Required Permissions:
Action: users:read
Scope: global.users:*

**Arguments**:

- `results_per_page` _int_ - Specify the results_per_page as integer (default 1000)
- `page` _int_ - Specify the page as integer (default 1)
- `query` _str_ - Specify the query (default None)
- `sort` _str_ - Specify the sort option. Valid values are login-asc, login-desc, email-asc, email-desc, name-asc, name-desc, lastSeenAtAge-asc and lastSeenAtAge-desc. By default, if sort is not specified, the user list will be ordered by login, email in ascending order (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the Grafana users

<a id="user.User.get_user_by_id"></a>

#### get\_user\_by\_id

```python
def get_user_by_id(id: int) -> dict
```

The method includes a functionality to get a specific user by the id

Required Permissions:
Action: users:read
Scope: users:*

**Arguments**:

- `id` _int_ - Specify the id of the user
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the user information

<a id="user.User.get_user_by_username_or_email"></a>

#### get\_user\_by\_username\_or\_email

```python
def get_user_by_username_or_email(username_or_email: str) -> dict
```

The method includes a functionality to get a specific user by the username_or_email

Required Permissions:
Action: users:read
Scope: global.users:*

**Arguments**:

- `username_or_email` _str_ - Specify the username_or_email of the user
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the user information

<a id="user.User.update_user"></a>

#### update\_user

```python
def update_user(id: int, user: UserObject)
```

The method includes a functionality to update the specified user

Required Permissions:
Action: users:write
Scope: users:*

**Arguments**:

- `id` _int_ - Specify the id of the user
- `user` _UserObject_ - Specify the used UserObject
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.User.get_user_organizations"></a>

#### get\_user\_organizations

```python
def get_user_organizations(id: int) -> list
```

The method includes a functionality to get the specified user organizations

Required Permissions:
Action: users:read
Scope: users:*

**Arguments**:

- `id` _int_ - Specify the id of the user
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of the user bound organizations

<a id="user.User.get_user_teams"></a>

#### get\_user\_teams

```python
def get_user_teams(id: int) -> list
```

The method includes a functionality to get the specified user teams

Required Permissions:
Action: users.teams:read
Scope: users:*

**Arguments**:

- `id` _int_ - Specify the id of the user
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of the user bound teams

<a id="user.User.switch_specific_user_context"></a>

#### switch\_specific\_user\_context

```python
def switch_specific_user_context(user_id: int, org_id: int)
```

The method includes a functionality to switch the user context to the given organization

**Arguments**:

- `user_id` _int_ - Specify the user_id
- `org_id` _int_ - Specify the org_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.CurrentUser"></a>

## CurrentUser Objects

```python
class CurrentUser()
```

The class includes all necessary methods to access the Grafana current user API endpoints. Be aware that all functionalities inside the class maybe only working with basic authentication (username and password)

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="user.CurrentUser.get_user"></a>

#### get\_user

```python
def get_user() -> dict
```

The method includes a functionality to get the current user

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the user information

<a id="user.CurrentUser.update_password"></a>

#### update\_password

```python
def update_password(old_password: str, new_password: str,
                    confirm_new_password: str)
```

The method includes a functionality to update the current user password

**Arguments**:

- `old_password` _str_ - Specify the old_password
- `new_password` _str_ - Specify the new_password
- `confirm_new_password` _str_ - Specify the confirm_new_password
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.CurrentUser.switch_current_user_context"></a>

#### switch\_current\_user\_context

```python
def switch_current_user_context(org_id: int)
```

The method includes a functionality to switch the current user context to the given organization

**Arguments**:

- `org_id` _int_ - Specify the organization id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.CurrentUser.get_user_organizations"></a>

#### get\_user\_organizations

```python
def get_user_organizations() -> list
```

The method includes a functionality to get the current user organizations

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of organizations

<a id="user.CurrentUser.get_user_teams"></a>

#### get\_user\_teams

```python
def get_user_teams() -> list
```

The method includes a functionality to get the current user teams

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of teams

<a id="user.CurrentUser.star_a_dashboard"></a>

#### star\_a\_dashboard

```python
def star_a_dashboard(dashboard_id: int)
```

The method includes a functionality to star a dashboard for the current user

**Arguments**:

- `dashboard_id` _int_ - Specify the dashboard id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.CurrentUser.unstar_a_dashboard"></a>

#### unstar\_a\_dashboard

```python
def unstar_a_dashboard(dashboard_id: int)
```

The method includes a functionality to unstar a dashboard for the current user

**Arguments**:

- `dashboard_id` _int_ - Specify the dashboard id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="user.CurrentUser.get_auth_tokens"></a>

#### get\_auth\_tokens

```python
def get_auth_tokens() -> list
```

The method includes a functionality to get the auth tokens for the current user

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of auth tokens of the current user

<a id="user.CurrentUser.revoke_auth_token"></a>

#### revoke\_auth\_token

```python
def revoke_auth_token(auth_token_id: int)
```

The method includes a functionality to revoke a specified auth token of the current user

**Arguments**:

- `auth_token_id` _int_ - Specify the auth_token_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

