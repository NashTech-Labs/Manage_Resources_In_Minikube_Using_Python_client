from kubernetes import client
import os

configuration = client.Configuration()
configuration.api_key_prefix["authorization"] = "Bearer"
configuration.host = "https://192.168.49.2:8443"
configuration.api_key["authorization"] = os.getenv("SERVICE_TOKEN", None)
configuration.verify_ssl = False  # Only for testing with Minikube!
api_client = client.ApiClient(configuration)
v1 = client.CoreV1Api(api_client)

ret = v1.list_namespaced_pod(namespace="default", watch=False)
for pod in ret.items:
    print(f"Name: {pod.metadata.name}, Namespace: {pod.metadata.namespace} IP: {pod.status.pod_ip}")
    # Name: example, Namespace: default IP: 10.244.2.2
