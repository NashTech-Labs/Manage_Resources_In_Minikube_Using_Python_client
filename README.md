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

minikube status --profile kubernetes-cluster
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

```
### on system install required libraries (is is good to have virtual)
You may get error like this
```
$ python3 -m venv k8s
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
[sudo] password for vaibhav: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.10-venv
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3-venv python3.10-venv
0 upgraded, 4 newly installed, 0 to remove and 6 not upgraded.
Need to get 2,474 kB of archives.
After this operation, 2,888 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-pip-whl all 22.0.2+dfsg-1 [1,679 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-setuptools-whl all 59.6.0-1.2 [788 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3.10-venv amd64 3.10.4-3ubuntu0.1 [5,668 B]
Get:4 http://in.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-venv amd64 3.10.4-0ubuntu2 [1,050 B]
Fetched 2,474 kB in 2s (1,212 kB/s)      
Selecting previously unselected package python3-pip-whl.
(Reading database ... 234512 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_22.0.2+dfsg-1_all.deb ...
Unpacking python3-pip-whl (22.0.2+dfsg-1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_59.6.0-1.2_all.deb ...
Unpacking python3-setuptools-whl (59.6.0-1.2) ...
Selecting previously unselected package python3.10-venv.
Preparing to unpack .../python3.10-venv_3.10.4-3ubuntu0.1_amd64.deb ...
Unpacking python3.10-venv (3.10.4-3ubuntu0.1) ...
Selecting previously unselected package python3-venv.
Preparing to unpack .../python3-venv_3.10.4-0ubuntu2_amd64.deb ...
Unpacking python3-venv (3.10.4-0ubuntu2) ...
Setting up python3-setuptools-whl (59.6.0-1.2) ...
Setting up python3-pip-whl (22.0.2+dfsg-1) ...
Setting up python3.10-venv (3.10.4-3ubuntu0.1) ...
Setting up python3-venv (3.10.4-0ubuntu2) ...
```
Now create a virtual environment and work on that
```bash
$ python3 -m venv k8s
$ source k8s/bin/activate
(k8s) $ pip install kubernetes
Collecting kubernetes
  Downloading kubernetes-24.2.0-py2.py3-none-any.whl (1.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 4.9 MB/s eta 0:00:00
Collecting certifi>=14.05.14
  Downloading certifi-2022.6.15-py3-none-any.whl (160 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.2/160.2 KB 2.8 MB/s eta 0:00:00
Requirement already satisfied: setuptools>=21.0.0 in ./k8s/lib/python3.10/site-packages (from kubernetes) (59.6.0)
Collecting requests-oauthlib
  Using cached requests_oauthlib-1.3.1-py2.py3-none-any.whl (23 kB)
Collecting python-dateutil>=2.5.3
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 KB 4.6 MB/s eta 0:00:00
Collecting requests
  Downloading requests-2.28.1-py3-none-any.whl (62 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 KB 1.1 MB/s eta 0:00:00
Collecting pyyaml>=5.4.1
  Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 682.2/682.2 KB 7.6 MB/s eta 0:00:00
Collecting websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0
  Using cached websocket_client-1.3.3-py3-none-any.whl (54 kB)
Collecting google-auth>=1.0.1
  Downloading google_auth-2.10.0-py2.py3-none-any.whl (167 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.2/167.2 KB 2.1 MB/s eta 0:00:00
Collecting urllib3>=1.24.2
  Downloading urllib3-1.26.11-py2.py3-none-any.whl (139 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.9/139.9 KB 1.1 MB/s eta 0:00:00
Collecting six>=1.9.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting pyasn1-modules>=0.2.1
  Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.3/155.3 KB 3.3 MB/s eta 0:00:00
Collecting cachetools<6.0,>=2.0.0
  Using cached cachetools-5.2.0-py3-none-any.whl (9.3 kB)
Collecting rsa<5,>=3.1.4
  Using cached rsa-4.9-py3-none-any.whl (34 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 982.3 kB/s eta 0:00:00
Collecting charset-normalizer<3,>=2
  Downloading charset_normalizer-2.1.0-py3-none-any.whl (39 kB)
Collecting oauthlib>=3.0.0
  Downloading oauthlib-3.2.0-py3-none-any.whl (151 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.5/151.5 KB 457.7 kB/s eta 0:00:00
Collecting pyasn1<0.5.0,>=0.4.6
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.1/77.1 KB 1.4 MB/s eta 0:00:00
Installing collected packages: pyasn1, websocket-client, urllib3, six, rsa, pyyaml, pyasn1-modules, oauthlib, idna, charset-normalizer, certifi, cachetools, requests, python-dateutil, google-auth, requests-oauthlib, kubernetes
Successfully installed cachetools-5.2.0 certifi-2022.6.15 charset-normalizer-2.1.0 google-auth-2.10.0 idna-3.3 kubernetes-24.2.0 oauthlib-3.2.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 python-dateutil-2.8.2 pyyaml-6.0 requests-2.28.1 requests-oauthlib-1.3.1 rsa-4.9 six-1.16.0 urllib3-1.26.11 websocket-client-1.3.3

```

#### Authentication Work

To Use the Python Client to perform tasks on the cluster, we nee to autheticate the client and provide it the roles to do perform all the tasks

* creating Service Account

```
$ kubectl create sa resource-service-account
serviceaccount/resource-service-account created
$ kubectl describe sa resource-service-account
Name:                resource-service-account
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   <none>
Tokens:              <none>
Events:              <none>

```
As you can see no token is generated
**NOTE:** 
In kubernetes 1.24 this was disabled by default
See the MUST READ section of the changelog: [kubernetes/CHANGELOG-1.24.md at master · kubernetes/kubernetes · GitHub](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#no-really-you-must-read-this-before-you-upgrade)

Relevant section:

    The LegacyServiceAccountTokenNoAutoGeneration feature gate is beta, and enabled by default. When enabled, Secret API objects containing service account tokens are no longer auto-generated for every ServiceAccount. Use the TokenRequest 25 API to acquire service account tokens, or if a non-expiring token is required, create a Secret API object for the token controller to populate with a service account token by following this guide 18. (#108309, @zshihang)

and another blog:
https://itnext.io/big-change-in-k8s-1-24-about-serviceaccounts-and-their-secrets-4b909a4af4e0

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

$ kubectl get secret
NAME                             TYPE                                  DATA   AGE
resource-service-account-token   kubernetes.io/service-account-token   3      82s

$ kubectl describe sa resource-service-account
Name:                resource-service-account
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   <none>
Tokens:              resource-service-account-token
Events:              <none>

$ kubectl get secret resource-service-account-token -o json | jq -r .data.token | base64 --decode
eyJhbGciOiJSUzI1NiIsImtpZCI6IkFVb3A3VUZrN0YzeGVaaWxrX1JfZGhfLTNjUTNGbVNiM21KRlB6cC00QXMifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6InJlc291cmNlLXNlcnZpY2UtYWNjb3VudC10b2tlbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJyZXNvdXJjZS1zZXJ2aWNlLWFjY291bnQiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIzMDEwMWQ1NS1kMWZlLTRiNGEtOGYyMy0wMGQyNmNkYWI2MjciLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDpyZXNvdXJjZS1zZXJ2aWNlLWFjY291bnQifQ.iHRDXeqUiN8oKMxgZA6pFijr5xoyoncXFoWIJx0gXm_EWZt-mIMsbBrZwax6SsilajiI9zSQFp9nqgwBzKzZQwTqdtcuvE-RYQJLxr4sFNfMtbfOpx-QT255ymBOkKEg2cG5q89w1vnxoMuykHIu4HpqZv0EaMuALvqOeekv_-PpqBMmv_Nl4zwHuTwLFHF6CHvU9JVT0xiNzznGlCx86enl53n5nQrQ4Zjqh3OeopnHO7TJ7YQI3SEKl4MK-gOS8ENd8m_nAVG_-J1MRs9j8LpA_Ttyqw43pcwEAFz4K--ydEkbcbA-n2hjlbkPrtBoN2vLIA2-1QEks89Qw30a5wv
```
You may need to install *jq* the JSON Parser
```bash
$ sudo apt-get install jq
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
jq is already the newest version (1.6-2.1ubuntu3).
0 upgraded, 0 newly installed, 0 to remove and 6 not upgraded.

```

Now we will pass this value to a environment variable **SERVICE_TOKEN** for our use.
```bash
$ export SERVICE_TOKEN=$(kubectl get secret resource-service-account-token -o json | jq -r .data.token | base64 --decode)

```
We use this to authenticate our python client. First lets check it.  Using a service account also has the benefit, that it's not tied to any single person, which is always preferable for automation purposes.
The url is where control plane is running that can be get from `kubectl cluster-info` as before.
Token from the output above can be then used in requests: 
```
$ curl -k -X GET -H "Authorization: Bearer $SERVICE_TOKEN" https://192.168.49.2:8443/apis
{
  "kind": "APIGroupList",
  "apiVersion": "v1",
  "groups": [
    {
      "name": "apiregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "apiregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apps",
      "versions": [
        {
          "groupVersion": "apps/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apps/v1",
        "version": "v1"
      }
    },
    {
      "name": "events.k8s.io",
      "versions": [
        {
          "groupVersion": "events.k8s.io/v1",
          "version": "v1"
        },
        {
          "groupVersion": "events.k8s.io/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "events.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "authentication.k8s.io",
      "versions": [
        {
          "groupVersion": "authentication.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "authentication.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "authorization.k8s.io",
      "versions": [
        {
          "groupVersion": "authorization.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "authorization.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "autoscaling",
      "versions": [
        {
          "groupVersion": "autoscaling/v2",
          "version": "v2"
        },
        {
          "groupVersion": "autoscaling/v1",
          "version": "v1"
        },
        {
          "groupVersion": "autoscaling/v2beta1",
          "version": "v2beta1"
        },
        {
          "groupVersion": "autoscaling/v2beta2",
          "version": "v2beta2"
        }
      ],
      "preferredVersion": {
        "groupVersion": "autoscaling/v2",
        "version": "v2"
      }
    },
    {
      "name": "batch",
      "versions": [
        {
          "groupVersion": "batch/v1",
          "version": "v1"
        },
        {
          "groupVersion": "batch/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "batch/v1",
        "version": "v1"
      }
    },
    {
      "name": "certificates.k8s.io",
      "versions": [
        {
          "groupVersion": "certificates.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "certificates.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "networking.k8s.io",
      "versions": [
        {
          "groupVersion": "networking.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "networking.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "policy",
      "versions": [
        {
          "groupVersion": "policy/v1",
          "version": "v1"
        },
        {
          "groupVersion": "policy/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "policy/v1",
        "version": "v1"
      }
    },
    {
      "name": "rbac.authorization.k8s.io",
      "versions": [
        {
          "groupVersion": "rbac.authorization.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "rbac.authorization.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "storage.k8s.io",
      "versions": [
        {
          "groupVersion": "storage.k8s.io/v1",
          "version": "v1"
        },
        {
          "groupVersion": "storage.k8s.io/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "storage.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "admissionregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "admissionregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "admissionregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apiextensions.k8s.io",
      "versions": [
        {
          "groupVersion": "apiextensions.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiextensions.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "scheduling.k8s.io",
      "versions": [
        {
          "groupVersion": "scheduling.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "scheduling.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "coordination.k8s.io",
      "versions": [
        {
          "groupVersion": "coordination.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "coordination.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "node.k8s.io",
      "versions": [
        {
          "groupVersion": "node.k8s.io/v1",
          "version": "v1"
        },
        {
          "groupVersion": "node.k8s.io/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "node.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "discovery.k8s.io",
      "versions": [
        {
          "groupVersion": "discovery.k8s.io/v1",
          "version": "v1"
        },
        {
          "groupVersion": "discovery.k8s.io/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "discovery.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "flowcontrol.apiserver.k8s.io",
      "versions": [
        {
          "groupVersion": "flowcontrol.apiserver.k8s.io/v1beta2",
          "version": "v1beta2"
        },
        {
          "groupVersion": "flowcontrol.apiserver.k8s.io/v1beta1",
          "version": "v1beta1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "flowcontrol.apiserver.k8s.io/v1beta2",
        "version": "v1beta2"
      }
    }
  ]
}
```
This confirms our authentication, but not authorized to do much of anything. Therefore, next we need to create a Role and bind it to the ServiceAccount so that we can perform actions on resources: 
```
$ kubectl create clusterrole manage-pods \
    --verb=get --verb=list --verb=watch --verb=create --verb=update --verb=patch --verb=delete \
    --resource=pods
clusterrole.rbac.authorization.k8s.io/manage-pods created
$ kubectl -n default create rolebinding sa-manage-pods \
    --clusterrole=manage-pods \
    --serviceaccount=default:resource-service-account
rolebinding.rbac.authorization.k8s.io/sa-manage-pods created
```
Now we have the permission to perform any action on pods, limited to default namespace.

You should always keep your roles very narrow and specific, but for minikube, it makes sense to apply cluster-wide admin role: 
```
$ kubectl create clusterrolebinding sa-cluster-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=default:resource-service-account
clusterrolebinding.rbac.authorization.k8s.io/sa-cluster-admin created

```

 To get a better understanding of what is kubectl and also the client doing under the hood, we will start with raw HTTP requests using curl.

The easiest way to find out what requests are being made under the hood, is to run the desired kubectl command with -v 10 which will output complete curl commands.The output with loglevel 10 will be very verbose, but somewhere it there, you will find the above curl command. 
```bash
$ kubectl get pods -v 10
I0818 12:04:16.024889 1190803 loader.go:372] Config loaded from file:  /home/vaibhav/.kube/config
I0818 12:04:16.025335 1190803 cert_rotation.go:137] Starting client certificate rotation controller
I0818 12:04:16.025520 1190803 cached_discovery.go:112] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/servergroups.json
I0818 12:04:16.025747 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1/serverresources.json
I0818 12:04:16.025753 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.025820 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1/serverresources.json
I0818 12:04:16.025830 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/admissionregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.025841 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta1/serverresources.json
I0818 12:04:16.025847 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apps/v1/serverresources.json
I0818 12:04:16.025841 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2/serverresources.json
I0818 12:04:16.025907 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1beta1/serverresources.json
I0818 12:04:16.025914 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v1/serverresources.json
I0818 12:04:16.025907 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiextensions.k8s.io/v1/serverresources.json
I0818 12:04:16.025910 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.025938 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta2/serverresources.json
I0818 12:04:16.025967 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authentication.k8s.io/v1/serverresources.json
I0818 12:04:16.025968 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/scheduling.k8s.io/v1/serverresources.json
I0818 12:04:16.025994 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/certificates.k8s.io/v1/serverresources.json
I0818 12:04:16.026007 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1/serverresources.json
I0818 12:04:16.026017 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1beta1/serverresources.json
I0818 12:04:16.026030 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/v1/serverresources.json
I0818 12:04:16.026039 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/coordination.k8s.io/v1/serverresources.json
I0818 12:04:16.026054 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.026070 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026089 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/rbac.authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.026113 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026117 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1/serverresources.json
I0818 12:04:16.026123 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/networking.k8s.io/v1/serverresources.json
I0818 12:04:16.026141 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta2/serverresources.json
I0818 12:04:16.026144 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026169 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1/serverresources.json
I0818 12:04:16.026198 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1/serverresources.json
I0818 12:04:16.026203 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026370 1190803 cached_discovery.go:112] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/servergroups.json
I0818 12:04:16.026445 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.026472 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026501 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1/serverresources.json
I0818 12:04:16.026518 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/rbac.authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.026523 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026522 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1/serverresources.json
I0818 12:04:16.026571 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authentication.k8s.io/v1/serverresources.json
I0818 12:04:16.026568 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/networking.k8s.io/v1/serverresources.json
I0818 12:04:16.026588 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1/serverresources.json
I0818 12:04:16.026644 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1/serverresources.json
I0818 12:04:16.026651 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.026654 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1beta1/serverresources.json
I0818 12:04:16.026661 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1beta1/serverresources.json
I0818 12:04:16.026660 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v1/serverresources.json
I0818 12:04:16.026664 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apps/v1/serverresources.json
I0818 12:04:16.026713 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026732 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/certificates.k8s.io/v1/serverresources.json
I0818 12:04:16.026732 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta1/serverresources.json
I0818 12:04:16.026744 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta2/serverresources.json
I0818 12:04:16.026732 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2/serverresources.json
I0818 12:04:16.026779 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026783 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/v1/serverresources.json
I0818 12:04:16.026781 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1/serverresources.json
I0818 12:04:16.026798 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1/serverresources.json
I0818 12:04:16.026794 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.026825 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiextensions.k8s.io/v1/serverresources.json
I0818 12:04:16.026839 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/admissionregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.026845 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/scheduling.k8s.io/v1/serverresources.json
I0818 12:04:16.026854 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/coordination.k8s.io/v1/serverresources.json
I0818 12:04:16.026869 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta2/serverresources.json
I0818 12:04:16.027039 1190803 cached_discovery.go:112] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/servergroups.json
I0818 12:04:16.027124 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2/serverresources.json
I0818 12:04:16.027133 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.027138 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.027160 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.027205 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authentication.k8s.io/v1/serverresources.json
I0818 12:04:16.027225 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.027264 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.027264 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/storage.k8s.io/v1/serverresources.json
I0818 12:04:16.027279 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apps/v1/serverresources.json
I0818 12:04:16.027286 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.027314 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/apiextensions.k8s.io/v1/serverresources.json
I0818 12:04:16.027337 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1beta1/serverresources.json
I0818 12:04:16.027341 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v1/serverresources.json
I0818 12:04:16.027245 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/node.k8s.io/v1/serverresources.json
I0818 12:04:16.027392 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/flowcontrol.apiserver.k8s.io/v1beta2/serverresources.json
I0818 12:04:16.027410 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/discovery.k8s.io/v1/serverresources.json
I0818 12:04:16.027428 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/scheduling.k8s.io/v1/serverresources.json
I0818 12:04:16.027452 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/coordination.k8s.io/v1/serverresources.json
I0818 12:04:16.027458 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/v1/serverresources.json
I0818 12:04:16.027467 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta1/serverresources.json
I0818 12:04:16.027469 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/certificates.k8s.io/v1/serverresources.json
I0818 12:04:16.027499 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1/serverresources.json
I0818 12:04:16.027507 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/batch/v1beta1/serverresources.json
I0818 12:04:16.027511 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/admissionregistration.k8s.io/v1/serverresources.json
I0818 12:04:16.027532 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1/serverresources.json
I0818 12:04:16.027535 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/autoscaling/v2beta2/serverresources.json
I0818 12:04:16.027557 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/policy/v1beta1/serverresources.json
I0818 12:04:16.027572 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/networking.k8s.io/v1/serverresources.json
I0818 12:04:16.027584 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/events.k8s.io/v1/serverresources.json
I0818 12:04:16.027634 1190803 cached_discovery.go:76] returning cached discovery info from /home/vaibhav/.kube/cache/discovery/192.168.49.2_8443/rbac.authorization.k8s.io/v1/serverresources.json
I0818 12:04:16.029162 1190803 round_trippers.go:466] curl -v -XGET  -H "User-Agent: kubectl/v1.24.3 (linux/amd64) kubernetes/aef86a9" -H "Accept: application/json;as=Table;v=v1;g=meta.k8s.io,application/json;as=Table;v=v1beta1;g=meta.k8s.io,application/json" 'https://192.168.49.2:8443/api/v1/namespaces/default/pods?limit=500'
I0818 12:04:16.029346 1190803 round_trippers.go:510] HTTP Trace: Dial to tcp:192.168.49.2:8443 succeed
I0818 12:04:16.045513 1190803 round_trippers.go:553] GET https://192.168.49.2:8443/api/v1/namespaces/default/pods?limit=500 200 OK in 16 milliseconds
I0818 12:04:16.045533 1190803 round_trippers.go:570] HTTP Statistics: DNSLookup 0 ms Dial 0 ms TLSHandshake 4 ms ServerProcessing 11 ms Duration 16 ms
I0818 12:04:16.045543 1190803 round_trippers.go:577] Response Headers:
I0818 12:04:16.045552 1190803 round_trippers.go:580]     Audit-Id: 84c49ce3-b22b-47bf-9d9f-b6b3bbfc9d9d
I0818 12:04:16.045561 1190803 round_trippers.go:580]     Cache-Control: no-cache, private
I0818 12:04:16.045569 1190803 round_trippers.go:580]     Content-Type: application/json
I0818 12:04:16.045577 1190803 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: d35cff50-48c4-4c65-ba20-b3ca84dd52fb
I0818 12:04:16.045586 1190803 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 27037bd2-6b3a-4de1-9959-1d50f90b7d69
I0818 12:04:16.045594 1190803 round_trippers.go:580]     Content-Length: 2934
I0818 12:04:16.045603 1190803 round_trippers.go:580]     Date: Thu, 18 Aug 2022 06:34:16 GMT
I0818 12:04:16.045637 1190803 request.go:1073] Response Body: {"kind":"Table","apiVersion":"meta.k8s.io/v1","metadata":{"resourceVersion":"12654"},"columnDefinitions":[{"name":"Name","type":"string","format":"name","description":"Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names","priority":0},{"name":"Ready","type":"string","format":"","description":"The aggregate readiness state of this pod for accepting traffic.","priority":0},{"name":"Status","type":"string","format":"","description":"The aggregate status of the containers in this pod.","priority":0},{"name":"Restarts","type":"string","format":"","description":"The number of times the containers in this pod have been restarted and when the last container in this pod has restarted.","priority":0},{"name":"Age","type":"string","format":"","description":"CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.\n\nPopulated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata","priority":0},{"name":"IP","type":"string","format":"","description":"IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.","priority":1},{"name":"Node","type":"string","format":"","description":"NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.","priority":1},{"name":"Nominated Node","type":"string","format":"","description":"nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.","priority":1},{"name":"Readiness Gates","type":"string","format":"","description":"If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to \"True\" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates","priority":1}],"rows":[]}
No resources found in default namespace.

$ curl -k -v -XGET  -H "Accept: application/json;as=Table;v=v1;g=meta.k8s.io,application/json..." \
    'https://192.168.49.2:8443/api/v1/namespaces/kube-system/pods?limit=500'
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 192.168.49.2:8443...
* Connected to 192.168.49.2 (192.168.49.2) port 8443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Request CERT (13):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.3 (OUT), TLS handshake, Certificate (11):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: O=system:masters; CN=minikube
*  start date: Aug 16 09:20:32 2022 GMT
*  expire date: Aug 16 09:20:32 2025 GMT
*  issuer: CN=minikubeCA
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* Using Stream ID: 1 (easy handle 0x556c73a1fe80)
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
> GET /api/v1/namespaces/default/pods?limit=500 HTTP/2
> Host: 192.168.49.2:8443
> user-agent: curl/7.81.0
> accept: application/json;as=Table;v=v1;g=meta.k8s.io,application/json...
> 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Connection state changed (MAX_CONCURRENT_STREAMS == 250)!
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
< HTTP/2 403 
< audit-id: 7a8f7b11-4cb2-4388-a544-88d85e5e95b8
< cache-control: no-cache, private
< content-type: application/json
< x-content-type-options: nosniff
< x-kubernetes-pf-flowschema-uid: 5505646b-e2fa-4d3d-aed3-6d23efd3a6e6
< x-kubernetes-pf-prioritylevel-uid: 02df8a65-6f10-4ea3-9a41-ee7cbfae8f9a
< content-length: 302
< date: Thu, 18 Aug 2022 06:52:24 GMT
< 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "pods is forbidden: User \"system:anonymous\" cannot list resource \"pods\" in API group \"\" in the namespace \"default\"",
  "reason": "Forbidden",
  "details": {
    "kind": "pods"
  },
  "code": 403
* Connection #0 to host 192.168.49.2 left intact
}
```

Add a Bearer token header in the above curl command with your long-lived token and you should be able to perform same actions as kubectl, such as: 

```bash
$ curl -s -k -XGET -H "Authorization: Bearer $SERVICE_TOKEN" -H "Accept: application/json, */*" -H "Content-Type: application/json"     -H "kubernetes/$Format" 'https://192.168.49.2:8443/api/v1/namespaces/kube-system/pods/storage-provisioner' | jq .status.phase
"Running"

```
add a json file and deploy using this using curl http request.
```bash
$ cat > nginx-pod.json <<EOFF
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": "nginx1"
    },
    "spec": {
        "containers": [
            {
                "name": "nginx",
                "image": "nginx:1.7.9",
                "ports": [
                    {
                        "containerPort": 80
                    }
                ]
            }
        ]
    }
}
EOF
```
```bash
$ curl -k -XPOST -H "Authorization: Bearer $SERVICE_TOKEN" -H "Accept: application/json, */*" -H "Content-Type: application/json"     -H "kubernetes/$Format" https://192.168.49.2:8443/api/v1/namespaces/default/pods -d@nginx-pod.json 
{
  "kind": "Pod",
  "apiVersion": "v1",
  "metadata": {
    "name": "nginx1",
    "namespace": "default",
    "uid": "132bba11-5bbe-4c2d-a4f0-77b2d0d4e6c0",
    "resourceVersion": "15277",
    "creationTimestamp": "2022-08-18T07:23:01Z",
    "managedFields": [
      {
        "manager": "curl",
        "operation": "Update",
        "apiVersion": "v1",
        "time": "2022-08-18T07:23:01Z",
        "fieldsType": "FieldsV1",
        "fieldsV1": {
          "f:spec": {
            "f:containers": {
              "k:{\"name\":\"nginx\"}": {
                ".": {},
                "f:image": {},
                "f:imagePullPolicy": {},
                "f:name": {},
                "f:ports": {
                  ".": {},
                  "k:{\"containerPort\":80,\"protocol\":\"TCP\"}": {
                    ".": {},
                    "f:containerPort": {},
                    "f:protocol": {}
                  }
                },
                "f:resources": {},
                "f:terminationMessagePath": {},
                "f:terminationMessagePolicy": {}
              }
            },
            "f:dnsPolicy": {},
            "f:enableServiceLinks": {},
            "f:restartPolicy": {},
            "f:schedulerName": {},
            "f:securityContext": {},
            "f:terminationGracePeriodSeconds": {}
          }
        }
      }
    ]
  },
  "spec": {
    "volumes": [
      {
        "name": "kube-api-access-tdqc5",
        "projected": {
          "sources": [
            {
              "serviceAccountToken": {
                "expirationSeconds": 3607,
                "path": "token"
              }
            },
            {
              "configMap": {
                "name": "kube-root-ca.crt",
                "items": [
                  {
                    "key": "ca.crt",
                    "path": "ca.crt"
                  }
                ]
              }
            },
            {
              "downwardAPI": {
                "items": [
                  {
                    "path": "namespace",
                    "fieldRef": {
                      "apiVersion": "v1",
                      "fieldPath": "metadata.namespace"
                    }
                  }
                ]
              }
            }
          ],
          "defaultMode": 420
        }
      }
    ],
    "containers": [
      {
        "name": "nginx",
        "image": "nginx:1.7.9",
        "ports": [
          {
            "containerPort": 80,
            "protocol": "TCP"
          }
        ],
        "resources": {},
        "volumeMounts": [
          {
            "name": "kube-api-access-tdqc5",
            "readOnly": true,
            "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount"
          }
        ],
        "terminationMessagePath": "/dev/termination-log",
        "terminationMessagePolicy": "File",
        "imagePullPolicy": "IfNotPresent"
      }
    ],
    "restartPolicy": "Always",
    "terminationGracePeriodSeconds": 30,
    "dnsPolicy": "ClusterFirst",
    "serviceAccountName": "default",
    "serviceAccount": "default",
    "securityContext": {},
    "schedulerName": "default-scheduler",
    "tolerations": [
      {
        "key": "node.kubernetes.io/not-ready",
        "operator": "Exists",
        "effect": "NoExecute",
        "tolerationSeconds": 300
      },
      {
        "key": "node.kubernetes.io/unreachable",
        "operator": "Exists",
        "effect": "NoExecute",
        "tolerationSeconds": 300
      }
    ],
    "priority": 0,
    "enableServiceLinks": true,
    "preemptionPolicy": "PreemptLowerPriority"
  },
  "status": {
    "phase": "Pending",
    "qosClass": "BestEffort"
  }
}

$ kubectl get pods
NAME     READY   STATUS              RESTARTS   AGE
nginx1   0/1     ContainerCreating   0          36s
$ python3 pod-view.py
Name: nginx1, Namespace: default IP: 10.244.1.2

```
