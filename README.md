# Grafana API SDK ![Coverage report](https://github.com/ZPascal/grafana_api_sdk/blob/main/docs/coverage.svg)
The repository includes an SDK for the Grafana API. It's possible to communicate with the Grafana API endpoints. Another feature of the SDK is the possibility to specify the used folder for the dashboard.

## Currently, supported features

### Dashboard
- Create/ Update a dashboard 
- Delete a dashboard
- Get permissions of a dashboard
- Update the permissions of a dashboard
- Get all dashboard versions
- Get dashboard version of a specific dashboard
- Restore a dashboard version of a specific dashboard
- Compare two dashboard versions and extract the diff between booth dashboards

### Folder
- Get folder id by dashboard path
- Get all folder ids and folder names 
- Get all folders
- Get folder by uid
- Get folder by id
- Create a folder
- Update a folder
- Delete a folder
- Get permissions for a folder
- Update permissions for a folder

### Search
- Execute a custom query against the Grafana search endpoint

## Feature timeline

The following table describes the plan to implement the rest of the Grafana API functionality. Please, open an issue and vote them up, if you prefer a faster implementation of an API functionality.

| API endpoint group | Implementation week | Maintainer | PR | State |
|:------------------:|:-------------------:|:----------:|:--:|:-----:|
| [Admin HTTP API](https://grafana.com/docs/grafana/latest/http_api/admin/) |                     |            |    |    |
| [Alerting HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting/)  | 4 | [ZPascal](https://github.com/ZPascal) |  | Planned |
| [Alerting Notification Channels HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/) | 4 | [ZPascal](https://github.com/ZPascal) |    | Planned |
| [Annotations HTTP API](https://grafana.com/docs/grafana/latest/http_api/annotations/) |                   |            |    |    |
| [Authentication HTTP API](https://grafana.com/docs/grafana/latest/http_api/auth/) |                |            |    |    |
| [Data source HTTP API](https://grafana.com/docs/grafana/latest/http_api/data_source/) | 5 | [ZPascal](https://github.com/ZPascal) |    | Planned |
| [Datasource Permissions HTTP API](https://grafana.com/docs/grafana/latest/http_api/datasource_permissions/) |        |            |    |    |
| [External Group Sync HTTP API](https://grafana.com/docs/grafana/latest/http_api/external_group_sync/) |           |            |    |    |
| [Fine-grained access control HTTP API](https://grafana.com/docs/grafana/latest/http_api/access_control/) |   |            |    |    |
| [HTTP Preferences API](https://grafana.com/docs/grafana/latest/http_api/preferences/) |                   |            |    |    |
| [HTTP Snapshot API](https://grafana.com/docs/grafana/latest/http_api/snapshot/) |                      |            |    |    |
| [Library Element HTTP API](https://grafana.com/docs/grafana/latest/http_api/library_element/) |               |            |    |    |
| [Licensing HTTP API](https://grafana.com/docs/grafana/latest/http_api/licensing/) |                     |            |    |    |
| [Organization HTTP API](https://grafana.com/docs/grafana/latest/http_api/org/) |                  |            |    |    |
| [Other HTTP API](https://grafana.com/docs/grafana/latest/http_api/other/) |                         |            |    |    |
| [Playlist HTTP API](https://grafana.com/docs/grafana/latest/http_api/playlist/) |                      |            |    |    |
| [Reporting API](https://grafana.com/docs/grafana/latest/http_api/reporting/) |                          |            |    |    |
| [Short URL HTTP API](https://grafana.com/docs/grafana/latest/http_api/short_url/) |                     |            |    |    |
| [Team HTTP API](https://grafana.com/docs/grafana/latest/http_api/team/) |                          |            |    |    |
| [User HTTP API](https://grafana.com/docs/grafana/latest/http_api/user/) |                          |            |    |    |

## Installation

`pip install grafana-api-sdk`

## Example

```python
import json

from grafana_api.model import APIModel
from grafana_api.dashboard import Dashboard

model: APIModel = APIModel(host="test", token="test")

dashboard: Dashboard = Dashboard(model)

with open("/tmp/test/test.json") as file:
    json_dashboard = json.load(file)

dashboard.create_or_update_dashboard(message="Create a new test dashboard", dashboard_json=json_dashboard, dashboard_path="test")
```

## Templating
If you want to template your JSON document based on a predefined folder structure you can check out one of my other [project](https://github.com/ZPascal/grafana_dashboard_templater) and integrate the functionality inside your code.

## Contribution
If you would like to contribute something, have an improvement request, or want to make a change inside the code, please open a pull request.

## Support
If you need support, or you encounter a bug, please don't hesitate to open an issue.

## Donations
If you would like to support my work, I ask you to take an unusual action inside the open source community. Donate the money to a non-profit organization like Doctors Without Borders or the Children's Cancer Aid. I will continue to build tools because I like it and it is my passion to develop and share applications.

## License
This product is available under the Apache 2.0 license.