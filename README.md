# Manage_Resources_In_Minikube_Using_Python_client
In this techhub we are managing the resources in minikube using Python client.


#### Create a cluster on minikube with 3 nodes or how many you want

```
$ minikube start --nodes 3 -p kubernetes-cluster
```
```
$ kubectl get nodes
```
NAME                     STATUS     ROLES           AGE     VERSION
kubernetes-cluster       Ready      control-plane   5m5s    v1.24.3
kubernetes-cluster-m02   Ready      <none>          2m45s   v1.24.3
kubernetes-cluster-m03   NotReady   <none>          48s     v1.24.3

```
minikube status --profile kubernetes-cluster
```
kubernetes-cluster
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

kubernetes-cluster-m02
type: Worker
host: Running
kubelet: Running

kubernetes-cluster-m03
type: Worker
host: Running
kubelet: Running


### on system install required libraries (is is good to have virtual)
You may get error like this
```
$ python3 -m venv k8s
```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```
So install the package 
```bash 
$  sudo apt install python3-venv
```
Now create a virtual environment and work on that
```bash
$ python3 -m venv k8s
$ source k8s/bin/activate
(k8s) $ pip install kubernetes
```

#### Authentication Work

To Use the Python Client to perform tasks on the cluster, we nee to autheticate the client and provide it the roles to do perform all the tasks

* creating Service Account

```
$ kubectl create sa resource-service-account
```

```
$ kubectl describe sa resource-service-account
```
    
```    
$ kubectl apply -f - <<EOF
> apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: resource-service-account-token
  annotations:
    kubernetes.io/service-account.name: "resource-service-account"
> EOF
secret/resource-service-account-token created
```
```
$ kubectl get secret
```

    ```
$ kubectl get secret resource-service-account-token -o json | jq -r .data.token | base64 --decode
 ```
 
 ```
    $ sudo apt-get install jq
 ```
    
    
```
$ kubectl get pods
```

```
$ python3 pod-view.py
```

