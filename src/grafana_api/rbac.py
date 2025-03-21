import json
import logging

from .model import APIModel, APIEndpoints, RequestsMethods, CustomRole
from .api import Api


class RBAC:
    """The class includes all necessary methods to access the Grafana RBAC API endpoints. Be aware that the functionality is a Grafana ENTERPRISE feature

    Args:
        grafana_api_model (APIModel): Inject a Grafana API model object that includes all necessary values and information

    Attributes:
        grafana_api_model (APIModel): This is where we store the grafana_api_model
    """

    def __init__(self, grafana_api_model: APIModel):
        self.grafana_api_model = grafana_api_model

    def get_status(self) -> bool:
        """The method includes a functionality to get the status if role-based access control is enabled or not

        Required Permissions:
            Action: status:accesscontrol
            Scope: services:accesscontrol

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (bool): Return a flag indicating if the role-based access control is enabled or not
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.RBAC.value}/status", response_status_code=True
        )

        status_code: int = api_call.get("status")

        alert_manager_status_dict: dict = dict(
            {
                403: "Access denied.",
                404: "Not found, an indication that role-based access control is not available at all.",
                500: "Unexpected error. Refer to body and/or server logs for more details.",
            }
        )

        if status_code == 200:
            return bool(api_call.get("enabled"))
        elif 403 <= status_code <= 500:
            logging.error(alert_manager_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def get_all_roles(self, include_hidden_roles: bool = False) -> list:
        """The method includes a functionality gets all existing roles. The response contains all global and organization local roles, for the organization which user is signed in

        Args:
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: roles:read
            Scope: roles:*

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return all global and organization local roles
        """

        additional_parameters: str = ""
        if include_hidden_roles:
            additional_parameters = "?includeHidden=true"

        api_call: list = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.RBAC.value}/roles{additional_parameters}",
            response_status_code=True,
        )

        status_code: int = api_call[0].get("status")

        alert_manager_status_dict: dict = dict(
            {
                403: "Access denied.",
                500: "Unexpected error. Refer to body and/or server logs for more details.",
            }
        )

        if status_code == 200:
            return api_call
        elif 403 <= status_code <= 500:
            logging.error(alert_manager_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception

    def get_role(self, uid: str) -> dict:
        """The method includes a functionality get a role specified by the uid

        Args:
            uid (str): Specify the uid of the role

        Required Permissions:
            Action: roles:read
            Scope: roles:*

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the corresponding role
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/roles/{uid}", response_status_code=True
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def create_role(self, role_definition: CustomRole) -> dict:
        """The method includes a functionality create a new custom role and maps given permissions to that role. Note that roles with the same prefix as Fixed roles can’t be created

        Args:
            role_definition (CustomRole): Specify the corresponding role definition

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the newly created role
        """

        if role_definition is not None and len(role_definition.name) != 0:
            role_object: dict = dict(
                {
                    "name": role_definition.name,
                    "global": role_definition.global_role,
                    "hidden": role_definition.hidden,
                }
            )

            if role_definition.uid is not None:
                role_object.update(dict({"uid": role_definition.uid}))

            if role_definition.version is not None:
                role_object.update(dict({"version": role_definition.version}))

            if role_definition.description is not None:
                role_object.update(dict({"description": role_definition.description}))

            if role_definition.display_name is not None:
                role_object.update(dict({"displayName": role_definition.display_name}))

            if role_definition.group is not None:
                role_object.update(dict({"group": role_definition.group}))

            if role_definition.permissions is not None:
                permission_list: list = list()
                for permission in role_definition.permissions:
                    permission_object: dict = dict()
                    if permission.action is not None:
                        permission_object.update({"action": permission.action})
                    else:
                        logging.error("There is no permission action value defined.")
                        raise ValueError

                    if permission.scope is not None:
                        permission_object.update({"scope": permission.scope})

                    permission_list.append(permission_object)
                role_object.update(dict({"permissions": permission_list}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/roles",
                RequestsMethods.POST,
                json.dumps(role_object),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    400: "Bad request (invalid json, missing content-type, missing or invalid fields, etc.).",
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 400 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no role_definition or name defined.")
            raise ValueError

    def update_role(self, uid: str, role_definition: CustomRole) -> dict:
        """The method includes a functionality to update the role with the given uid, and its permissions. The operation is idempotent and all permissions of the role will be replaced based on the request content. You need to increment the version of the role with each update, otherwise the request will fail

        Args:
            uid (str): Specify the corresponding uid of the custom role
            role_definition (CustomRole): Specify the corresponding role definition

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (dict): Return the updated role
        """

        if (
            role_definition is not None
            and len(role_definition.name) != 0
            and role_definition.version != 0
            and len(uid) != 0
        ):
            role_object: dict = dict(
                {
                    "name": role_definition.name,
                    "global": role_definition.global_role,
                    "hidden": role_definition.hidden,
                    "version": role_definition.version,
                }
            )

            if role_definition.description is not None:
                role_object.update(dict({"description": role_definition.description}))

            if role_definition.display_name is not None:
                role_object.update(dict({"displayName": role_definition.display_name}))

            if role_definition.group is not None:
                role_object.update(dict({"group": role_definition.group}))

            if role_definition.permissions is not None:
                permission_list: list = list()
                for permission in role_definition.permissions:
                    permission_object: dict = dict()
                    if permission.action is not None:
                        permission_object.update({"action": permission.action})
                    else:
                        logging.error("There is no permission action value defined.")
                        raise ValueError

                    if permission.scope is not None:
                        permission_object.update({"scope": permission.scope})

                    permission_list.append(permission_object)
                role_object.update(dict({"permissions": permission_list}))

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/roles/{uid}",
                RequestsMethods.PUT,
                json.dumps(role_object),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    400: "Bad request (invalid json, missing content-type, missing or invalid fields, etc.).",
                    403: "Access denied.",
                    404: "Role was not found to update.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 400 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no role_definition, version, name or uid defined.")
            raise ValueError

    def delete_role(self, uid: str, force: bool = False, global_role: bool = False):
        """The method includes a functionality to delete a role with the given uid

        Args:
            uid (str): Specify the corresponding uid of the custom role
            force (bool): Specify the corresponding if the role will be deleted with all it’s assignments or not (default False)
            global_role (bool): Specify the corresponding if the role is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: roles:delete
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if len(uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/roles/{uid}?force={force.__str__().lower()}&"
                f"global={global_role.__str__().lower()}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    400: "Bad request (invalid json, missing content-type, missing or invalid fields, etc.).",
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role deleted" != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully destroyed the role.")
            elif 400 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no uid defined.")
            raise ValueError

    def get_user_assigned_roles(
        self, user_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get the roles that have been directly assigned to a given user specified by the user id. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin), and it does not include roles that have been inherited from a team

        Args:
            user_id (int): Specify the corresponding user_id of the user
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: users.roles:read
            Scope: users:id:<user ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding user roles
        """

        if user_id != 0 and user_id is not None:
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{user_id}/roles{additional_parameters}",
                response_status_code=True,
            )

            status_code: int = api_call[0].get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.error("There is no user_id defined.")
            raise ValueError

    def get_user_assigned_permissions(self, user_id: int) -> list:
        """The method includes a functionality to get the permissions that have been directly assigned to a given user specified by the user id

        Args:
            user_id (int): Specify the corresponding user_id of the user

        Required Permissions:
            Action: users.permissions:read
            Scope: users:id:<user ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding user permissions
        """

        if user_id != 0 and user_id is not None:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{user_id}/permissions",
                response_status_code=True,
            )

            status_code: int = api_call[0].get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
            raise Exception
        else:
            logging.error("There is no user_id defined.")
            raise ValueError

    def add_user_role_assignment(
        self, user_id: int, role_uid: str, global_assignment: bool = False
    ):
        """The method includes a functionality to assign a role to a specific user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uid (str): Specify the corresponding uid of the role
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0 and user_id is not None and len(role_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{user_id}/roles",
                RequestsMethods.POST,
                json.dumps({"global": global_assignment, "roleUid": role_uid}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role added to the user." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully added the role of the user.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no user_id or role_uid defined.")
            raise ValueError

    def remove_user_role_assignment(self, user_id: int, role_uid: str):
        """The method includes a functionality to revoke a role to a specific user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0 and user_id is not None and len(role_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{user_id}/roles/{role_uid}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role removed from user." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully removed the role of the user.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no user_id or role_uid defined.")
            raise ValueError

    def update_user_role_assignments(
        self,
        user_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
        global_assignment: bool = False,
    ):
        """The method includes a functionality to update the user role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            user_id (int): Specify the corresponding user_id of the user
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add, users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if user_id != 0 and user_id is not None and len(role_uids) != 0:
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{user_id}/roles{additional_parameters}",
                RequestsMethods.PUT,
                json.dumps({"global": global_assignment, "roleUids": role_uids}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "User roles have been updated." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully updated the roles of the user.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no user_id or role_uids defined.")
            raise ValueError

    def get_service_account_assigned_roles(
        self, service_account_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get the roles that have been directly assigned to a given service account. The list does not include basic roles (Viewer, Editor, Admin or Grafana Admin)

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: users.roles:read
            Scope: users:id:<service account ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding service account roles
        """

        if service_account_id != 0 and service_account_id is not None:
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{service_account_id}/roles{additional_parameters}",
                response_status_code=True,
            )

            status_code: int = api_call[0].get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no service_account_id defined.")
            raise ValueError

    def get_service_account_assigned_permissions(self, service_account_id: int) -> list:
        """The method includes a functionality to get the permissions that a given service account has

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account

        Required Permissions:
            Action: users.permissions:read
            Scope: users:id:<service account ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding service account permissions
        """

        if service_account_id != 0 and service_account_id is not None:
            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{service_account_id}/permissions",
                response_status_code=True,
            )

            status_code: int = api_call[0].get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no service_account_id defined.")
            raise ValueError

    def add_service_account_role_assignment(
        self, service_account_id: int, role_uid: str, global_assignment: bool = False
    ):
        """The method includes a functionality to assign a role to a specific service account

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uid (str): Specify the corresponding uid of the role
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            service_account_id != 0
            and service_account_id is not None
            and len(role_uid) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{service_account_id}/roles",
                RequestsMethods.POST,
                json.dumps({"global": global_assignment, "roleUid": role_uid}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")
            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role added to the user." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info(
                        "You successfully added the role of the service account."
                    )
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no service_account_id or role_uid defined.")
            raise ValueError

    def remove_service_account_role_assignment(
        self, service_account_id: int, role_uid: str
    ):
        """The method includes a functionality to revoke a role to a specific service account

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            service_account_id != 0
            and service_account_id is not None
            and len(role_uid) != 0
        ):
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{service_account_id}/roles/{role_uid}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role removed from user." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info(
                        "You successfully removed the role of the service account."
                    )
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no service_account_id or role_uid defined.")
            raise ValueError

    def update_service_account_role_assignments(
        self,
        service_account_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
        global_assignment: bool = False,
    ):
        """The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            service_account_id (int): Specify the corresponding service_account_id of the service account
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)
            global_assignment (bool): Specify the corresponding if the assignment is global or not. If set to false, the default org id of the authenticated user will be used from the request (default False)

        Required Permissions:
            Action: users.roles:add, users.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if (
            service_account_id != 0
            and service_account_id is not None
            and len(role_uids) != 0
        ):
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/users/{service_account_id}/roles{additional_parameters}",
                RequestsMethods.PUT,
                json.dumps({"global": global_assignment, "roleUids": role_uids}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "User roles have been updated." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info(
                        "You successfully updated the roles of the service account."
                    )
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no service_account_id or role_uids defined.")
            raise ValueError

    def get_team_assigned_roles(
        self, team_id: int, include_hidden_roles: bool = False
    ) -> list:
        """The method includes a functionality to get that have been directly assigned to a given team.

        Args:
            team_id (int): Specify the corresponding team_id of the team
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: teams.roles:read
            Scope: teams:id:<team ID>

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            api_call (list): Return the corresponding team roles
        """

        if team_id != 0 and team_id is not None:
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: list = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/teams/{team_id}/roles{additional_parameters}",
                response_status_code=True,
            )

            status_code: int = api_call[0].get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                return api_call
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no team_id defined.")
            raise ValueError

    def add_team_role_assignment(self, team_id: int, role_uid: str):
        """The method includes a functionality to assign a role to a specific team

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: teams.roles:add
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if team_id != 0 and team_id is not None and len(role_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/teams/{team_id}/roles",
                RequestsMethods.POST,
                json.dumps({"roleUid": role_uid}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role added to the team." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully added the role of the team.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no team_id or role_uid defined.")
            raise ValueError

    def remove_team_role_assignment(self, team_id: int, role_uid: str):
        """The method includes a functionality to revoke a role to a specific team

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uid (str): Specify the corresponding uid of the role

        Required Permissions:
            Action: teams.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if team_id != 0 and team_id is not None and len(role_uid) != 0:
            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/teams/{team_id}/roles/{role_uid}",
                RequestsMethods.DELETE,
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Role removed from team." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully removed the role of the team.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no team_id or role_uid defined.")
            raise ValueError

    def update_team_role_assignments(
        self,
        team_id: int,
        role_uids: list,
        include_hidden_roles: bool = False,
    ):
        """The method includes a functionality to update the service account role assignments to match the provided set of uid's. This will remove any assigned roles that aren’t in the request and add roles that are in the set but are not already assigned to the user

        Args:
            team_id (int): Specify the corresponding team_id of the team
            role_uids (list): Specify the corresponding uids of the role
            include_hidden_roles (bool): Specify if the output contains the hidden roles or not (default False)

        Required Permissions:
            Action: teams.roles:add, teams.roles:remove
            Scope: permissions:type:delegate

        Raises:
            ValueError: Missed specifying a necessary value
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        if team_id != 0 and team_id is not None and len(role_uids) != 0:
            additional_parameters: str = ""
            if include_hidden_roles:
                additional_parameters = "?includeHidden=true"

            api_call: dict = Api(self.grafana_api_model).call_the_api(
                f"{APIEndpoints.RBAC.value}/teams/{team_id}/roles{additional_parameters}",
                RequestsMethods.PUT,
                json.dumps({"roleUids": role_uids}),
                response_status_code=True,
            )

            status_code: int = api_call.get("status")

            alert_manager_status_dict: dict = dict(
                {
                    403: "Access denied.",
                    404: "Role not found.",
                    500: "Unexpected error. Refer to body and/or server logs for more details.",
                }
            )

            if status_code == 200:
                if "Team roles have been updated." != api_call.get("message"):
                    logging.error(f"Please, check the error: {api_call}.")
                    raise Exception
                else:
                    logging.info("You successfully updated the roles of the team.")
            elif 403 <= status_code <= 500:
                logging.error(alert_manager_status_dict.get(status_code))
                raise Exception
            else:
                logging.error(f"Check the error: {api_call}.")
                raise Exception
        else:
            logging.error("There is no team_id or role_uids defined.")
            raise ValueError

    def reset_basic_roles_to_their_default(self):
        """The method includes a functionality to reset basic roles permissions to their default

        Required Permissions:
            Action: roles:write
            Scope: permissions:type:escalate

        Raises:
            Exception: Unspecified error by executing the API call

        Returns:
            None
        """

        api_call: dict = Api(self.grafana_api_model).call_the_api(
            f"{APIEndpoints.RBAC.value}/roles/hard-reset",
            RequestsMethods.POST,
            json.dumps({"BasicRoles": True}),
            response_status_code=True,
        )

        status_code: int = api_call.get("status")

        alert_manager_status_dict: dict = dict(
            {
                500: "Failed to reset basic roles.",
            }
        )

        if status_code == 200:
            if "Reset performed" != api_call.get("message"):
                logging.error(f"Please, check the error: {api_call}.")
                raise Exception
            else:
                logging.info("You successfully performed the reset.")
        elif 403 <= status_code <= 500:
            logging.error(alert_manager_status_dict.get(status_code))
            raise Exception
        else:
            logging.error(f"Check the error: {api_call}.")
            raise Exception
