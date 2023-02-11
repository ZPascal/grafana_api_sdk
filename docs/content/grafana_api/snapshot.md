# Table of Contents

* [snapshot](#snapshot)
  * [Snapshot](#snapshot.Snapshot)
    * [create\_new\_snapshot](#snapshot.Snapshot.create_new_snapshot)
    * [get\_snapshots](#snapshot.Snapshot.get_snapshots)
    * [get\_snapshot\_by\_key](#snapshot.Snapshot.get_snapshot_by_key)
    * [delete\_snapshot\_by\_key](#snapshot.Snapshot.delete_snapshot_by_key)
    * [delete\_snapshot\_by\_delete\_key](#snapshot.Snapshot.delete_snapshot_by_delete_key)

<a id="snapshot"></a>

# snapshot

<a id="snapshot.Snapshot"></a>

## Snapshot Objects

```python
class Snapshot()
```

The class includes all necessary methods to access the Grafana snapshot API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="snapshot.Snapshot.create_new_snapshot"></a>

#### create\_new\_snapshot

```python
def create_new_snapshot(dashboard_json: dict,
                        name: str = None,
                        expires: int = None,
                        external: bool = False,
                        key: str = None,
                        delete_key: str = None) -> dict
```

The method includes a functionality to create the specified dashboard snapshot

**Arguments**:

- `dashboard_json` _dict_ - Specify the dashboard_json of the dashboard
- `name` _str_ - Specify the optional name of the dashboard snapshot
- `expires` _int_ - Specify the optional expiry time as seconds of the dashboard snapshot. 3600 is 1 hour, 86400 is 1 day (default never expired)
- `external` _bool_ - Specify the optional external server rather than locally (default False)
- `key` _str_ - Specify the optional unique key. Required if external is true.
- `delete_key` _str_ - Specify the optional unique key used to delete the snapshot. It is different from the key so that only the creator can delete the snapshot. Required if external is true.
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the snapshot information of the dashboard

<a id="snapshot.Snapshot.get_snapshots"></a>

#### get\_snapshots

```python
def get_snapshots() -> list
```

The method includes a functionality to list all dashboard snapshots

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all dashboard snapshots

<a id="snapshot.Snapshot.get_snapshot_by_key"></a>

#### get\_snapshot\_by\_key

```python
def get_snapshot_by_key(key: str) -> dict
```

The method includes a functionality to get a specific dashboard snapshot by the key

**Arguments**:

- `key` _str_ - Specify the key of the dashboard snapshot
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns a specific dashboard snapshot

<a id="snapshot.Snapshot.delete_snapshot_by_key"></a>

#### delete\_snapshot\_by\_key

```python
def delete_snapshot_by_key(key: str)
```

The method includes a functionality to delete a specific dashboard snapshot by the key

**Arguments**:

- `key` _str_ - Specify the key of the dashboard snapshot
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="snapshot.Snapshot.delete_snapshot_by_delete_key"></a>

#### delete\_snapshot\_by\_delete\_key

```python
def delete_snapshot_by_delete_key(delete_key: str)
```

The method includes a functionality to delete a specific dashboard snapshot by the delete_key

**Arguments**:

- `delete_key` _str_ - Specify the delete_key of the dashboard snapshot
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

