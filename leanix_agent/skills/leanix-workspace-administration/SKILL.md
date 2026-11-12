---
name: leanix-workspace-administration
skill_type: skill
description: >-
  Administer the LeanIX tenant through the multi-tenant manager: accounts, workspaces,
  users, contracts, editions, features and custom features, domains and identity
  providers, API tokens, labels, events, settings, and data-breach contacts. Use when the
  agent must manage who and what a workspace contains. Do NOT use for inventory content.
license: MIT
tags: [leanix, admin, workspaces, users, tokens, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# LeanIX Workspace Administration

The multi-tenant manager owns the tenant level: accounts and workspaces, the contracts and editions that unlock features, the users and identity providers that sign in, and the API tokens that connectors use.

## When to use
- Read and change accounts, workspaces, contracts, editions and features.
- Manage domains, identity providers and users.
- Create, read, update and delete API tokens.
- Manage labels and data-breach contacts; read events and tasks.

## When NOT to use
- Any inventory content: use the other leanix skills.

## Workflow
1. Read the account or workspace first.
2. Apply one change and read it back.
3. Report ids and the new state.

## Safety
- Never print API tokens or token responses.
- Deleting an account, contract, domain or token can lock people out; ask first.

## Tools (152)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Mtm

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_mtm_checkip` | POST | Call POST /idm/check_ip |
| `leanix_leanix_mtm_get_account` | GET | get_account |
| `leanix_leanix_mtm_get_accounts` | GET | get_accounts |
| `leanix_leanix_mtm_get_contract` | GET | get_contract |
| `leanix_leanix_mtm_get_contracts` | GET | get_contracts |
| `leanix_leanix_mtm_get_contracts_1` | GET | get_contracts_1_1 |
| `leanix_leanix_mtm_get_custom_feature` | GET | get_custom_feature |
| `leanix_leanix_mtm_get_custom_feature_1` | GET | get_custom_feature_1_1 |
| `leanix_leanix_mtm_get_custom_features` | GET | get_custom_features |
| `leanix_leanix_mtm_get_custom_features_1` | GET | get_custom_features_1_1 |
| `leanix_leanix_mtm_get_custom_features_2` | GET | get_custom_features_2_2 |
| `leanix_leanix_mtm_get_data_breach_contact` | GET | get_data_breach_contact |
| `leanix_leanix_mtm_get_domains` | GET | get_domains |
| `leanix_leanix_mtm_get_domains_1` | GET | get_domains_1_1 |
| `leanix_leanix_mtm_get_event` | GET | get_event |
| `leanix_leanix_mtm_get_events` | GET | get_events |
| `leanix_leanix_mtm_get_events_1` | GET | get_events_1_1 |
| `leanix_leanix_mtm_get_events_2` | GET | get_events_2_2 |
| `leanix_leanix_mtm_get_events_3` | GET | get_events_3_3 |
| `leanix_leanix_mtm_get_events_4` | GET | get_events_4_4 |
| `leanix_leanix_mtm_get_events_5` | GET | get_events_5_5 |
| `leanix_leanix_mtm_get_events_6` | GET | get_events_6_6 |
| `leanix_leanix_mtm_get_export` | GET | get_export |
| `leanix_leanix_mtm_get_feature_bundle` | GET | get_feature_bundle |
| `leanix_leanix_mtm_get_identity_provider` | GET | get_identity_provider |
| `leanix_leanix_mtm_get_identity_providers` | GET | get_identity_providers |
| `leanix_leanix_mtm_get_impersonations` | GET | get_impersonations |
| `leanix_leanix_mtm_get_instance` | GET | get_instance |
| `leanix_leanix_mtm_get_instances` | GET | get_instances |
| `leanix_leanix_mtm_get_instances_1` | GET | get_instances_1_1 |
| `leanix_leanix_mtm_get_instances_2` | GET | get_instances_2_2 |
| `leanix_leanix_mtm_get_metadata` | GET | get_metadata |
| `leanix_leanix_mtm_get_permission` | GET | get_permission |
| `leanix_leanix_mtm_get_permission_stats` | GET | get_permission_stats |
| `leanix_leanix_mtm_get_permissions` | GET | get_permissions |
| `leanix_leanix_mtm_get_settings` | GET | get_settings |
| `leanix_leanix_mtm_get_settings_1` | GET | get_settings_1_1 |
| `leanix_leanix_mtm_get_settings_2` | GET | get_settings_2_2 |
| `leanix_leanix_mtm_get_support_permissions` | GET | get_support_permissions |
| `leanix_leanix_mtm_get_technical_user` | GET | get_technical_user |
| `leanix_leanix_mtm_get_user_list_export` | GET | get_user_list_export |
| `leanix_leanix_mtm_get_user_segment` | GET | get_user_segment |
| `leanix_leanix_mtm_get_users` | GET | get_users |
| `leanix_leanix_mtm_get_users_1` | GET | get_users_1_1 |
| `leanix_leanix_mtm_get_users_2` | GET | get_users_2_2 |
| `leanix_leanix_mtm_get_workspace` | GET | get_workspace |
| `leanix_leanix_mtm_get_workspaces` | GET | get_workspaces |
| `leanix_leanix_mtm_get_workspaces_1` | GET | get_workspaces_1_1 |
| `leanix_leanix_mtm_get_workspaces_2` | GET | get_workspaces_2_2 |
| `leanix_leanix_mtm_get_workspaces_3` | GET | get_workspaces_3_3 |
| `leanix_leanix_mtm_getaiaccess` | GET | Returns AI feature access summary for the given workspace. Restricted to internal use only. |
| `leanix_leanix_mtm_getall` | GET | Get all labels |
| `leanix_leanix_mtm_getapitoken` | GET | Retrieves a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User'... |
| `leanix_leanix_mtm_getapitokens` | GET | Retrieves all matching personal API Tokens.  Personal API Tokens are deprecated. Please use the 'Technical... |
| `leanix_leanix_mtm_getapplication` | GET | Get Application |
| `leanix_leanix_mtm_getapplications` | GET | Get Applications |
| `leanix_leanix_mtm_getdomain` | GET | Retrieves a specific domain. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getdomains` | GET | Retrieves all domains. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getedition` | GET | Get Edition |
| `leanix_leanix_mtm_geteditions` | GET | Get Editions |
| `leanix_leanix_mtm_getevents_6` | GET | Retrieves all events for an user (date must be ISO 8601 formatted) |
| `leanix_leanix_mtm_getfeature` | GET | Get Feature |
| `leanix_leanix_mtm_getfeatures` | GET | Get Features |
| `leanix_leanix_mtm_getidentityproviders` | GET | Retrieves all SIGNIN-based identity providers for a domain. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getinstancesbyworkspace` | POST | Call POST /instances/find_by_workspace_ids |
| `leanix_leanix_mtm_getlabelsbyworkspace` | GET | Get all currently existing labels on a workspace. |
| `leanix_leanix_mtm_getlabelsbyworkspaces` | GET | Get all currently existing labels on a list of workspaces. |
| `leanix_leanix_mtm_getnotificationsettings` | GET | Endpoint to get_user_segment all settings related to notifications, internal usage only. |
| `leanix_leanix_mtm_getpermission` | GET | Retrieves one permission for requested permission id. |
| `leanix_leanix_mtm_getpermissions` | GET | Endpoint to list the user permissions. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getpermissions_1` | GET | Endpoint to list the user permissions. |
| `leanix_leanix_mtm_getpreferredinstance` | GET | Call GET /instances/preferred |
| `leanix_leanix_mtm_getraw` | GET | Call GET /events/raw |
| `leanix_leanix_mtm_getsetting` | GET | Endpoint to get_user_segment a setting. |
| `leanix_leanix_mtm_getsettings_2` | GET | Endpoint to list the permission specific settings. |
| `leanix_leanix_mtm_getsettings_3` | GET | Retrieves settings |
| `leanix_leanix_mtm_getsettings_4` | GET | Endpoint to list the user specific settings. |
| `leanix_leanix_mtm_gettaskbyid` | GET | Get asynchronous task status by ID |
| `leanix_leanix_mtm_gettechnicalusers` | GET | Technical users |
| `leanix_leanix_mtm_getuser` | GET | Returns user data. |
| `leanix_leanix_mtm_getuserpiichanges` | POST | Get user PII changes |
| `leanix_leanix_mtm_getuserrandom` | GET | Call GET /permissions/sample |
| `leanix_leanix_mtm_getuserrandom_1` | GET | Call GET /users/sample |
| `leanix_leanix_mtm_getusers_1` | GET | List or search all users. |
| `leanix_leanix_mtm_getworkspacemaintenance` | GET | Get maintenance mode |
| `leanix_leanix_mtm_getworkspaces_2` | GET | Retrieves all workspaces for a domain. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getworkspaces_3` | GET | Retrieves all workspaces connected to an identity provider. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_getworkspacesforbackup` | GET | Call GET /workspaces/backup_workspaces |
| `leanix_leanix_mtm_inactive` | GET | inactive |
| `leanix_leanix_mtm_list` | GET | List all long-lived bearer tokens. |
| `leanix_leanix_mtm_accessfeature` | POST | Access Feature |
| `leanix_leanix_mtm_activate` | POST | activate |
| `leanix_leanix_mtm_add_data_breach_contact` | POST | add_data_breach_contact |
| `leanix_leanix_mtm_authenticate` | POST | authenticate |
| `leanix_leanix_mtm_create` | POST | Create a new long-lived bearer token. |
| `leanix_leanix_mtm_create_account` | POST | create_account |
| `leanix_leanix_mtm_create_contract` | POST | create_contract |
| `leanix_leanix_mtm_create_custom_feature` | POST | create_custom_feature |
| `leanix_leanix_mtm_create_event` | POST | create_event |
| `leanix_leanix_mtm_create_identity_provider` | POST | create_identity_provider |
| `leanix_leanix_mtm_create_instance` | POST | create_instance |
| `leanix_leanix_mtm_create_technical_user` | POST | create_technical_user |
| `leanix_leanix_mtm_create_workspace` | POST | create_workspace |
| `leanix_leanix_mtm_createapitoken` | POST | Creates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User'... |
| `leanix_leanix_mtm_createpermission` | POST | Set a user permission for a workspace. If the related user object contains changed data, the data is... |
| `leanix_leanix_mtm_createsetting` | POST | Endpoint to set a setting. |
| `leanix_leanix_mtm_createuser` | POST | Create a user |
| `leanix_leanix_mtm_createuserpassword` | POST | Create a password for a user. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_createworkspacelabel` | POST | Adds a label to a workspace. |
| `leanix_leanix_mtm_createworkspacemaintenance` | POST | Create a new maintenance |
| `leanix_leanix_mtm_invalidate` | POST | Invalidate an existing long-lived bearer token. |
| `leanix_leanix_mtm_invite` | POST | invite |
| `leanix_leanix_mtm_login` | POST | login |
| `leanix_leanix_mtm_loginpractitioner` | POST | Call POST /idm/practitioner |
| `leanix_leanix_mtm_logout` | POST | logout |
| `leanix_leanix_mtm_permissions_search` | POST | permissions_search |
| `leanix_leanix_mtm_process_graph_ql` | POST | process_graph_ql |
| `leanix_leanix_mtm_reset_password` | POST | reset_password |
| `leanix_leanix_mtm_review` | POST | review |
| `leanix_leanix_mtm_set_password` | POST | set_password |
| `leanix_leanix_mtm_setpassword_1` | POST | Endpoint to finish the reset the password process, can only be accessed by systems. |
| `leanix_leanix_mtm_setworkspacenotificationstatus` | POST | Endpoint to enable/disable notifications. |
| `leanix_leanix_mtm_switchdefaultinstance` | POST | Call POST /instances/{id}/set_to_default |
| `leanix_leanix_mtm_switchpermissionrole` | POST | Call POST /idm/switch_permission_role |
| `leanix_leanix_mtm_token` | POST | Creates an access token. |
| `leanix_leanix_mtm_create_or_update_user_segment` | PUT | create_or_update_user_segment |
| `leanix_leanix_mtm_replace_technical_user_api_token` | PUT | replace_technical_user_api_token |
| `leanix_leanix_mtm_update_account` | PUT | update_account |
| `leanix_leanix_mtm_update_contract` | PUT | update_contract |
| `leanix_leanix_mtm_update_custom_feature` | PUT | update_custom_feature |
| `leanix_leanix_mtm_update_event` | PUT | update_event |
| `leanix_leanix_mtm_update_identity_provider` | PUT | update_identity_provider |
| `leanix_leanix_mtm_update_instance` | PUT | update_instance |
| `leanix_leanix_mtm_update_technical_user` | PUT | update_technical_user |
| `leanix_leanix_mtm_update_workspace` | PUT | update_workspace |
| `leanix_leanix_mtm_updateapitoken` | PUT | Updates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User'... |
| `leanix_leanix_mtm_updatesetting` | PUT | Update a setting |
| `leanix_leanix_mtm_updateuser` | PUT | Update a user |
| `leanix_leanix_mtm_upsertdomain` | PUT | Creates or updates a domain and the respective CNAME. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_delete_account` | DELETE | delete_account |
| `leanix_leanix_mtm_delete_contract` | DELETE | delete_contract |
| `leanix_leanix_mtm_delete_custom_feature` | DELETE | delete_custom_feature |
| `leanix_leanix_mtm_delete_data_breach_contact` | DELETE | delete_data_breach_contact |
| `leanix_leanix_mtm_delete_identity_provider` | DELETE | delete_identity_provider |
| `leanix_leanix_mtm_delete_instance` | DELETE | delete_instance |
| `leanix_leanix_mtm_delete_technical_user` | DELETE | delete_technical_user |
| `leanix_leanix_mtm_delete_workspace` | DELETE | delete_workspace |
| `leanix_leanix_mtm_deleteapitoken` | DELETE | Deletes a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User'... |
| `leanix_leanix_mtm_deletedomain` | DELETE | Deletes a domain and the respective CNAME. Restricted to LeanIX internal use only. |
| `leanix_leanix_mtm_deletesetting` | DELETE | Delete a setting |
| `leanix_leanix_mtm_deleteworkspacelabel` | DELETE | Removes a label from a workspace. |
| `leanix_leanix_mtm_deleteworkspacemaintenance` | DELETE | Delete maintenance mode |
