
# Kubernetes Ingress with Flask Template


## Deployment

Download [Minikube](https://minikube.sigs.k8s.io/docs/start/)


```bash
minikube version
minikube start
kubectl version
kubectl cluster-info
kubectl get nodes
minikube addons enable ingres
kubectl get pods -n ingress-nginx
```

Docker Images with Minikube:
```bash
cd app
docker build -t flask-kubernetes .
cd ..
cd app2
docker build -t flask-kubernetes2 .
minikube ssh
docker image ls
```

Deploy Kubernetes:
```bash
kubectl apply -f kubernetes
or
kubectl apply -f flask-app.yaml,flask-app-2.yaml,flask-service.yaml,flask-service-2.yaml,ingress.yaml
```

Minikube Dashboard:
```bash
minikube dashboard --url
```

Delete Kubernetes Resources:
```bash
kubectl delete all --all
```

Port Forwarding:
```bash
kubectl port-forward service/flask-service 5000:5000
kubectl port-forward service/flask-servie-2 5001:5001
```

Local Development:
```bash
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```