# Grafana API SDK
The repository includes an SDK for the Grafana API. It's possible to interact with all publicly available Grafana HTTP API endpoints.

The core features that are implemented inside this SDK:

- All public Grafana API (HTTP) endpoints are supported
- Full API support for Grafana legacy alerting, current alerting, alerting channels, and alert provisioning
- Possibility to specify custom and self-signed certificates
- HTTP/2 support

## Supported Features

The following list describes the currently supported features of the Grafana API functionality.

- [x] [Admin HTTP API](https://grafana.com/docs/grafana/latest/http_api/admin/)
- [x] [Legacy Alerting HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting/)
- [x] [Alerting HTTP API](https://editor.swagger.io/?url=https://raw.githubusercontent.com/grafana/grafana/main/pkg/services/ngalert/api/tooling/post.json)
- [x] [Alerting Notification Channels HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/) 
- [x] [Annotations HTTP API](https://grafana.com/docs/grafana/latest/http_api/annotations/)
- [x] [Authentication HTTP API](https://grafana.com/docs/grafana/latest/http_api/auth/)
- [x] [Dashboard](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
- [x] [Dashboard Permissions](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard_permissions/)
- [x] [Dashboard Versions](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard_versions/)
- [x] [Public Dashboard](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard_public/)
- [x] [Data source HTTP API](https://grafana.com/docs/grafana/latest/http_api/data_source/)
- [x] [Datasource query and resource caching](https://grafana.com/docs/grafana/latest/developers/http_api/query_and_resource_caching/)
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
- [x] [Team Sync](https://grafana.com/docs/grafana/latest/developers/http_api/team_sync/)
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

## TLS/ mTLS for HTTP/1.1

It is possible to pass a custom ssl_context to the underlying library to perform the requests to the HTTP API. For this step and to support custom TLS/ mTLS, there is an option to inject the Python ssl_context. More information can be found [here](https://docs.python.org/3/library/ssl.html#ssl.create_default_context) and a dummy TLS/ mTLS implementation below.

### TLS

```python
import ssl

from grafana_api.model import APIModel

ssl_ctx = ssl.create_default_context(
    ssl.Purpose.SERVER_AUTH,
    cafile="/test/path/ca.crt"
)
ssl_ctx.verify_mode = ssl.CERT_REQUIRED

model: APIModel = APIModel(host="test", token="test", ssl_context=ssl_ctx)
```

### mTLS

```python
import ssl

from grafana_api.model import APIModel

ssl_ctx = ssl.create_default_context(
    ssl.Purpose.SERVER_AUTH,
    cafile="/test/path/ca.crt",
)
ssl_ctx.verify_mode = ssl.CERT_REQUIRED
ssl_ctx.load_cert_chain(certfile="/test/path/client.crt", keyfile="/test/path/client.key")

model: APIModel = APIModel(host="test", token="test", ssl_context=ssl_ctx)
```

## TLS/ mTLS for HTTP/2

It is possible to pass a custom HTTP/2 conform ssl_context to the underlying library to perform the requests to the HTTP API. For this step and to support custom TLS/ mTLS, there is an option to create the ssl_context by the execution of `httpx.create_ssl_context()` function. More information can be found [here](https://github.com/encode/httpx/blob/e99e2948e64fac2ca498865e9742ff50a69a2155/httpx/_config.py#L46) and a dummy TLS/ mTLS implementation below.

### TLS

```python
import httpx

from grafana_api.model import APIModel

ssl_ctx = httpx.create_ssl_context(
    verify="/test/path/ca.crt",
    http2=True,
)

model: APIModel = APIModel(host="test", token="test", ssl_context=ssl_ctx)
```

### mTLS

```python
import httpx

from grafana_api.model import APIModel

ssl_ctx = httpx.create_ssl_context(
    cert=("/test/path/client.crt", "/test/path/client.key"),
    verify="/test/path/ca.crt",
    http2=True,
)

model: APIModel = APIModel(host="test", token="test", ssl_context=ssl_ctx)
```

## Templating
If you want to template your JSON document based on a predefined folder structure you can check out one of my other [project](https://github.com/ZPascal/grafana_dashboard_templater) and integrate the functionality inside your code.
