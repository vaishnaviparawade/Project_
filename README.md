# Complete Observability System - Windows Setup Guide

## Prerequisites
- Install Docker Desktop for Windows with WSL 2 backend: https://docs.docker.com/desktop/install/windows-install/
- Ensure Docker is set to use Linux containers (Right-click Docker icon > Switch to Linux containers)
- Optional: Install WSL 2 and Ubuntu from Microsoft Store for Linux terminal (recommended)

## Steps to Run

1. Open PowerShell or Command Prompt in the project directory (`C:\observability_system_windows` or your path)

2. Build and start containers:
   ```
   docker-compose up --build
   ```

3. Wait for services to start:
   - Prometheus UI: http://localhost:9090
   - Grafana UI: http://localhost:3000 (default login: admin/admin)
   - Jaeger UI: http://localhost:16686
   - Loki API: http://localhost:3100
   - Python app: http://localhost:5000

4. Explore the dashboards on Grafana (prometheus metrics, Loki logs, Jaeger traces)

## Notes
- Logs from the Python app are sent to Loki via console logs
- Metrics are scraped by Prometheus
- Jaeger collects traces for HTTP routes

Happy Observing!