# ResilienceOps: A Mini Site Reliability Engineering Toolkit

A simulated environment to demonstrate the principles of Site Reliability Engineering (SRE), built using Python, Docker, Kubernetes, Prometheus, and Grafana. This project reflects core SRE responsibilities like observability, reliability, automation, and proactive incident response.

## 📌 Project Goals

- Build a containerized microservice with intentional failure points
- Implement monitoring and alerting with Prometheus and Grafana
- Design auto-healing logic via Kubernetes health checks
- Simulate real-world outages and load testing
- Visualize key metrics (latency, error rate, SLO compliance)

## 🧰 Technologies Used

| Category        | Tools                                          |
|----------------|------------------------------------------------|
| Language        | Python (Flask), Bash                          |
| Monitoring      | Prometheus, Grafana, Alertmanager             |
| Logging         | Fluent Bit, Loki (optional)                   |
| Infrastructure  | Docker, Kubernetes, Helm                      |
| Chaos Testing   | Custom Bash Scripts, Chaos Mesh (optional)    |
| CI/CD           | GitHub Actions, AWS CodePipeline (optional)   |
| Load Testing    | Locust or k6                                   |

## 🚀 Quick Start

### Prerequisites

- Docker Desktop
- kubectl + Minikube or Docker Desktop with Kubernetes
- Helm (for managing Prometheus stack)

### Clone the Project

```bash
git clone https://github.com/yourusername/resilienceops.git
cd resilienceops
```

### Deploy to Kubernetes (Local Cluster)

```bash
# Start Kubernetes cluster
minikube start

# Deploy Prometheus + Grafana stack
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack

# Deploy the app
kubectl apply -f k8s/deployment.yaml
```

## 💥 Simulate a Failure

```bash
# Simulate CPU spike
bash chaos/cpu_spike.sh

# Kill a pod randomly
kubectl delete pod -l app=flask-svc

# Induce memory leak
bash chaos/memory_leak.sh
```

Grafana will visualize recovery metrics and SLO breach if any.

## 📊 Dashboards & Metrics

- **Latency**: `http_request_duration_seconds`
- **Error rate**: `http_errors_total`
- **Availability**: Uptime per 5m window
- **Custom SLO**: 99.9% successful requests under 300ms

Grafana is exposed via NodePort: http://localhost:30000

## 📎 Project Structure

```plaintext
resilienceops/
├── app/                  # Flask application
├── chaos/                # Fault injection scripts
├── k8s/                  # Kubernetes YAML files
├── dashboards/           # Grafana JSON dashboards
├── monitoring/           # Prometheus config
├── loadtest/             # Locust or k6 tests
├── scripts/              # Auto-healing, clean-up
└── README.md
```

## 📗 Learning Outcomes

✅ Reinforces SRE principles like SLOs, error budgets, and toil reduction  
✅ Demonstrates ability to work with observability stacks  
✅ Explores incident response techniques like chaos testing and recovery  
✅ Shows containerization and orchestration competency

## 🧠 Inspiration

- [Google SRE Book](https://sre.google/books/)
- [Awesome SRE GitHub Repo](https://github.com/dastergon/awesome-sre)
- [Kelsey Hightower's Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

## 📝 Author

**David Rodriguez**  
[LinkedIn](https://www.linkedin.com/in/david-i-rodriguez/)  
UTSA | CPS Energy | AWS | Automation | Scripting

## 📜 License

MIT License. Fork it, star it, or contribute!
