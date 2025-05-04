#!/bin/bash
echo "Tearing down ResilienceOps deployment..."
kubectl delete -n resilienceops -f ../k8s/deployment.yaml
kubectl delete -n resilienceops -f ../k8s/service.yaml
kubectl delete namespace resilienceops
minikube stop
