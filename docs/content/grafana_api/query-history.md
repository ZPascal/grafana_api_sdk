# Table of Contents

* [query\_history](#query_history)
  * [QueryHistory](#query_history.QueryHistory)
    * [add\_query\_to\_history](#query_history.QueryHistory.add_query_to_history)
    * [search\_query\_history](#query_history.QueryHistory.search_query_history)
    * [delete\_query\_history](#query_history.QueryHistory.delete_query_history)
    * [update\_query\_history](#query_history.QueryHistory.update_query_history)
    * [star\_query\_history](#query_history.QueryHistory.star_query_history)
    * [unstar\_query\_history](#query_history.QueryHistory.unstar_query_history)

<a id="query_history"></a>

# query\_history

<a id="query_history.QueryHistory"></a>

## QueryHistory Objects

```python
class QueryHistory()
```

The class includes all necessary methods to access the Grafana query history API endpoints. Be aware that it requires that the user is logged in and that query history feature is enabled in the config file

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="query_history.QueryHistory.add_query_to_history"></a>

#### add\_query\_to\_history

```python
def add_query_to_history(datasource_uid: str, queries: list) -> dict
```

The method includes a functionality to add queries to query history

**Arguments**:

- `datasource_uid` _str_ - Specify the datasource uid
- `queries` _list_ - Specify the queries as list from type QueryObject
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the added result of the query history

<a id="query_history.QueryHistory.search_query_history"></a>

#### search\_query\_history

```python
def search_query_history(datasource_uids: list,
                         search_string: str,
                         sort: str = "time-desc",
                         only_starred: bool = False,
                         pages: int = 1,
                         results_per_page: int = 100) -> dict
```

The method includes a functionality to search a query inside the query history

**Arguments**:

- `datasource_uids` _list_ - Specify the datasource uid
- `search_string` _str_ - Specify the search string to filter the result
- `sort` _str_ - Specify the sorting order e.g. time-asc or time-desc (default time-desc)
- `only_starred` _bool_ - Specify if queries that are starred should be used for the search (default false)
- `pages` _int_ - Specify the pages as integer (default 1)
- `results_per_page` _int_ - Specify the results_per_page as integer (default 100)
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding result of the query history

<a id="query_history.QueryHistory.delete_query_history"></a>

#### delete\_query\_history

```python
def delete_query_history(uid: str)
```

The method includes a functionality to delete a query inside the query history

**Arguments**:

- `uid` _str_ - Specify the uid of the query
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="query_history.QueryHistory.update_query_history"></a>

#### update\_query\_history

```python
def update_query_history(uid: str, comment: str) -> dict
```

The method includes a functionality to update a query inside the query history

**Arguments**:

- `uid` _str_ - Specify the uid of the query
- `comment` _str_ - Specify the comment of the query
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the modified result of the query history

<a id="query_history.QueryHistory.star_query_history"></a>

#### star\_query\_history

```python
def star_query_history(uid: str) -> dict
```

The method includes a functionality to star a query inside the query history

**Arguments**:

- `uid` _str_ - Specify the uid of the query
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding stared query history

<a id="query_history.QueryHistory.unstar_query_history"></a>

#### unstar\_query\_history

```python
def unstar_query_history(uid: str) -> dict
```

The method includes a functionality to unstar a query inside the query history

**Arguments**:

- `uid` _str_ - Specify the uid of the query
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding unstared query history

