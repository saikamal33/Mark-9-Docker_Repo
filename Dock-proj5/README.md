# 📊 Mini Monitor – Dockerized Full-Stack Metrics Dashboard

## A full-stack Docker project featuring:

🖥️ Frontend (Node.js + Express)

🐍 Backend API (Python Flask)

📈 Prometheus for metrics scraping

📊 Grafana for dashboards

🐳 All orchestrated using Docker Compose

🚀 Getting Started

Docker & Docker Compose installed
~~~
git clone https://github.com/yourusername/minimonitor.git
cd minimonitor
docker-compose up --build
~~~

## 🔗 URLs
Service	URL
~~~
Frontend	  http://localhost:3000
Backend API	http://localhost:5000/metrics
Prometheus	http://localhost:9090
Grafana	    http://localhost:3001
~~~

## 🔐 Grafana Login
### Username: admin

### Password: admin

## Add Prometheus as a Data Source:

Go to Grafana → Settings → Data Sources

Add new → Prometheus

URL: http://prometheus:9090

## 📊 Metrics Preview
The backend emits mock metrics like:

~~~
cpu_usage 67
memory_usage 800
~~~
You can build dashboards using these in Grafana.

## 📦 Docker Volumes
Data is persisted using Docker volumes:

~~~
volumes:
  prometheus_data:  # Persists Prometheus TSDB
  grafana_data:     # Persists Grafana dashboards/settings
~~~

## 🧰 Tech Stack
Node.js

Flask (Python 3.11)

Prometheus

Grafana OSS

Docker & Docker Compose

## 📝 To Do (Next Steps)
Add Grafana dashboard export

Add Prometheus alerting rules

Deploy to Kubernetes

GitHub Actions CI/CD pipeline
