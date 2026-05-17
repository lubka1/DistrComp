
# DRIVE2STARS (D2S) — V2I Platform

A cloud-native Vehicle-to-Infrastructure (V2I) simulation platform built with microservices, Kubernetes, and Google Cloud Platform.

The project simulates assisted-driving communication between vehicle ECUs and backend infrastructure using distributed services, asynchronous messaging, and real-time monitoring.

### Environment Setup
```bash
conda env create -f environment.yml
conda activate auto2
```

## Microservices

- WHEREAMI — vehicle GPS tracking
- UTRACKED — movement history storage
- SONAR — distance monitoring
- BRAKENOW — emergency braking
- ORCHESTRATOR — control and validation logic
- SPIDER — API Gateway
- SIMULATOR — vehicle/sensor simulation
- STOREFRONT — web dashboard

## Tech Stack

- Kubernetes (GKE)
- Docker
- Spring Boot
- RabbitMQ
- MongoDB

## Deployment

The platform is designed for deployment on Google Kubernetes Engine (GKE) using Kubernetes manifests and containerized services.
