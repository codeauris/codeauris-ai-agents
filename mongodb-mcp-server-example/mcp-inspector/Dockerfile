# Use Node.js 22 as specified in the requirements
FROM node:22-alpine

# Install curl, python3, and other utilities for health checks and MCP server support
RUN apk add --no-cache curl python3 py3-pip bash git

# Set working directory
WORKDIR /app

# Create a non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S inspector -u 1001

# Install global MCP Inspector package
RUN npm install -g @modelcontextprotocol/inspector

# Set environment variables with defaults
ENV CLIENT_PORT=6274
ENV SERVER_PORT=6277
ENV HOST=0.0.0.0
ENV NODE_ENV=production
ENV MCP_PROXY_AUTH_TOKEN=""

# Make sure python is available as 'python' (not just 'python3')
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Install common Python packages for MCP servers
RUN pip3 install --no-cache-dir --break-system-packages \
    mcp \
    pymongo \
    requests \
    pydantic

# Expose the default ports
EXPOSE 6274 6277

# Create directory for configurations and MCP servers
RUN mkdir -p /app/config /app/mcp-servers && \
    chown -R inspector:nodejs /app

# Switch to non-root user
USER inspector

# Health check to ensure the service is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:${CLIENT_PORT} || exit 1

# Default command to run the MCP Inspector
# CMD ["npx", "@modelcontextprotocol/inspector"]
CMD ["npx", "@modelcontextprotocol/inspector", "python", "mcp-mongodb-server"]


# # Use Node.js 22.7.5 as specified in the requirements
# FROM node:22.7.5-alpine
#
# # Install curl, python3, and other utilities for health checks and MCP server support
# RUN apk add --no-cache curl python3 py3-pip bash git
#
# # Set working directory
# WORKDIR /app
#
# # Create a non-root user for security
# RUN addgroup -g 1001 -S nodejs && \
#     adduser -S inspector -u 1001
#
# # Option 1: Install global MCP Inspector package (simpler approach)
# RUN npm install -g @modelcontextprotocol/inspector
#
# # Option 2: Build from source (uncomment if you prefer this approach)
# # COPY package*.json ./
# # RUN npm ci --only=production
# # COPY . .
# # RUN npm run build
#
# # Set environment variables with defaults
# ENV CLIENT_PORT=6274
# ENV SERVER_PORT=6277
# ENV HOST=0.0.0.0
# ENV NODE_ENV=production
# ENV MCP_PROXY_AUTH_TOKEN=""
#
# # Make sure python is available as 'python' (not just 'python3')
# RUN ln -sf /usr/bin/python3 /usr/bin/python
#
# # Install common Python packages for MCP servers
# RUN pip3 install --no-cache-dir --break-system-packages \
#     mcp \
#     pymongo \
#     requests \
#     pydantic
#
# # Expose the default ports
# EXPOSE 6274 6277
#
# # Create directory for configurations and MCP servers
# RUN mkdir -p /app/config /app/mcp-servers && \
#     chown -R inspector:nodejs /app
#
# # Switch to non-root user
# USER inspector
#
# # Health check to ensure the service is running
# HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#   CMD curl -f http://localhost:${CLIENT_PORT} || exit 1
#
# # Default command to run the MCP Inspector
# # You can override this with docker run commands or in docker-compose
# CMD ["npx", "@modelcontextprotocol/inspector"]
#
# # Alternative commands you might want to use:
# # CMD ["npx", "@modelcontextprotocol/inspector", "--cli"]  # For CLI mode
# # CMD ["npx", "@modelcontextprotocol/inspector", "python", "your-mcp-server.py"]  # To test specific server