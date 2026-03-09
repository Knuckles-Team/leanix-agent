# LeanIX Agent - A2A | AG-UI | MCP

![PyPI - Version](https://img.shields.io/pypi/v/leanix-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/leanix-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/leanix-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/leanix-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/leanix-agent)
![PyPI - License](https://img.shields.io/pypi/l/leanix-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/leanix-agent)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/leanix-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/leanix-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/leanix-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/leanix-agent)

![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/leanix-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/leanix-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/leanix-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/leanix-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/leanix-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/leanix-agent)

*Version: 0.1.11*

## Overview

**LeanIX Agent MCP Server + A2A Agent**

Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL.

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `LEANIX_WORKSPACE`: The URL of the target service.
*   `LEANIX_API_TOKEN`: The API token or access token.

#### Run in stdio mode (default):
```bash
export LEANIX_WORKSPACE="http://localhost:8080"
export LEANIX_API_TOKEN="your_token"
leanix-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export LEANIX_WORKSPACE="http://localhost:8080"
export LEANIX_API_TOKEN="your_token"
leanix-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export LEANIX_WORKSPACE="http://localhost:8080"
export LEANIX_API_TOKEN="your_token"
leanix-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Docker

### Build

```bash
docker build -t leanix-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name leanix-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e LEANIX_WORKSPACE="http://your-service:8080" \
  -e LEANIX_API_TOKEN="your_token" \
  knucklessg1/leanix-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  leanix-agent:
    image: knucklessg1/leanix-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - LEANIX_WORKSPACE=http://your-service:8080
      - LEANIX_API_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "leanix": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "leanix-agent",
        "leanix-mcp"
      ],
      "env": {
        "LEANIX_WORKSPACE": "http://your-service:8080",
        "LEANIX_API_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install leanix-agent
```
```bash
uv pip install leanix-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)
