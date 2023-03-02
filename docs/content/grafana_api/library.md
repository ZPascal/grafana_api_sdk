# Table of Contents

* [library](#library)
  * [Library](#library.Library)
    * [get\_all\_library\_elements](#library.Library.get_all_library_elements)
    * [get\_library\_element\_by\_uid](#library.Library.get_library_element_by_uid)
    * [get\_library\_element\_by\_name](#library.Library.get_library_element_by_name)
    * [get\_library\_element\_connections](#library.Library.get_library_element_connections)
    * [create\_library\_element](#library.Library.create_library_element)
    * [update\_library\_element](#library.Library.update_library_element)
    * [delete\_library\_element](#library.Library.delete_library_element)

<a id="library"></a>

# library

<a id="library.Library"></a>

## Library Objects

```python
class Library()
```

The class includes all necessary methods to access the Grafana library API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="library.Library.get_all_library_elements"></a>

#### get\_all\_library\_elements

```python
def get_all_library_elements(
        results_per_page: int = 100,
        pages: int = 1,
        search_string: str = None,
        kind: int = 1,
        sort_direction: SortDirection = SortDirection.DESC,
        types_filter: str = None,
        exclude_uid: str = None,
        folder_filter_ids: str = None) -> dict
```

The method includes a functionality to get a list of all library elements the authenticated user has permission to view. Use the perPage query parameter to control the maximum number of library elements returned, The default limit is 100. You can also use the page query parameter to fetch library elements from any page other than the first one

**Arguments**:

- `results_per_page` _int_ - Specify the results_per_page as integer (default 100)
- `pages` _int_ - Specify the pages as integer (default 1)
- `search_string` _str_ - Specify the search string (default None)
- `kind` _int_ - Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
- `sort_direction` _SortDirection_ - Specify the sort order of elements. Use alpha-asc for ascending and alpha-desc for descending sort order (default alpha-desc)
- `types_filter` _str_ - Specify a comma separated list of types to filter the elements by (default None)
- `exclude_uid` _str_ - Specify the element uid to exclude from search results (default None)
- `folder_filter_ids` _str_ - Specify a comma separated list of folder ID(s) to filter the elements by (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the library elements

<a id="library.Library.get_library_element_by_uid"></a>

#### get\_library\_element\_by\_uid

```python
def get_library_element_by_uid(uid: str) -> dict
```

The method includes a functionality to get a library element with the given uid

**Arguments**:

- `uid` _str_ - Specify the uid of the library element
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding library element

<a id="library.Library.get_library_element_by_name"></a>

#### get\_library\_element\_by\_name

```python
def get_library_element_by_name(name: str) -> dict
```

The method includes a functionality to get a library element with the given name

**Arguments**:

- `name` _str_ - Specify the name of the library element
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding library element

<a id="library.Library.get_library_element_connections"></a>

#### get\_library\_element\_connections

```python
def get_library_element_connections(uid: str) -> dict
```

The method includes a functionality to get a list of connections for a library element based on the specified uid

**Arguments**:

- `uid` _str_ - Specify the uid of the library element
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding list of connections

<a id="library.Library.create_library_element"></a>

#### create\_library\_element

```python
def create_library_element(folder_id: int,
                           model: dict,
                           kind: int = 1,
                           folder_uid: str = None,
                           name: str = None,
                           uid: str = None) -> dict
```

The method includes a functionality to create a library element based on the specified folder id and model

**Arguments**:

- `folder_id` _int_ - Specify the folder where the library element is stored. It is deprecated since Grafana v9
- `model` _dict_ - Specify the JSON model for the library element
- `kind` _int_ - Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
- `folder_uid` _str_ - Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder (default None)
- `name` _str_ - Specify the name of the library element (default None)
- `uid` _str_ - Specify the uid of the library element (default None)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the newly created library element

<a id="library.Library.update_library_element"></a>

#### update\_library\_element

```python
def update_library_element(uid: str,
                           folder_id: int,
                           folder_uid: str,
                           name: str,
                           model: dict,
                           version: int,
                           kind: int = 1) -> dict
```

The method includes a functionality to update a library element

**Arguments**:

- `uid` _str_ - Specify the uid of the library element
- `folder_id` _int_ - Specify the folder where the library element is stored. It is deprecated since Grafana v9
- `folder_uid` _str_ - Specify the uid of the folder where the library element is stored. Specify an empty string when it is general folder
- `name` _str_ - Specify the name of the library element
- `model` _dict_ - Specify the JSON model for the library element
- `version` _int_ - Specify the version for the library element
- `kind` _int_ - Specify the kind of element to search for. Use 1 for library panels or 2 for library variables (default 1)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the updated library element

<a id="library.Library.delete_library_element"></a>

#### delete\_library\_element

```python
def delete_library_element(uid: str)
```

The method includes a functionality to delete a library element specified by the uid

**Arguments**:

- `uid` _str_ - Specify the uid of the library element
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

