# Use Node 22 Alpine
FROM node:22-alpine

# Set build argument with default value
ARG VERSION=latest

# Install build tools for native modules and curl
RUN apk add --no-cache python3 make g++ bash git curl

# Upgrade npm to latest as root
RUN npm install -g npm@latest

# Install MongoDB MCP Server globally
RUN npm install -g mongodb-mcp-server@${VERSION}

# Create non-root user after global installations
RUN addgroup -S mcp && adduser -S mcp -G mcp

# Create app directory and change ownership
RUN mkdir -p /home/mcp && chown -R mcp:mcp /home/mcp

# Switch to non-root user
USER mcp
WORKDIR /home/mcp

# Set environment variables
ENV MDB_MCP_LOGGERS=stderr,mcp
ENV NODE_ENV=production

# Entry point
# ENTRYPOINT ["mongodb-mcp-server"]
# Entry point with HTTP server mode
# Use SSE (Server-Sent Events) transport for HTTP connectivity
# ENTRYPOINT ["mongodb-mcp-server", "--transport", "sse", "--port", "3000"]
# Entry point with HTTP transport
ENTRYPOINT ["mongodb-mcp-server", "--transport", "http", "--httpHost", "0.0.0.0", "--httpPort", "3000", "--readOnly"]

# Labels
LABEL maintainer="MongoDB Inc <info@mongodb.com>"
LABEL description="MongoDB MCP Server"
LABEL version=${VERSION}