from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_mtm_client,
)


def register_leanix_mtm_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-mtm"})
    async def leanix_leanix_mtm(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaiaccess', 'gettaskbyid', 'createworkspacelabel', 'deleteworkspacelabel', 'getall', 'getlabelsbyworkspace', 'getlabelsbyworkspaces', 'token', 'get_data_breach_contact', 'add_data_breach_contact', 'delete_data_breach_contact', 'get_accounts', 'create_account', 'get_account', 'update_account', 'delete_account', 'get_contracts', 'get_events', 'get_instances', 'get_settings', 'get_users', 'get_workspaces', 'getapitokens', 'createapitoken', 'getapitoken', 'updateapitoken', 'deleteapitoken', 'getfeature', 'accessfeature', 'getapplication', 'getapplications', 'getedition', 'geteditions', 'getfeatures', 'create_contract', 'get_contract', 'update_contract', 'delete_contract', 'get_custom_features', 'create_custom_feature', 'get_custom_feature', 'update_custom_feature', 'delete_custom_feature', 'deletedomain', 'getdomain', 'getdomains', 'upsertdomain', 'getidentityproviders', 'getworkspaces_2', 'create_event', 'get_event', 'update_event', 'getraw', 'get_export', 'process_graph_ql', 'get_identity_providers', 'create_identity_provider', 'get_identity_provider', 'update_identity_provider', 'delete_identity_provider', 'get_domains', 'get_metadata', 'getworkspaces_3', 'activate', 'authenticate', 'checkip', 'invite', 'login', 'loginpractitioner', 'logout', 'reset_password', 'review', 'set_password', 'switchpermissionrole', 'inactive', 'create_instance', 'get_instance', 'update_instance', 'delete_instance', 'getinstancesbyworkspace', 'getpreferredinstance', 'switchdefaultinstance', 'list', 'create', 'invalidate', 'getpermissions', 'createpermission', 'getpermission', 'getsettings_2', 'getuserrandom', 'getsettings_3', 'createsetting', 'getsetting', 'updatesetting', 'deletesetting', 'getnotificationsettings', 'setworkspacenotificationstatus', 'gettechnicalusers', 'create_technical_user', 'get_technical_user', 'update_technical_user', 'delete_technical_user', 'replace_technical_user_api_token', 'getusers_1', 'createuser', 'createuserpassword', 'getevents_6', 'getpermissions_1', 'getsettings_4', 'getuser', 'updateuser', 'getuserrandom_1', 'setpassword_1', 'create_workspace', 'get_workspace', 'update_workspace', 'delete_workspace', 'get_feature_bundle', 'get_impersonations', 'get_permission', 'get_permission_stats', 'get_permissions', 'get_support_permissions', 'get_user_list_export', 'getworkspacesforbackup', 'permissions_search', 'getuserpiichanges', 'get_user_segment', 'create_or_update_user_segment', 'getworkspacemaintenance', 'createworkspacemaintenance', 'deleteworkspacemaintenance', 'get_contracts_1', 'get_custom_features_1', 'get_custom_features_2', 'get_domains_1', 'get_events_1', 'get_events_2', 'get_events_3', 'get_events_4', 'get_events_5', 'get_events_6', 'get_instances_1', 'get_instances_2', 'get_settings_1', 'get_settings_2', 'get_users_1', 'get_users_2', 'get_workspaces_1', 'get_workspaces_2', 'get_workspaces_3', 'get_custom_feature_1'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_mtm_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix mtm operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getaiaccess":
            return client.getaiaccess(**kwargs)
        if action == "gettaskbyid":
            return client.gettaskbyid(**kwargs)
        if action == "createworkspacelabel":
            return client.createworkspacelabel(**kwargs)
        if action == "deleteworkspacelabel":
            return client.deleteworkspacelabel(**kwargs)
        if action == "getall":
            return client.getall(**kwargs)
        if action == "getlabelsbyworkspace":
            return client.getlabelsbyworkspace(**kwargs)
        if action == "getlabelsbyworkspaces":
            return client.getlabelsbyworkspaces(**kwargs)
        if action == "token":
            return client.token(**kwargs)
        if action == "get_data_breach_contact":
            return client.get_data_breach_contact(**kwargs)
        if action == "add_data_breach_contact":
            return client.add_data_breach_contact(**kwargs)
        if action == "delete_data_breach_contact":
            return client.delete_data_breach_contact(**kwargs)
        if action == "get_accounts":
            return client.get_accounts(**kwargs)
        if action == "create_account":
            return client.create_account(**kwargs)
        if action == "get_account":
            return client.get_account(**kwargs)
        if action == "update_account":
            return client.update_account(**kwargs)
        if action == "delete_account":
            return client.delete_account(**kwargs)
        if action == "get_contracts":
            return client.get_contracts(**kwargs)
        if action == "get_events":
            return client.get_events(**kwargs)
        if action == "get_instances":
            return client.get_instances(**kwargs)
        if action == "get_settings":
            return client.get_settings(**kwargs)
        if action == "get_users":
            return client.get_users(**kwargs)
        if action == "get_workspaces":
            return client.get_workspaces(**kwargs)
        if action == "getapitokens":
            return client.getapitokens(**kwargs)
        if action == "createapitoken":
            return client.createapitoken(**kwargs)
        if action == "getapitoken":
            return client.getapitoken(**kwargs)
        if action == "updateapitoken":
            return client.updateapitoken(**kwargs)
        if action == "deleteapitoken":
            return client.deleteapitoken(**kwargs)
        if action == "getfeature":
            return client.getfeature(**kwargs)
        if action == "accessfeature":
            return client.accessfeature(**kwargs)
        if action == "getapplication":
            return client.getapplication(**kwargs)
        if action == "getapplications":
            return client.getapplications(**kwargs)
        if action == "getedition":
            return client.getedition(**kwargs)
        if action == "geteditions":
            return client.geteditions(**kwargs)
        if action == "getfeatures":
            return client.getfeatures(**kwargs)
        if action == "create_contract":
            return client.create_contract(**kwargs)
        if action == "get_contract":
            return client.get_contract(**kwargs)
        if action == "update_contract":
            return client.update_contract(**kwargs)
        if action == "delete_contract":
            return client.delete_contract(**kwargs)
        if action == "get_custom_features":
            return client.get_custom_features(**kwargs)
        if action == "create_custom_feature":
            return client.create_custom_feature(**kwargs)
        if action == "get_custom_feature":
            return client.get_custom_feature(**kwargs)
        if action == "update_custom_feature":
            return client.update_custom_feature(**kwargs)
        if action == "delete_custom_feature":
            return client.delete_custom_feature(**kwargs)
        if action == "deletedomain":
            return client.deletedomain(**kwargs)
        if action == "getdomain":
            return client.getdomain(**kwargs)
        if action == "getdomains":
            return client.getdomains(**kwargs)
        if action == "upsertdomain":
            return client.upsertdomain(**kwargs)
        if action == "getidentityproviders":
            return client.getidentityproviders(**kwargs)
        if action == "getworkspaces_2":
            return client.getworkspaces_2(**kwargs)
        if action == "create_event":
            return client.create_event(**kwargs)
        if action == "get_event":
            return client.get_event(**kwargs)
        if action == "update_event":
            return client.update_event(**kwargs)
        if action == "getraw":
            return client.getraw(**kwargs)
        if action == "get_export":
            return client.get_export(**kwargs)
        if action == "process_graph_ql":
            return client.process_graph_ql(**kwargs)
        if action == "get_identity_providers":
            return client.get_identity_providers(**kwargs)
        if action == "create_identity_provider":
            return client.create_identity_provider(**kwargs)
        if action == "get_identity_provider":
            return client.get_identity_provider(**kwargs)
        if action == "update_identity_provider":
            return client.update_identity_provider(**kwargs)
        if action == "delete_identity_provider":
            return client.delete_identity_provider(**kwargs)
        if action == "get_domains":
            return client.get_domains(**kwargs)
        if action == "get_metadata":
            return client.get_metadata(**kwargs)
        if action == "getworkspaces_3":
            return client.getworkspaces_3(**kwargs)
        if action == "activate":
            return client.activate(**kwargs)
        if action == "authenticate":
            return client.authenticate(**kwargs)
        if action == "checkip":
            return client.checkip(**kwargs)
        if action == "invite":
            return client.invite(**kwargs)
        if action == "login":
            return client.login(**kwargs)
        if action == "loginpractitioner":
            return client.loginpractitioner(**kwargs)
        if action == "logout":
            return client.logout(**kwargs)
        if action == "reset_password":
            return client.reset_password(**kwargs)
        if action == "review":
            return client.review(**kwargs)
        if action == "set_password":
            return client.set_password(**kwargs)
        if action == "switchpermissionrole":
            return client.switchpermissionrole(**kwargs)
        if action == "inactive":
            return client.inactive(**kwargs)
        if action == "create_instance":
            return client.create_instance(**kwargs)
        if action == "get_instance":
            return client.get_instance(**kwargs)
        if action == "update_instance":
            return client.update_instance(**kwargs)
        if action == "delete_instance":
            return client.delete_instance(**kwargs)
        if action == "getinstancesbyworkspace":
            return client.getinstancesbyworkspace(**kwargs)
        if action == "getpreferredinstance":
            return client.getpreferredinstance(**kwargs)
        if action == "switchdefaultinstance":
            return client.switchdefaultinstance(**kwargs)
        if action == "list":
            return client.list(**kwargs)
        if action == "create":
            return client.create(**kwargs)
        if action == "invalidate":
            return client.invalidate(**kwargs)
        if action == "getpermissions":
            return client.getpermissions(**kwargs)
        if action == "createpermission":
            return client.createpermission(**kwargs)
        if action == "getpermission":
            return client.getpermission(**kwargs)
        if action == "getsettings_2":
            return client.getsettings_2(**kwargs)
        if action == "getuserrandom":
            return client.getuserrandom(**kwargs)
        if action == "getsettings_3":
            return client.getsettings_3(**kwargs)
        if action == "createsetting":
            return client.createsetting(**kwargs)
        if action == "getsetting":
            return client.getsetting(**kwargs)
        if action == "updatesetting":
            return client.updatesetting(**kwargs)
        if action == "deletesetting":
            return client.deletesetting(**kwargs)
        if action == "getnotificationsettings":
            return client.getnotificationsettings(**kwargs)
        if action == "setworkspacenotificationstatus":
            return client.setworkspacenotificationstatus(**kwargs)
        if action == "gettechnicalusers":
            return client.gettechnicalusers(**kwargs)
        if action == "create_technical_user":
            return client.create_technical_user(**kwargs)
        if action == "get_technical_user":
            return client.get_technical_user(**kwargs)
        if action == "update_technical_user":
            return client.update_technical_user(**kwargs)
        if action == "delete_technical_user":
            return client.delete_technical_user(**kwargs)
        if action == "replace_technical_user_api_token":
            return client.replace_technical_user_api_token(**kwargs)
        if action == "getusers_1":
            return client.getusers_1(**kwargs)
        if action == "createuser":
            return client.createuser(**kwargs)
        if action == "createuserpassword":
            return client.createuserpassword(**kwargs)
        if action == "getevents_6":
            return client.getevents_6(**kwargs)
        if action == "getpermissions_1":
            return client.getpermissions_1(**kwargs)
        if action == "getsettings_4":
            return client.getsettings_4(**kwargs)
        if action == "getuser":
            return client.getuser(**kwargs)
        if action == "updateuser":
            return client.updateuser(**kwargs)
        if action == "getuserrandom_1":
            return client.getuserrandom_1(**kwargs)
        if action == "setpassword_1":
            return client.setpassword_1(**kwargs)
        if action == "create_workspace":
            return client.create_workspace(**kwargs)
        if action == "get_workspace":
            return client.get_workspace(**kwargs)
        if action == "update_workspace":
            return client.update_workspace(**kwargs)
        if action == "delete_workspace":
            return client.delete_workspace(**kwargs)
        if action == "get_feature_bundle":
            return client.get_feature_bundle(**kwargs)
        if action == "get_impersonations":
            return client.get_impersonations(**kwargs)
        if action == "get_permission":
            return client.get_permission(**kwargs)
        if action == "get_permission_stats":
            return client.get_permission_stats(**kwargs)
        if action == "get_permissions":
            return client.get_permissions(**kwargs)
        if action == "get_support_permissions":
            return client.get_support_permissions(**kwargs)
        if action == "get_user_list_export":
            return client.get_user_list_export(**kwargs)
        if action == "getworkspacesforbackup":
            return client.getworkspacesforbackup(**kwargs)
        if action == "permissions_search":
            return client.permissions_search(**kwargs)
        if action == "getuserpiichanges":
            return client.getuserpiichanges(**kwargs)
        if action == "get_user_segment":
            return client.get_user_segment(**kwargs)
        if action == "create_or_update_user_segment":
            return client.create_or_update_user_segment(**kwargs)
        if action == "getworkspacemaintenance":
            return client.getworkspacemaintenance(**kwargs)
        if action == "createworkspacemaintenance":
            return client.createworkspacemaintenance(**kwargs)
        if action == "deleteworkspacemaintenance":
            return client.deleteworkspacemaintenance(**kwargs)
        if action == "get_contracts_1":
            return client.get_contracts_1(**kwargs)
        if action == "get_custom_features_1":
            return client.get_custom_features_1(**kwargs)
        if action == "get_custom_features_2":
            return client.get_custom_features_2(**kwargs)
        if action == "get_domains_1":
            return client.get_domains_1(**kwargs)
        if action == "get_events_1":
            return client.get_events_1(**kwargs)
        if action == "get_events_2":
            return client.get_events_2(**kwargs)
        if action == "get_events_3":
            return client.get_events_3(**kwargs)
        if action == "get_events_4":
            return client.get_events_4(**kwargs)
        if action == "get_events_5":
            return client.get_events_5(**kwargs)
        if action == "get_events_6":
            return client.get_events_6(**kwargs)
        if action == "get_instances_1":
            return client.get_instances_1(**kwargs)
        if action == "get_instances_2":
            return client.get_instances_2(**kwargs)
        if action == "get_settings_1":
            return client.get_settings_1(**kwargs)
        if action == "get_settings_2":
            return client.get_settings_2(**kwargs)
        if action == "get_users_1":
            return client.get_users_1(**kwargs)
        if action == "get_users_2":
            return client.get_users_2(**kwargs)
        if action == "get_workspaces_1":
            return client.get_workspaces_1(**kwargs)
        if action == "get_workspaces_2":
            return client.get_workspaces_2(**kwargs)
        if action == "get_workspaces_3":
            return client.get_workspaces_3(**kwargs)
        if action == "get_custom_feature_1":
            return client.get_custom_feature_1(**kwargs)
        raise ValueError(f"Unknown action: {action}")
