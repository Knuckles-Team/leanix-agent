from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_mtm_client,
)

_MTM_ACTIONS = frozenset(
    {
        "getaiaccess",
        "gettaskbyid",
        "createworkspacelabel",
        "deleteworkspacelabel",
        "getall",
        "getlabelsbyworkspace",
        "getlabelsbyworkspaces",
        "token",
        "get_data_breach_contact",
        "add_data_breach_contact",
        "delete_data_breach_contact",
        "get_accounts",
        "create_account",
        "get_account",
        "update_account",
        "delete_account",
        "get_contracts",
        "get_events",
        "get_instances",
        "get_settings",
        "get_users",
        "get_workspaces",
        "getapitokens",
        "createapitoken",
        "getapitoken",
        "updateapitoken",
        "deleteapitoken",
        "getfeature",
        "accessfeature",
        "getapplication",
        "getapplications",
        "getedition",
        "geteditions",
        "getfeatures",
        "create_contract",
        "get_contract",
        "update_contract",
        "delete_contract",
        "get_custom_features",
        "create_custom_feature",
        "get_custom_feature",
        "update_custom_feature",
        "delete_custom_feature",
        "deletedomain",
        "getdomain",
        "getdomains",
        "upsertdomain",
        "getidentityproviders",
        "getworkspaces_2",
        "create_event",
        "get_event",
        "update_event",
        "getraw",
        "get_export",
        "process_graph_ql",
        "get_identity_providers",
        "create_identity_provider",
        "get_identity_provider",
        "update_identity_provider",
        "delete_identity_provider",
        "get_domains",
        "get_metadata",
        "getworkspaces_3",
        "activate",
        "authenticate",
        "checkip",
        "invite",
        "login",
        "loginpractitioner",
        "logout",
        "reset_password",
        "review",
        "set_password",
        "switchpermissionrole",
        "inactive",
        "create_instance",
        "get_instance",
        "update_instance",
        "delete_instance",
        "getinstancesbyworkspace",
        "getpreferredinstance",
        "switchdefaultinstance",
        "list",
        "create",
        "invalidate",
        "getpermissions",
        "createpermission",
        "getpermission",
        "getsettings_2",
        "getuserrandom",
        "getsettings_3",
        "createsetting",
        "getsetting",
        "updatesetting",
        "deletesetting",
        "getnotificationsettings",
        "setworkspacenotificationstatus",
        "gettechnicalusers",
        "create_technical_user",
        "get_technical_user",
        "update_technical_user",
        "delete_technical_user",
        "replace_technical_user_api_token",
        "getusers_1",
        "createuser",
        "createuserpassword",
        "getevents_6",
        "getpermissions_1",
        "getsettings_4",
        "getuser",
        "updateuser",
        "getuserrandom_1",
        "setpassword_1",
        "create_workspace",
        "get_workspace",
        "update_workspace",
        "delete_workspace",
        "get_feature_bundle",
        "get_impersonations",
        "get_permission",
        "get_permission_stats",
        "get_permissions",
        "get_support_permissions",
        "get_user_list_export",
        "getworkspacesforbackup",
        "permissions_search",
        "getuserpiichanges",
        "get_user_segment",
        "create_or_update_user_segment",
        "getworkspacemaintenance",
        "createworkspacemaintenance",
        "deleteworkspacemaintenance",
        "get_contracts_1",
        "get_custom_features_1",
        "get_custom_features_2",
        "get_domains_1",
        "get_events_1",
        "get_events_2",
        "get_events_3",
        "get_events_4",
        "get_events_5",
        "get_events_6",
        "get_instances_1",
        "get_instances_2",
        "get_settings_1",
        "get_settings_2",
        "get_users_1",
        "get_users_2",
        "get_workspaces_1",
        "get_workspaces_2",
        "get_workspaces_3",
        "get_custom_feature_1",
    }
)


def _dispatch_mtm_action(client, action: str, kwargs: dict):
    """Call client.<action>(**kwargs) for a whitelisted action name.

    Behavior-preserving replacement for the original 152-branch
    if/elif chain: action name always equals the target client method
    name in this generated module, so a single whitelist-gated
    getattr() call is exactly equivalent to the original dispatch.
    """
    if action not in _MTM_ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    return getattr(client, action)(**kwargs)


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
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return _dispatch_mtm_action(client, action, kwargs)
