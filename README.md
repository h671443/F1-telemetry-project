# F1-telemetry-project
Project Aimed to gather F1 telemetry data

GRAFANA

install GRAFANA ALLOY:
Option 1: Grafana Alloy (recommended)
Alloy is Grafana's telemetry collector that can scrape and forward metrics.

    Install Alloy on your machine — get it at grafana.com/docs/alloy
    Configure it to scrape your Prometheus targets and remote_write to Grafana Cloud
    Your Cloud credentials (endpoint + API key) are in Connections → Data sources → Prometheus
    - https://grafana.com/docs/alloy/latest/set-up/install/docker/
    - https://grafana.com/docs/alloy/latest/set-up/install/linux/
    
