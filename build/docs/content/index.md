# Grafana API SDK
The repository includes an SDK for the Grafana API. It's possible to communicate with the Grafana API endpoints. Another feature of the SDK is the possibility to specify the used folder for the dashboard.

## Supported Features

The following list describes the currently supported features of the Grafana API functionality.

- [ ] [Admin HTTP API](https://grafana.com/docs/grafana/latest/http_api/admin/)
- [x] [Legacy Alerting HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting/)
- [x] [Alerting HTTP API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/grafana/grafana/main/pkg/services/ngalert/api/tooling/post.json)
- [x] [Alerting Notification Channels HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/) 
- [ ] [Annotations HTTP API](https://grafana.com/docs/grafana/latest/http_api/annotations/)
- [ ] [Authentication HTTP API](https://grafana.com/docs/grafana/latest/http_api/auth/)
- [x] [Data source HTTP API](https://grafana.com/docs/grafana/latest/http_api/data_source/)
- [x] [Datasource Permissions HTTP API](https://grafana.com/docs/grafana/latest/http_api/datasource_permissions/)
- [x] [Folder HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder/)
- [x] [Folder Permissions HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder_permissions/)
- [x] [Search HTTP API](https://grafana.com/docs/grafana/v7.5/http_api/folder_dashboard_search/)
- [ ] [External Group Sync HTTP API](https://grafana.com/docs/grafana/latest/http_api/external_group_sync/)
- [ ] [Fine-grained access control HTTP API](https://grafana.com/docs/grafana/latest/http_api/access_control/)
- [ ] [HTTP Preferences API](https://grafana.com/docs/grafana/latest/http_api/preferences/)
- [ ] [HTTP Snapshot API](https://grafana.com/docs/grafana/latest/http_api/snapshot/)
- [ ] [Library Element HTTP API](https://grafana.com/docs/grafana/latest/http_api/library_element/)
- [ ] [Licensing HTTP API](https://grafana.com/docs/grafana/latest/http_api/licensing/)
- [ ] [Organization HTTP API](https://grafana.com/docs/grafana/latest/http_api/org/)
- [ ] [Other HTTP API](https://grafana.com/docs/grafana/latest/http_api/other/)
- [ ] [Playlist HTTP API](https://grafana.com/docs/grafana/latest/http_api/playlist/)
- [ ] [Reporting API](https://grafana.com/docs/grafana/latest/http_api/reporting/)
- [ ] [Short URL HTTP API](https://grafana.com/docs/grafana/latest/http_api/short_url/)
- [ ] [Team HTTP API](https://grafana.com/docs/grafana/latest/http_api/team/)
- [ ] [User HTTP API](https://grafana.com/docs/grafana/latest/http_api/user/)

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