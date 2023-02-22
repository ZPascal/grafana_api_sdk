# Table of Contents

* [folder](#folder)
  * [Folder](#folder.Folder)
    * [get\_folders](#folder.Folder.get_folders)
    * [get\_folder\_by\_uid](#folder.Folder.get_folder_by_uid)
    * [get\_folder\_by\_id](#folder.Folder.get_folder_by_id)
    * [create\_folder](#folder.Folder.create_folder)
    * [update\_folder](#folder.Folder.update_folder)
    * [delete\_folder](#folder.Folder.delete_folder)
    * [get\_folder\_permissions](#folder.Folder.get_folder_permissions)
    * [update\_folder\_permissions](#folder.Folder.update_folder_permissions)
    * [get\_folder\_id\_by\_dashboard\_path](#folder.Folder.get_folder_id_by_dashboard_path)
    * [get\_all\_folder\_ids\_and\_names](#folder.Folder.get_all_folder_ids_and_names)

<a id="folder"></a>

# folder

<a id="folder.Folder"></a>

## Folder Objects

```python
class Folder()
```

The class includes all necessary methods to access the Grafana folder API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="folder.Folder.get_folders"></a>

#### get\_folders

```python
def get_folders() -> list
```

The method includes a functionality to extract all folders inside the organization

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all folders

<a id="folder.Folder.get_folder_by_uid"></a>

#### get\_folder\_by\_uid

```python
def get_folder_by_uid(uid: str) -> dict
```

The method includes a functionality to extract all folder information specified by the uid of the folder

**Arguments**:

- `uid` _str_ - Specify the uid of the folder
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a folder

<a id="folder.Folder.get_folder_by_id"></a>

#### get\_folder\_by\_id

```python
def get_folder_by_id(id: int) -> dict
```

The method includes a functionality to extract all folder information specified by the id of the folder

**Arguments**:

- `id` _int_ - Specify the id of the folder
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a folder

<a id="folder.Folder.create_folder"></a>

#### create\_folder

```python
def create_folder(title: str, uid: str = None) -> dict
```

The method includes a functionality to create a new folder inside the organization specified by the defined title and the optional uid

**Arguments**:

- `title` _str_ - Specify the title of the folder
- `uid` _str_ - Specify the uid of the folder (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a newly created folder

<a id="folder.Folder.update_folder"></a>

#### update\_folder

```python
def update_folder(title: str,
                  uid: str,
                  version: int = 0,
                  overwrite: bool = False) -> dict
```

The method includes a functionality to update a folder information inside the organization specified by the uid, the title, the version of the folder or if folder information be overwritten

**Arguments**:

- `title` _str_ - Specify the title of the folder
- `uid` _str_ - Specify the uid of the folder
- `version` _int_ - Specify the version of the folder (default 0)
- `overwrite` _bool_ - Should the already existing folder information be overwritten (default False)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns an updated folder

<a id="folder.Folder.delete_folder"></a>

#### delete\_folder

```python
def delete_folder(uid: str)
```

The method includes a functionality to delete a folder inside the organization specified by the defined uid

**Arguments**:

- `uid` _str_ - Specify the uid of the folder
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="folder.Folder.get_folder_permissions"></a>

#### get\_folder\_permissions

```python
def get_folder_permissions(uid: str) -> list
```

The method includes a functionality to extract the folder permissions inside the organization specified by the defined uid

**Arguments**:

- `uid` _str_ - Specify the uid of the folder
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns a list of folder permissions

<a id="folder.Folder.update_folder_permissions"></a>

#### update\_folder\_permissions

```python
def update_folder_permissions(uid: str, permission_json: dict)
```

The method includes a functionality to update the folder permissions based on the specified uid and the permission json document

**Arguments**:

- `uid` _str_ - Specify the uid of the folder
- `permission_json` _dict_ - Specify the inserted permissions as dict
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="folder.Folder.get_folder_id_by_dashboard_path"></a>

#### get\_folder\_id\_by\_dashboard\_path

```python
def get_folder_id_by_dashboard_path(dashboard_path: str) -> int
```

The method includes a functionality to extract the folder id specified inside model dashboard path

**Arguments**:

- `dashboard_path` _str_ - Specify the dashboard path
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `folder_id` _int_ - Returns the folder id

<a id="folder.Folder.get_all_folder_ids_and_names"></a>

#### get\_all\_folder\_ids\_and\_names

```python
def get_all_folder_ids_and_names() -> list
```

The method extract all folder id and names inside the complete organisation

**Returns**:

- `folders` _list_ - Returns a list of dicts with folder ids and the corresponding names

