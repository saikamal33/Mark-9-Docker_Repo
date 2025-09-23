FROM node:18-slim

# Install dependencies and tools
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unzip \
    openjdk-17-jre \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Install Sonar Scanner manually
RUN curl -sSLo /tmp/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip \
    && unzip /tmp/sonar-scanner.zip -d /opt \
    && rm /tmp/sonar-scanner.zip \
    && ln -s /opt/sonar-scanner-*/bin/sonar-scanner /usr/local/bin/sonar-scanner \
    && groupadd -for -g 999 docker && usermod -aG docker node


WORKDIR /app

