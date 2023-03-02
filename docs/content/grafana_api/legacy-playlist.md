# Table of Contents

* [legacy\_playlist](#legacy_playlist)
  * [LegacyPlaylist](#legacy_playlist.LegacyPlaylist)
    * [get\_playlist](#legacy_playlist.LegacyPlaylist.get_playlist)
    * [get\_playlist\_items](#legacy_playlist.LegacyPlaylist.get_playlist_items)
    * [get\_playlist\_dashboards](#legacy_playlist.LegacyPlaylist.get_playlist_dashboards)
    * [update\_playlist](#legacy_playlist.LegacyPlaylist.update_playlist)
    * [delete\_playlist](#legacy_playlist.LegacyPlaylist.delete_playlist)

<a id="legacy_playlist"></a>

# legacy\_playlist

<a id="legacy_playlist.LegacyPlaylist"></a>

## LegacyPlaylist Objects

```python
class LegacyPlaylist()
```

The class includes all necessary methods to access the Grafana legacy playlist API endpoints.  Be aware that the functionality is a Grafana <= v9 feature

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="legacy_playlist.LegacyPlaylist.get_playlist"></a>

#### get\_playlist

```python
def get_playlist(playlist_id: int) -> dict
```

The method includes a functionality to get the playlist specified by the playlist_id

**Arguments**:

- `playlist_id` _int_ - Specify the playlist_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist

<a id="legacy_playlist.LegacyPlaylist.get_playlist_items"></a>

#### get\_playlist\_items

```python
def get_playlist_items(playlist_id: int) -> list
```

The method includes a functionality to get the playlist items specified by the playlist_id

**Arguments**:

- `playlist_id` _int_ - Specify the playlist_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist items

<a id="legacy_playlist.LegacyPlaylist.get_playlist_dashboards"></a>

#### get\_playlist\_dashboards

```python
def get_playlist_dashboards(playlist_id: int) -> list
```

The method includes a functionality to get the playlist dashboards specified by the playlist_id

**Arguments**:

- `playlist_id` _int_ - Specify the playlist_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist dashboards

<a id="legacy_playlist.LegacyPlaylist.update_playlist"></a>

#### update\_playlist

```python
def update_playlist(playlist_id: int, playlist: PlaylistObject) -> dict
```

The method includes a functionality to update a playlist specified by the playlist object and playlist_id

**Arguments**:

- `playlist_id` _int_ - Specify the playlist_id
- `playlist` _PlaylistObject_ - Specify the playlist object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the corresponding playlist

<a id="legacy_playlist.LegacyPlaylist.delete_playlist"></a>

#### delete\_playlist

```python
def delete_playlist(playlist_id: int)
```

The method includes a functionality to delete a playlist specified by the playlist_id

**Arguments**:

- `playlist_id` _int_ - Specify the playlist_id
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

