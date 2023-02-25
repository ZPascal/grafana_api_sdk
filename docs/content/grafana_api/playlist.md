# Table of Contents

* [playlist](#playlist)
  * [Playlist](#playlist.Playlist)
    * [search\_playlist](#playlist.Playlist.search_playlist)
    * [get\_playlist](#playlist.Playlist.get_playlist)
    * [get\_playlist\_items](#playlist.Playlist.get_playlist_items)
    * [get\_playlist\_dashboards](#playlist.Playlist.get_playlist_dashboards)
    * [create\_playlist](#playlist.Playlist.create_playlist)
    * [update\_playlist](#playlist.Playlist.update_playlist)
    * [delete\_playlist](#playlist.Playlist.delete_playlist)

<a id="playlist"></a>

# playlist

<a id="playlist.Playlist"></a>

## Playlist Objects

```python
class Playlist()
```

The class includes all necessary methods to access the Grafana playlist API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="playlist.Playlist.search_playlist"></a>

#### search\_playlist

```python
def search_playlist(query: str = None, limit: int = None) -> list
```

The method includes a functionality to get the organization playlist's specified by the optional pagination functionality

**Arguments**:

- `query` _str_ - Specify the query to limit response to playlist having a name like this value(default None)
- `limit` _int_ - Specify the limit as integer of the response (default None)
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the organization playlist's

<a id="playlist.Playlist.get_playlist"></a>

#### get\_playlist

```python
def get_playlist(playlist_uid: str) -> dict
```

The method includes a functionality to get the playlist specified by the playlist_uid

**Arguments**:

- `playlist_uid` _str_ - Specify the playlist_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist

<a id="playlist.Playlist.get_playlist_items"></a>

#### get\_playlist\_items

```python
def get_playlist_items(playlist_uid: str) -> list
```

The method includes a functionality to get the playlist items specified by the playlist_uid

**Arguments**:

- `playlist_uid` _str_ - Specify the playlist_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist items

<a id="playlist.Playlist.get_playlist_dashboards"></a>

#### get\_playlist\_dashboards

```python
def get_playlist_dashboards(playlist_uid: str) -> list
```

The method includes a functionality to get the playlist dashboards specified by the playlist_uid

**Arguments**:

- `playlist_uid` _str_ - Specify the playlist_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist dashboards

<a id="playlist.Playlist.create_playlist"></a>

#### create\_playlist

```python
def create_playlist(playlist: PlaylistObject) -> dict
```

The method includes a functionality to create a playlist specified by the playlist object

**Arguments**:

- `playlist` _PlaylistObject_ - Specify the playlist object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist

<a id="playlist.Playlist.update_playlist"></a>

#### update\_playlist

```python
def update_playlist(playlist_uid: str, playlist: PlaylistObject) -> dict
```

The method includes a functionality to update a playlist specified by the playlist object and playlist_uid

**Arguments**:

- `playlist_uid` _str_ - Specify the playlist_uid
- `playlist` _PlaylistObject_ - Specify the playlist object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist

<a id="playlist.Playlist.delete_playlist"></a>

#### delete\_playlist

```python
def delete_playlist(playlist_uid: str)
```

The method includes a functionality to delete a playlist specified by the playlist_uid

**Arguments**:

- `playlist_uid` _str_ - Specify the playlist_uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

