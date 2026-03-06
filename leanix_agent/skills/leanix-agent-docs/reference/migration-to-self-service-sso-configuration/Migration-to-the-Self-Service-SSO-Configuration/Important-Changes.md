##  Important Changes
Each workspace now requires its own SSO configuration. The legacy setup with one IdP for all workspaces no longer works.
The new setup is workspace-specific. Each workspace must have its own IdP connection with a dedicated Entity ID and Reply (ACS) URL.
In your IdP, you can either connect to separate applications or, if possible, use a single application.
