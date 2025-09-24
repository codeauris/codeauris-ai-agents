# Stage 1: build client
FROM node:18-bullseye AS client-build
WORKDIR /app/client

COPY client/package.json ./
RUN npm install --legacy-peer-deps

COPY client/ ./
RUN npm run build

# Stage 2: server
FROM node:18-bullseye
WORKDIR /app/server

COPY server/package.json ./
RUN npm install --production

# Copy server source and .env
COPY server/ ./

# Copy built frontend
COPY --from=client-build /app/client/dist ../client/dist

EXPOSE 3000
CMD ["node", "index.js"]
