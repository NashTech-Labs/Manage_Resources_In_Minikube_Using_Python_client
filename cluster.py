from os import path
from kubernetes.client.rest import ApiException
from kubernetes import client, config
from os import path
from kubernetes import client, config
import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client import ApiClient


def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = kubernetes.client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
            api_instance1 = kubernetes.client.CoreV1Api(api_client)
        return api_instance1
    except Exception as e:
        print("Error getting kubernetes client \n{}".format(e))
        return None

def __format_data_for_nodes(client_output):
    temp_dict={}
    temp_list=[]
    json_data=ApiClient().sanitize_for_serialization(client_output)
    if len(json_data["items"]) != 0:
        for node in json_data["items"]:
            temp_dict={
                "node": node["metadata"]["name"],
                "labels": node["metadata"]["labels"],
                }
            temp_list.append(temp_dict)
    return temp_list


def get_nodes(cluster_details, namespace="default",all_namespaces=False):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
       
        node_list = client_api.list_node()
        data=__format_data_for_nodes(node_list)
        print (data)

def main():
    cluster_details={
        "bearer_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6Imh2TG5kQ0l1U1k1NHVzSDM0S1pac29WLTVjbXF4TjdiNkQ5TDRXeWZRMEUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFwaS1zZXJ2aWNlLWFjY291bnQtdG9rZW4tN3I3a3YiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYXBpLXNlcnZpY2UtYWNjb3VudCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjQzYTg4YjhjLWVjMWQtNGYxNS1hMmQ3LTFiMjNkODFkYWYzZiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmFwaS1zZXJ2aWNlLWFjY291bnQifQ.kABKbY1t70wwmhTIj1IPanEbdqWvYloH8-36stcgozZAzR7G_10jFbguoa0hIkkP5uBFrkSn067D5QKy8S5BjdQtbTCX8W1giS-FkMkdgvWYsQZIyyIFDcxTq7fX4Z3nPtOuMQ78fHNORJ2NWlWCtRLy7q4c9FvZiVxsiK9YLCnKPB99dPzyG4szdQmKwjMkReRX2vLOICkVZWN_-xmDxlolu5mptIofVR0FaLWm0uMjM7sTdo7773gl0gp8oG_N1qbS9E4ZCRNU7q3KTIXxJiH-9b0naj_jgqmtTZoDpxxXvEnwX5nK6BKC2HffmPPco-XwKiriEbmDA-esCXXgcg",
        "api_server_endpoint":"https://C582161F558BEC14C50BC1AC50CF6263.gr7.us-east-1.eks.amazonaws.com"
    }

    get_nodes(cluster_details)


if __name__ == "__main__":
    main()
