#  MongoDB MCP Server Example | CodeAuris
A complete Docker-based implementation of the MongoDB Model Context Protocol (MCP) server with integrated development and testing tools.

**Links:**
- [Video link]()

## 🏗️ Project Overview

This project provides a comprehensive setup for running and testing MongoDB MCP Server using Docker containers. It includes MongoDB database, MCP server, inspector tools, and utility services for complete development workflow.

**Developed by:** CodeAuris  
**Project:** `mongodb-mcp-server-example`

## ✨ Features

- **MongoDB MCP Server**: Production-ready MongoDB Model Context Protocol server
- **MCP Inspector**: Visual testing and debugging interface for MCP servers
- **Database Management**: Automated MongoDB setup with data restoration
- **Development Tools**: MongoDB shell access and debugging utilities
- **Health Monitoring**: Comprehensive health checks for all services
- **Network Isolation**: Separate networks for security and service isolation
- **Data Persistence**: Persistent MongoDB data storage
- **Hot Reload**: Development-friendly configuration for rapid iteration

## 🏛️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     MCP Inspector                           │
│                  (Port 6274/6277)                           │
│              Visual Testing Interface                       │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ HTTP Connection
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                MCP MongoDB Server                           │
│                   (Port 3000)                               │
│              Model Context Protocol                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ MongoDB Connection
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                   MongoDB                                   │
│                 (Port 27017)                                │
│              Database Storage                               │
└─────────────────────────────────────────────────────────────┘
```

## 📋 Prerequisites

### System Requirements
- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 3.8 or higher
- **Operating System**: Linux, macOS, or Windows with WSL2
- **RAM**: Minimum 4GB, Recommended 8GB
- **Disk Space**: At least 2GB free space

### Network Requirements
- Ports 27017, 3000, 6274, 6277 should be available
- Internet connection for pulling Docker images

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/CodeAuris/mongodb-mcp-server-example.git
cd mongodb-mcp-server-example
```

### 2. Start Services
```bash
# Start all services
docker-compose up -d

# Or start with logs
docker-compose up

# Specific services only
docker-compose up mongodb mcp-mongodb-server
```

### 3. Verify Installation
```bash
# Check all services are running
docker-compose ps

# Test MongoDB connection
curl http://localhost:27017

# Access MCP Inspector
open http://localhost:6274
```

### 4. Access Services

**MCP Inspector Web UI:**
```bash
# Open in browser
http://localhost:6274

# Connect to Database
mongodb://mongoadmin:secret@mongodb:27017/mcpdb_data?authSource=admin
```

**MongoDB Direct Access:**
```bash
# Using MongoDB shell
docker-compose --profile tools up -d mongosh
docker-compose exec mongosh mongosh
```

**MCP Server API:**
```bash
# Health check
curl http://localhost:3000/health

# API endpoints
curl http://localhost:3000/api/collections
```

### 5. Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (⚠️ Data loss!)
docker-compose down -v
```

### 6. Monitor Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f mcp-mongodb-server

# Last 100 lines
docker-compose logs --tail=100 mongodb
```

## 📁 Project Structure

```
mongodb-mcp-server-example/
├── docker-compose.yml          # Main orchestration file
├── README.md                   # This file
│
├── mcp-server/                 # MCP Server configuration
│   ├── Dockerfile             # MCP Server container build
│
├── mcp-inspector/             # MCP Inspector configuration  
│   ├── Dockerfile            # Inspector container build
│
└── mongodata/                # MongoDB dump/restore data
    ├── airline.bson      # Your database dumps
    ├── airline.metadata.json
    └── ...                   # Additional collections
```

## 🔧 Services Overview

### 1. MongoDB (Primary Database)
- **Container**: `mongodb`
- **Image**: `mongo:latest`
- **Port**: `27017`
- **Purpose**: Primary data storage
- **Credentials**: 
  - Username: `mongoadmin`
  - Password: `secret`
  - Database: `mcpdb_data`

**Health Check**: Pings database every 30 seconds

### 2. MongoDB Restore Service
- **Container**: `mongorestore`  
- **Image**: `mongo:latest`
- **Purpose**: Automatically restores data from dump files
- **Run Mode**: One-time execution, then stops
- **Data Path**: Maps local `mongodata/` to container `/dump`

### 3. MongoDB Shell (mongosh)
- **Container**: `mongosh`
- **Image**: `mongo:latest` 
- **Purpose**: Interactive database shell access
- **Activation**: Only starts with `--profile tools`
- **Usage**: `docker-compose --profile tools up mongosh`

### 4. MCP MongoDB Server
- **Container**: `mcp-mongodb-server`
- **Build**: Custom build from `./mcp-server/`
- **Port**: `3000`
- **Purpose**: Model Context Protocol server for MongoDB operations
- **Features**:
  - RESTful API for MCP operations
  - Health monitoring
  - Debug logging
  - Production-ready configuration

### 5. MCP Inspector
- **Container**: `modelcontextinspector`
- **Build**: Custom build from `./mcp-inspector/`
- **Ports**: `6274` (UI), `6277` (Proxy)
- **Purpose**: Visual testing and debugging interface
- **Features**:
  - Web-based UI for testing MCP servers
  - Real-time request/response monitoring
  - Authentication disabled for development
  - Comprehensive timeout configuration

**Made by CodeAuris**
