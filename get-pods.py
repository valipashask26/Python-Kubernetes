from kubernetes import client, config

# Load kubeconfig file (optional, assumes running in-cluster if not provided)
config.load_kube_config()

# Create the API client
api = client.CoreV1Api()

# Specify the namespace
namespace = "my-namespace"

# List all pods in the namespace
pod_list = api.list_namespaced_pod(namespace).items

# Print pod details
for pod in pod_list:
    print(f"Name: {pod.metadata.name}, Status: {pod.status.phase}")
