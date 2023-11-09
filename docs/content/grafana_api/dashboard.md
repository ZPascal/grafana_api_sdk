# Table of Contents

* [dashboard](#dashboard)
  * [Dashboard](#dashboard.Dashboard)
    * [create\_or\_update\_dashboard](#dashboard.Dashboard.create_or_update_dashboard)
    * [delete\_dashboard\_by\_name\_and\_path](#dashboard.Dashboard.delete_dashboard_by_name_and_path)
    * [get\_dashboard\_by\_uid](#dashboard.Dashboard.get_dashboard_by_uid)
    * [get\_dashboard\_home](#dashboard.Dashboard.get_dashboard_home)
    * [get\_dashboard\_tags](#dashboard.Dashboard.get_dashboard_tags)
    * [get\_dashboard\_uid\_and\_id\_by\_name\_and\_folder](#dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder)
    * [get\_dashboard\_permissions](#dashboard.Dashboard.get_dashboard_permissions)
    * [get\_dashboard\_permissions\_by\_uid](#dashboard.Dashboard.get_dashboard_permissions_by_uid)
    * [update\_dashboard\_permissions](#dashboard.Dashboard.update_dashboard_permissions)
    * [update\_dashboard\_permissions\_by\_uid](#dashboard.Dashboard.update_dashboard_permissions_by_uid)
    * [get\_dashboard\_versions](#dashboard.Dashboard.get_dashboard_versions)
    * [get\_dashboard\_versions\_by\_uid](#dashboard.Dashboard.get_dashboard_versions_by_uid)
    * [get\_dashboard\_version](#dashboard.Dashboard.get_dashboard_version)
    * [get\_dashboard\_version\_by\_uid](#dashboard.Dashboard.get_dashboard_version_by_uid)
    * [restore\_dashboard\_version](#dashboard.Dashboard.restore_dashboard_version)
    * [restore\_dashboard\_version\_by\_uid](#dashboard.Dashboard.restore_dashboard_version_by_uid)
    * [calculate\_dashboard\_diff](#dashboard.Dashboard.calculate_dashboard_diff)
    * [get\_public\_dashboards](#dashboard.Dashboard.get_public_dashboards)
    * [get\_public\_dashboard\_by\_uid](#dashboard.Dashboard.get_public_dashboard_by_uid)
    * [create\_public\_dashboard](#dashboard.Dashboard.create_public_dashboard)
    * [update\_public\_dashboard](#dashboard.Dashboard.update_public_dashboard)
    * [delete\_public\_dashboard](#dashboard.Dashboard.delete_public_dashboard)

<a id="dashboard"></a>

# dashboard

<a id="dashboard.Dashboard"></a>

## Dashboard Objects

```python
class Dashboard()
```

The class includes all necessary methods to access the Grafana dashboard API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="dashboard.Dashboard.create_or_update_dashboard"></a>

#### create\_or\_update\_dashboard

```python
def create_or_update_dashboard(dashboard_path: str,
                               dashboard_json: dict,
                               message: str,
                               overwrite: bool = False)
```

The method includes a functionality to create the specified dashboard

**Arguments**:

- `dashboard_path` _str_ - Specify the dashboard path in which the dashboard is to be placed
- `dashboard_json` _dict_ - Specify the inserted dashboard as dict
- `message` _str_ - Specify the message that should be injected as commit message inside the dashboard
- `overwrite` _bool_ - Should the already existing dashboard be overwritten (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.delete_dashboard_by_name_and_path"></a>

#### delete\_dashboard\_by\_name\_and\_path

```python
def delete_dashboard_by_name_and_path(dashboard_name: str,
                                      dashboard_path: str)
```

The method includes a functionality to delete the specified dashboard inside the model

**Arguments**:

- `dashboard_name` _str_ - Specify the dashboard name of the deleted dashboard
- `dashboard_path` _str_ - Specify the dashboard path in which the dashboard is to be placed
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.get_dashboard_by_uid"></a>

#### get\_dashboard\_by\_uid

```python
def get_dashboard_by_uid(uid: str) -> dict
```

The method includes a functionality to get the dashboard from the specified uid

**Arguments**:

- `uid` _str_ - Specify the uid of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dashboard

<a id="dashboard.Dashboard.get_dashboard_home"></a>

#### get\_dashboard\_home

```python
def get_dashboard_home() -> dict
```

The method includes a functionality to get the home dashboard

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the home dashboard

<a id="dashboard.Dashboard.get_dashboard_tags"></a>

#### get\_dashboard\_tags

```python
def get_dashboard_tags() -> list
```

The method includes a functionality to get the all tags of all dashboards

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all dashboard tags

<a id="dashboard.Dashboard.get_dashboard_uid_and_id_by_name_and_folder"></a>

#### get\_dashboard\_uid\_and\_id\_by\_name\_and\_folder

```python
def get_dashboard_uid_and_id_by_name_and_folder(dashboard_name: str,
                                                dashboard_path: str) -> dict
```

The method includes a functionality to extract the dashboard uid specified inside the model

**Arguments**:

- `dashboard_name` _str_ - Specify the dashboard name of the dashboard
- `dashboard_path` _str_ - Specify the dashboard path of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the dashboard uid and the id

<a id="dashboard.Dashboard.get_dashboard_permissions"></a>

#### get\_dashboard\_permissions

```python
def get_dashboard_permissions(id: int) -> list
```

The method includes a functionality to extract the dashboard permissions based on the specified id

**Arguments**:

- `id` _int_ - Specify the id of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the dashboard permissions of a dashboard as list

<a id="dashboard.Dashboard.get_dashboard_permissions_by_uid"></a>

#### get\_dashboard\_permissions\_by\_uid

```python
def get_dashboard_permissions_by_uid(uid: str) -> list
```

The method includes a functionality to extract the dashboard permissions based on the specified uid

**Arguments**:

- `uid` _str_ - Specify the uid of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the dashboard permissions of a dashboard as list

<a id="dashboard.Dashboard.update_dashboard_permissions"></a>

#### update\_dashboard\_permissions

```python
def update_dashboard_permissions(id: int, permission_json: dict)
```

The method includes a functionality to update the dashboard permissions based on the specified id and the permission json document

**Arguments**:

- `id` _int_ - Specify the id of the dashboard
- `permission_json` _dict_ - Specify the inserted permissions as dict
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.update_dashboard_permissions_by_uid"></a>

#### update\_dashboard\_permissions\_by\_uid

```python
def update_dashboard_permissions_by_uid(uid: str, permission_json: dict)
```

The method includes a functionality to update the dashboard permissions based on the specified uid and the permission json document

**Arguments**:

- `uid` _str_ - Specify the uid of the dashboard
- `permission_json` _dict_ - Specify the inserted permissions as dict
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.get_dashboard_versions"></a>

#### get\_dashboard\_versions

```python
def get_dashboard_versions(id: int) -> list
```

The method includes a functionality to extract the versions of a dashboard based on the specified id

**Arguments**:

- `id` _int_ - Specify the id of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all dashboard versions of a dashboard as list

<a id="dashboard.Dashboard.get_dashboard_versions_by_uid"></a>

#### get\_dashboard\_versions\_by\_uid

```python
def get_dashboard_versions_by_uid(uid: str) -> list
```

The method includes a functionality to extract the versions of a dashboard based on the specified uid

**Arguments**:

- `uid` _str_ - Specify the id of the dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all dashboard versions of a dashboard as list

<a id="dashboard.Dashboard.get_dashboard_version"></a>

#### get\_dashboard\_version

```python
def get_dashboard_version(id: int, version_id: int) -> dict
```

The method includes a functionality to extract a specified version of a dashboard based on the specified dashboard id and a version_id of the dashboard

**Arguments**:

- `id` _int_ - Specify the id of the dashboard
- `version_id` _int_ - Specify the version_id of a dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a dashboard version of a dashboard as dict

<a id="dashboard.Dashboard.get_dashboard_version_by_uid"></a>

#### get\_dashboard\_version\_by\_uid

```python
def get_dashboard_version_by_uid(uid: str, version_id: int) -> dict
```

The method includes a functionality to extract a specified version of a dashboard based on the specified dashboard uid and a version_id of the dashboard

**Arguments**:

- `uid` _str_ - Specify the uid of the dashboard
- `version_id` _int_ - Specify the version_id of a dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a dashboard version of a dashboard as dict

<a id="dashboard.Dashboard.restore_dashboard_version"></a>

#### restore\_dashboard\_version

```python
def restore_dashboard_version(id: int, version: dict)
```

The method includes a functionality to restore a specified version of a dashboard based on the specified dashboard id and a version as dict of the dashboard

**Arguments**:

- `id` _int_ - Specify the id of the dashboard
- `version` _dict_ - Specify the version_id of a dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.restore_dashboard_version_by_uid"></a>

#### restore\_dashboard\_version\_by\_uid

```python
def restore_dashboard_version_by_uid(uid: str, version: dict)
```

The method includes a functionality to restore a specified version of a dashboard based on the specified dashboard uid and a version as dict of the dashboard

**Arguments**:

- `uid` _str_ - Specify the uid of the dashboard
- `version` _dict_ - Specify the version_id of a dashboard
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="dashboard.Dashboard.calculate_dashboard_diff"></a>

#### calculate\_dashboard\_diff

```python
def calculate_dashboard_diff(dashboard_id_and_version_base: dict,
                             dashboard_id_and_version_new: dict,
                             diff_type: str = "json") -> str
```

The method includes a functionality to calculate the diff of specified versions of a dashboard based on the specified dashboard uid and the selected version of the base dashboard and the new dashboard and the diff type (basic or json)

**Arguments**:

- `dashboard_id_and_version_base` _dict_ - Specify the version and id of the base dashboard
- `dashboard_id_and_version_new` _dict_ - Specify the version and id of the new dashboard
- `diff_type` _str_ - Specify the diff type (basic or json) (default json)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _str_ - Returns the difference of the two specified dashboards

<a id="dashboard.Dashboard.get_public_dashboards"></a>

#### get\_public\_dashboards

```python
def get_public_dashboards(per_page: int = None, page: int = None) -> dict
```

The method includes a functionality to get all public available dashboards

Required Permissions:
Action: dashboards:read
Scope: dashboards:uid:<dashboard UID>

**Arguments**:

- `per_page` _int_ - Specify the value per page size
- `page` _int_ - Specify the page
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns all public available dashboards

<a id="dashboard.Dashboard.get_public_dashboard_by_uid"></a>

#### get\_public\_dashboard\_by\_uid

```python
def get_public_dashboard_by_uid(dashboard_uid: str) -> dict
```

The method includes a functionality to get a public available dashboard specified by dashboard_uid

Required Permissions:
Action: dashboards:read
Scope: dashboards:uid:<dashboard UID>

**Arguments**:

- `dashboard_uid` _str_ - Specify the dashboard_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding public available dashboard

<a id="dashboard.Dashboard.create_public_dashboard"></a>

#### create\_public\_dashboard

```python
def create_public_dashboard(
    dashboard_uid: str, public_dashboard: PublicDashboard = PublicDashboard()
) -> dict
```

The method includes a functionality to create a public available dashboard

Required Permissions:
Action: dashboards.public:write
Scope: dashboards:uid:<dashboard UID>

**Arguments**:

- `dashboard_uid` _str_ - Specify the dashboard_uid
- `public_dashboard` _PublicDashboard_ - Specify the optional public dashboard object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding public available dashboard

<a id="dashboard.Dashboard.update_public_dashboard"></a>

#### update\_public\_dashboard

```python
def update_public_dashboard(dashboard_uid: str,
                            public_dashboard_uid: str,
                            time_selection_enabled: bool = None,
                            is_enabled: bool = None,
                            annotations_enabled: bool = None,
                            share: str = None) -> dict
```

The method includes a functionality to update a public available dashboard

Required Permissions:
Action: dashboards.public:write
Scope: dashboards:uid:<dashboard UID>

**Arguments**:

- `dashboard_uid` _str_ - Specify the dashboard_uid
- `public_dashboard_uid` _str_ - Specify the public_dashboard_uid
- `time_selection_enabled` _bool_ - Specify the optional enablement of the time picker inside the public dashboard (default None)
- `is_enabled` _bool_ - Specify the optional enablement of the public dashboard (default None)
- `annotations_enabled` _bool_ - Specify the optional enablement of the annotations inside the public dashboard (default None)
- `share` _str_ - Specify the optional share mode of the public dashboard (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding public available dashboard

<a id="dashboard.Dashboard.delete_public_dashboard"></a>

#### delete\_public\_dashboard

```python
def delete_public_dashboard(dashboard_uid: str, public_dashboard_uid: str)
```

The method includes a functionality to delete a public available dashboard

Required Permissions:
Action: dashboards.public:write
Scope: dashboards:uid:<dashboard UID>

**Arguments**:

- `dashboard_uid` _str_ - Specify the dashboard_uid
- `public_dashboard_uid` _str_ - Specify the public_dashboard_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

