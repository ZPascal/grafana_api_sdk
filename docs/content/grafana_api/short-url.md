# Table of Contents

* [short\_url](#short_url)
  * [ShortUrl](#short_url.ShortUrl)
    * [create\_short\_url](#short_url.ShortUrl.create_short_url)

<a id="short_url"></a>

# short\_url

<a id="short_url.ShortUrl"></a>

## ShortUrl Objects

```python
class ShortUrl()
```

The class includes all necessary methods to access the Grafana short url API endpoint

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="short_url.ShortUrl.create_short_url"></a>

#### create\_short\_url

```python
def create_short_url(path: str)
```

The method includes a functionality to create a short link for a specific dashboard

**Arguments**:

- `path` _str_ - Specify the corresponding dashboard path
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the uid and the url of the newly generated link

