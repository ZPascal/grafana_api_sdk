# Table of Contents

* [correlations](#correlations)
  * [Correlations](#correlations.Correlations)
    * [create\_correlations](#correlations.Correlations.create_correlations)
    * [delete\_correlations](#correlations.Correlations.delete_correlations)
    * [update\_correlations](#correlations.Correlations.update_correlations)

<a id="correlations"></a>

# correlations

<a id="correlations.Correlations"></a>

## Correlations Objects

```python
class Correlations()
```

The class includes all necessary methods to access the Grafana correlations API endpoints

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="correlations.Correlations.create_correlations"></a>

#### create\_correlations

```python
def create_correlations(correlation_object: CorrelationObject) -> dict
```

The method includes a functionality to create a correlation between two data sources - the source data source identified by source uid in the path, and the target data source which is specified in the body

**Arguments**:

- `correlation_object` _CorrelationObject_ - Specify the correlation object
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the newly created correlation

<a id="correlations.Correlations.delete_correlations"></a>

#### delete\_correlations

```python
def delete_correlations(source_datasource_uid: str, correlation_uid: str)
```

The method includes a functionality to deletes a correlation

**Arguments**:

- `source_datasource_uid` _str_ - Specify the source data source uid
- `correlation_uid` _str_ - Specify the correlation uid
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="correlations.Correlations.update_correlations"></a>

#### update\_correlations

```python
def update_correlations(source_datasource_uid: str, correlation_uid: str,
                        label: str, description: str) -> dict
```

The method includes a functionality to update a correlation

**Arguments**:

- `source_datasource_uid` _str_ - Specify the source data source uid
- `correlation_uid` _str_ - Specify the correlation uid
- `label` _str_ - Specify a label for the correlation
- `description` _str_ - Specify a description for the correlation
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the updated correlation

