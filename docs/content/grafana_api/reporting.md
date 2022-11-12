# Table of Contents

* [reporting](#reporting)
  * [Reporting](#reporting.Reporting)
    * [send\_report](#reporting.Reporting.send_report)

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

<a id="reporting.Reporting.send_report"></a>

#### send\_report

```python
def send_report(id: int,
                emails: str = None,
                use_emails_from_report: bool = None)
```

The method includes a functionality to send a report to a specified email addresses

**Arguments**:

- `id` _int_ - Specify the id of sented report. It is the same as in the URL when editing a report, not to be confused with the id of the dashboard.
- `emails` _str_ - Specify the comma-separated list of emails to which to send the report to. Overrides the emails from the report. Required if useEmailsFromReport is not present (default None)
- `use_emails_from_report` _bool_ - Specify the if the emails inside the report should be used. Required if emails is not present (default None)
  
  Required Permissions:
- `Action` - reports:send
- `Scope` - N/A
  

**Raises**:

- `ValueError` - Missed specifying a necessary value
- `Exception` - Unspecified error by executing the API call
  

**Returns**:

  None

