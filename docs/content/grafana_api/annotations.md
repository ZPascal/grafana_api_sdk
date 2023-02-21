# Table of Contents

* [annotations](#annotations)
  * [Annotations](#annotations.Annotations)
    * [find\_annotations](#annotations.Annotations.find_annotations)
    * [create\_annotation](#annotations.Annotations.create_annotation)
    * [create\_graphite\_annotation](#annotations.Annotations.create_graphite_annotation)
    * [update\_annotation](#annotations.Annotations.update_annotation)
    * [delete\_annotation](#annotations.Annotations.delete_annotation)
    * [find\_annotation\_tags](#annotations.Annotations.find_annotation_tags)

<a id="annotations"></a>

# annotations

<a id="annotations.Annotations"></a>

## Annotations Objects

```python
class Annotations()
```

The class includes all necessary methods to access the Grafana annotations API endpoints. Annotations can be organization annotations that can be shown on any dashboard by configuring an annotation data source filtered by tags. They can also be tied to a panel on a dashboard and are then only shown on that panel

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="annotations.Annotations.find_annotations"></a>

#### find\_annotations

```python
def find_annotations(annotation: FindAnnotationObject = None) -> list
```

The method includes a functionality to find the corresponding annotations

**Arguments**:

- `annotation` _FindAnnotationObject_ - Specify the find annotation object
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns the result of the find annotations call

<a id="annotations.Annotations.create_annotation"></a>

#### create\_annotation

```python
def create_annotation(annotation: AnnotationObject) -> int
```

The method includes a functionality to create the corresponding annotation

Args:
    annotation (AnnotationObject): Specify the annotation object

Required Permissions:
    Action: annotations:create
    Scope: annotations:type:

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    api_call (int): Returns the annotation id


<a id="annotations.Annotations.create_graphite_annotation"></a>

#### create\_graphite\_annotation

```python
def create_graphite_annotation(annotation: AnnotationGraphiteObject) -> int
```

The method includes a functionality to create the corresponding graphite annotation

Args:
    annotation (AnnotationGraphiteObject): Specify the annotation object

Required Permissions:
    Action: annotations:create
    Scope: annotations:type:organization

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    api_call (int): Returns the annotation id


<a id="annotations.Annotations.update_annotation"></a>

#### update\_annotation

```python
def update_annotation(id: int, annotation: AnnotationObject)
```

The method includes a functionality to update the corresponding annotation specified by the annotation id

Args:
    id (int): Specify the annotation object id
    annotation (AnnotationObject): Specify the annotation object

Required Permissions:
    Action: annotations:write
    Scope: annotations:type:

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="annotations.Annotations.delete_annotation"></a>

#### delete\_annotation

```python
def delete_annotation(id: int)
```

The method includes a functionality to delete the corresponding annotation specified by the annotation id

Args:
    id (int): Specify the annotation object id

Required Permissions:
    Action: annotations:write
    Scope: annotations:type:

Raises:
    ValueError: Missed specifying a necessary value
    Exception: Unspecified error by executing the API call

Returns:
    None


<a id="annotations.Annotations.find_annotation_tags"></a>

#### find\_annotation\_tags

```python
def find_annotation_tags(tag: str = None, limit: int = 100)
```

The method includes a functionality to find the annotation tags

**Arguments**:

- `tag` _str_ - Specify the optional annotation tag
- `limit` _int_ - Specify the optional annotation limit (default 100)
  
  Required Permissions:
- `Action` - annotations:read
- `Scope` - N/A
  

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the result of the find annotation tags call

