# Table of Contents

* [search](#search)
  * [Search](#search.Search)
    * [search](#search.Search.search)

<a id="search"></a>

# search

<a id="search.Search"></a>

## Search Objects

```python
class Search()
```

The class includes all necessary methods to access the Grafana search API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="search.Search.search"></a>

#### search

```python
def search(search_query: str) -> list
```

The method includes a functionality to execute a custom query

**Arguments**:

- `search_query` _str_ - Specify the inserted query as string
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the list of query the results

