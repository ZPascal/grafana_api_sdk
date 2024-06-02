# Table of Contents

* [reporting](#reporting)
  * [Reporting](#reporting.Reporting)
    * [get\_reports](#reporting.Reporting.get_reports)
    * [get\_report\_by\_id](#reporting.Reporting.get_report_by_id)
    * [create\_report](#reporting.Reporting.create_report)
    * [update\_report](#reporting.Reporting.update_report)
    * [delete\_report](#reporting.Reporting.delete_report)
    * [send\_report](#reporting.Reporting.send_report)
    * [get\_report\_branding\_settings](#reporting.Reporting.get_report_branding_settings)
    * [save\_report\_branding\_settings](#reporting.Reporting.save_report_branding_settings)
    * [send\_report\_test\_email](#reporting.Reporting.send_report_test_email)

<a id="reporting"></a>

# reporting

<a id="reporting.Reporting"></a>

## Reporting Objects

```python
class Reporting()
```

The class includes all necessary methods to access the Grafana reporting API endpoints. Be aware that the functionality is a Grafana ENTERPRISE v7.0+ feature

HINT: Note Grafana Enterprise API need required permissions if fine-grained access control is enabled

**Arguments**:

- `grafana_api_model` _APIModel_ - Inject a Grafana API model object that includes all necessary values and information
  

**Attributes**:

- `grafana_api_model` _APIModel_ - This is where we store the grafana_api_model

<a id="reporting.Reporting.get_reports"></a>

#### get\_reports

```python
def get_reports() -> list
```

The method includes a functionality to get all reports

Required Permissions:
Action: reports:read
Scope: [reports:*, reports:id:*]

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _list_ - Returns all reports

<a id="reporting.Reporting.get_report_by_id"></a>

#### get\_report\_by\_id

```python
def get_report_by_id(id: int) -> dict
```

The method includes a functionality to get a report specified by the report id

**Arguments**:

- `id` _int_ - Specify the report id
  
  Required Permissions:
- `Action` - reports:read
- `Scope` - [reports:*, reports:id:*, reports:id:<report_id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the report

<a id="reporting.Reporting.create_report"></a>

#### create\_report

```python
def create_report(report: Report) -> int
```

The method includes a functionality to create a report

**Arguments**:

- `report` _Report_ - Specify the report object
  
  Required Permissions:
- `Action` - reports:create
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _int_ - Returns the report id

<a id="reporting.Reporting.update_report"></a>

#### update\_report

```python
def update_report(id: int, report: Report)
```

The method includes a functionality to update a report

**Arguments**:

- `id` _int_ - Specify the report id
- `report` _Report_ - Specify the report object
  
  Required Permissions:
- `Action` - reports:write
- `Scope` - [reports:*, reports:id:*, reports:id:<report_id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="reporting.Reporting.delete_report"></a>

#### delete\_report

```python
def delete_report(id: int)
```

The method includes a functionality to delete a report specified by the report id

**Arguments**:

- `id` _int_ - Specify the report id
  
  Required Permissions:
- `Action` - reports:delete
- `Scope` - [reports:*, reports:id:*, reports:id:<report_id>]
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="reporting.Reporting.send_report"></a>

#### send\_report

```python
def send_report(id: int,
                emails: str = None,
                use_emails_from_report: bool = None)
```

The method includes a functionality to send a report to a specified email addresses

**Arguments**:

- `id` _int_ - Specify the id of forwarded report. It is the same as in the URL when editing a report, not to be confused with the id of the dashboard.
- `emails` _str_ - Specify the comma-separated list of emails to which to send the report to. Overrides the emails from the report. Required if useEmailsFromReport is not present (default None)
- `use_emails_from_report` _bool_ - Specify if the emails inside the report should be used. Required if emails is not present (default None)
  
  Required Permissions:
- `Action` - reports:send
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="reporting.Reporting.get_report_branding_settings"></a>

#### get\_report\_branding\_settings

```python
def get_report_branding_settings() -> dict
```

The method includes a functionality to get the report branding settings

Required Permissions:
Action: reports.settings:read
Scope: N/A

**Raises**:

- `Exception` - Unspecified error by executing the API call
  

**Returns**:

- `api_call` _dict_ - Returns the report branding settings

<a id="reporting.Reporting.save_report_branding_settings"></a>

#### save\_report\_branding\_settings

```python
def save_report_branding_settings(branding_settings: ReportBrandingSettings)
```

The method includes a functionality to save the report branding settings

**Arguments**:

- `branding_settings` _ReportBrandingSettings_ - Specify the report branding settings object.
  
  Required Permissions:
- `Action` - reports.settings:write
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

<a id="reporting.Reporting.send_report_test_email"></a>

#### send\_report\_test\_email

```python
def send_report_test_email(report: Report)
```

The method includes a functionality to send a test report email

**Arguments**:

- `report` _Report_ - Specify the report object
  
  Required Permissions:
- `Action` - reports: send
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

