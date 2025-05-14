# Metrics Tracking/Visualization Practice

This project mirrors a basic production monitoring setup using Prometheus + Grafana. It includes:

- CPU, memory, and disk dashboards using node_exporter
- Custom recording rules (e.g. `instance:cpu_utilization:percent`)
- A fake GPU metrics exporter I wrote in Python
- Real-time alert examples (high CPU usage)

## Run the stack

```bash
docker compose up -d
```

Then visit:

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (admin/admin)

## Dashboards

- grafana/dashboards/system-metrics.json – CPU, memory, disk, and network panels


## Recording Rules

Defined in `prometheus/node.rules.yml`, covering:

- CPU utilization (instance:cpu_utilization:percent)
- Memory available percent
- Disk usage (bytes and percent)

## Alerts

I created an example alert in `prometheus/alerts`.yml.

## Fake GPU Exporter

To run:

    python gpu_fake_exporter.py

Exposes:

- gpu_temp_c – simulated temperature (gauge)
Prometheus scrapes from http://gpu-exporter:8000/metrics



