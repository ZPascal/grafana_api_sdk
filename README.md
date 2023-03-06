# Grafana API SDK ![Coverage report](https://github.com/ZPascal/grafana_api_sdk/blob/main/docs/coverage.svg)
The repository includes a Python SDK for the Grafana API. It's possible to communicate with the Grafana API endpoints. Another feature of the SDK is the possibility to specify the used folder for the dashboard.

## Differences between [grafana-client](https://github.com/panodata/grafana-client), [grafana_api](https://github.com/m0nhawk/grafana_api/) and the [grafana_api_sdk](https://github.com/ZPascal/grafana_api_sdk)
The grafana-client is only a fork of the non-maintained grafana_api repository. In general, the grafana-client project started at the same time, as I started this project. The corresponding SDK is a completely new project and based on non-other project and include a few features that are currently not implemented inside the grafana-client.

The main feature that is implemented inside this library:

- Grafana V8 Alerting API support (possibility to communicate (currently read only) with the attached Prometheus and Alertmanager)

In general my focus inside this project is to implement and deliver old and new features from the Grafana API, to document all features and functionality clear and to increase the overall test coverage of the project.

## Currently, supported features

### Dashboard
- Create/ Update a dashboard 
- Delete a dashboard
- Get permissions of a dashboard
- Get permissions of a dashboard by uid
- Update the permissions of a dashboard
- Update the permissions of a dashboard by uid
- Get all dashboard versions
- Get all dashboard versions by uid
- Get dashboard version of a specific dashboard
- Get dashboard version of a specific dashboard by uid
- Restore a dashboard version of a specific dashboard
- Restore a dashboard version of a specific dashboard by uid
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

### Datasource
- Get all datasources
- Get the datasource by id
- Get the datasource by uid
- Get the datasource by name
- Get the datasource id by name
- Create a new datasource
- Update a datasource
- Delete a datasource by id
- Delete a datasource by uid
- Delete a datasource by name
- Query a datasource by id
- Enabled datasource permissions
- Disable datasource permissions
- Get datasource permissions
- Add datasource permissions
- Delete datasource permissions

### Legacy Alerting
- Get alerts
- Get alerts by dashboard ids
- Get alert by id
- Pause alert by id
- Unpause alert by id

### Alerting
- Get all Alertmanager alerts
- Create or update Alertmanager alerts
- Get Alertmanager group alerts
- Get all Alertmanager silences
- Get Alertmanager silence by id
- Create or update Alertmanager silence
- Delete Alertmanager silence by id
- Get Alertmanager status
- Get the Alertmanager config
- Create or update the Alertmanager config
- Delete the Alertmanager config
- Test the Alertmanager receivers
- Get Prometheus alerts
- Get Prometheus rules
- Get Ruler rules
- Get a Ruler group
- Get Ruler groups by the namespace
- Create or update the Ruler group by the namespace
- Delete a Ruler group
- Delete a Ruler namespace
- Test a datasource rule
- Test a recipient rule
- Get the NGAlert organization configuration
- Get the NGAlert Alertmanager configuration by the organization
- Create or update the NGAlert organization configuration
- Delete the NGAlert organization configuration

### Alerting Channels
- Get all notification channels
- Get all notification channels (lookup)
- Get a notification channel by id
- Get a notification channel by uid
- Create an notification channel
- Update a notification channel by id
- Update a notification channel by uid
- Delete a notification channel by id
- Delete a notification channel by uid
- Test a notification channel

### Alerting Provisioning
- Get alert rule
- Add alert rule
- Update alert rule
- Update ethe interval fo the alert rule group
- Delete alert rule
- Get all contact points
- Add contact point
- Update contact point
- Delete contact point
- Get notification policies
- Add notification policies
- Get all mute timings
- Get mute timings
- Add mute timing
- Update mute timing
- Delete mute timing
- Get all message templates
- Get message template
- Create or update message template
- Delete message template

### Organization
- Get current organisation
- Update the current organisation name
- Add a new user and the role to the current organisation
- Get all users from current organisation
- Get all users from current organisation (lookup)
- Update the role of an organisation user by the user id
- Delete an organisation user by the user id
- Get an organisation by the id
- Get an organisation by the name
- Get all organisations
- Create an organisation
- Update an organisation
- Delete an organisation
- Get organisation users
- Add a new organisation user
- Update an organisation user
- Delete an organisation user

### Short URL
- Create a short url

### User
- Search users
- Get user by id
- Get user by username or email
- Update the user
- Get user organizations
- Get user teams
- Switch the specific user context
- Get the current user
- Update the current user
- Update the current password
- Switch current user context
- Get current user organizations
- Get current user teams
- Star a dashboard
- Unstar a dashboard
- Get auth tokens
- Revoke auth tokens

### Snapshot
- Create a new snapshot
- Get all snapshots
- Get a specific snapshot by key
- Delete snapshot by key
- Delete snapshot by delete key

### Team
- Search team
- Get team by id
- Add team
- Update team
- Delete team by id
- Get team members
- Add team member
- Delete team member
- Get team preferences
- Update team preferences

### Legacy Playlist
- Search playlist
- Get playlist by id
- Get playlist items by id
- Get playlist dashboards by id
- Create playlist
- Update playlist by id
- Delete playlist by id

### Playlist
- Search playlist
- Get playlist by uid
- Get playlist items by uid
- Get playlist dashboards by uid
- Create playlist
- Update playlist by uid
- Delete playlist by uid

### Reporting
- Send report

### Query History
- Add query to history
- Delete query inside the history
- Update query inside the history
- Search inside the query history
- Star a query inside the history
- Unstar a query inside the history

### Other HTTP
- Get frontend settings
- Renew login session 
- Get health status
- Get metrics

### Licensing
- Check license availability
- Manually force license refresh
- Remove the license from the database

### Annotation
- Find annotations
- Create annotation
- Create graphite annotation
- Update annotation
- Delete annotation
- Find annotation tags

### External Groups
- Get external groups
- Add external group
- Remove external group

### Authentication
- Get api tokens
- Create a api token
- Delete a api token

### Preferences
- Get current user preferences
- Update current user preferences
- Get current org preferences
- Update current org preferences

### Admin
- Get settings
- Update settings
- Get stats
- Get preview report
- Create global user
- Update user password
- Update user permissions
- Delete global user
- Pause all alerts
- Unpause all alerts
- Get user auth tokens
- Revoke user auth token
- Logout user
- Reload dashboard provisioning configuration
- Reload datasource provisioning configuration
- Reload plugins provisioning configuration
- Reload notifications provisioning configuration
- Reload access controls provisioning configuration
- Reload LDAP provisioning configuration
- Rotate data encryption keys

### Service Account
- Search service accounts
- Create a service account
- Get service account by id
- Update a service account
- Get service account token by id
- Create service account token by id
- Delete service account by id

### RBAC
- Get status
- Get all roles
- Get role
- Create role
- Update role
- Delete role
- Get user assigned roles
- Get user assigned permissions
- Add user role assignment
- Update user role assignment
- Remove user role assignment
- Get service account assigned roles
- Get service account assigned permissions
- Add service account role assignment
- Update service account role assignment
- Remove service account role assignment
- Get team assigned roles
- Add team role assignment
- Update team role assignment
- Remove team role assignment
- Reset basic roles to their default

### Library
- Get all library elements
- Get library element by uid
- Get library element by name
- Get library element connections
- Create library element
- Update library element
- Delete library element

### Correlations
- Get correlation
- Get all correlations by datasource uid
- Get all correlations
- Create correlations
- Update correlations
- Delete correlations

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
