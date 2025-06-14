# --- Stage 1: Build ---
FROM node:18 AS builder
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# --- Stage 2: Runtime ---
FROM node:18-slim
WORKDIR /app

# Copy only necessary files from build stage
COPY --from=builder /app ./

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]

