# Grafana API SDK
The repository includes an SDK for the Grafana API. It's possible to communicate with the Grafana API endpoints. Another feature of the SDK is the possibility to specify the used folder for the dashboard.

## Supported Features

The following list describes the currently supported features of the Grafana API functionality.

- [x] [Admin HTTP API](https://grafana.com/docs/grafana/latest/http_api/admin/)
- [x] [Legacy Alerting HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting/)
- [x] [Alerting HTTP API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/grafana/grafana/main/pkg/services/ngalert/api/tooling/post.json)
- [x] [Alerting Notification Channels HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/) 
- [x] [Annotations HTTP API](https://grafana.com/docs/grafana/latest/http_api/annotations/)
- [x] [Authentication HTTP API](https://grafana.com/docs/grafana/latest/http_api/auth/)
- [x] [Data source HTTP API](https://grafana.com/docs/grafana/latest/http_api/data_source/)
- [x] [Datasource Permissions HTTP API](https://grafana.com/docs/grafana/latest/http_api/datasource_permissions/)
- [x] [Folder HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder/)
- [x] [Folder Permissions HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder_permissions/)
- [x] [Search HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder_dashboard_search/)
- [x] [External Group Sync HTTP API](https://grafana.com/docs/grafana/latest/http_api/external_group_sync/)
- [x] [Access control HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/access_control/)
- [x] [HTTP Preferences API](https://grafana.com/docs/grafana/latest/http_api/preferences/)
- [x] [HTTP Snapshot API](https://grafana.com/docs/grafana/latest/http_api/snapshot/)
- [x] [Library Element HTTP API](https://grafana.com/docs/grafana/latest/http_api/library_element/)
- [x] [Query History API](https://grafana.com/docs/grafana/latest/http_api/query_history/)
- [x] [Licensing HTTP API](https://grafana.com/docs/grafana/latest/http_api/licensing/)
- [x] [Organization HTTP API](https://grafana.com/docs/grafana/latest/http_api/org/)
- [x] [Other HTTP API](https://grafana.com/docs/grafana/latest/http_api/other/)
- [x] [Playlist HTTP API](https://grafana.com/docs/grafana/latest/http_api/playlist/)
- [x] [Reporting API](https://grafana.com/docs/grafana/latest/http_api/reporting/)
- [x] [Short URL HTTP API](https://grafana.com/docs/grafana/latest/http_api/short_url/)
- [x] [Team HTTP API](https://grafana.com/docs/grafana/latest/http_api/team/)
- [x] [User HTTP API](https://grafana.com/docs/grafana/latest/http_api/user/)
- [x] [Service Account HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/)
- [x] [RBAC HTTP API](https://grafana.com/docs/grafana/latest/http_api/access_control/)
- [x] [Correlations API](https://grafana.com/docs/grafana/latest/developers/http_api/correlations/)
- [x] [Alerting Provisioning HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)

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