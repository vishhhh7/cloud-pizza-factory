# 🍕 Cloud Pizza Factory

A beginner-friendly Docker and Kubernetes project demonstrating:

- Containerization using Docker
- Kubernetes Deployments
- Self-Healing Pods
- Scaling Applications
- Flask Web Application

## Tech Stack

- Python
- Flask
- Docker
- Kubernetes

## Run with Docker

```bash
docker build -t cloud-pizza .
docker run -p 5000:5000 cloud-pizza
```

## Deploy with Kubernetes

```bash
kubectl apply -f deployment.yaml
```

## Scale Application

```bash
kubectl scale deployment cloud-pizza --replicas=5
```

## Features

✅ Dockerized Flask Application

✅ Kubernetes Deployment

✅ Self-Healing Pods

✅ Horizontal Scaling

---

Built as a hands-on DevOps learning project.