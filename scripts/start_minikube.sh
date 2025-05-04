#!/bin/bash
echo "Starting Minikube cluster..."
minikube start --memory=4096 --cpus=2

echo "Creating namespace..."
kubectl apply -f ../k8s/namespace.yaml

echo "Deploying app..."
kubectl apply -n resilienceops -f ../k8s/deployment.yaml
kubectl apply -n resilienceops -f ../k8s/service.yaml

echo "Done. Access the app at NodePort 30036."
