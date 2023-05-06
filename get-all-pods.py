from kubernetes import client, config

# Load kubeconfig file (optional, assumes running in-cluster if not provided)
config.load_kube_config()

# Create the API client
api = client.CoreV1Api()

# List all pods in the cluster
pod_list = api.list_pod_for_all_namespaces().items

# Print pod details
for pod in pod_list:
    print(f"Name: {pod.metadata.name}, Status: {pod.status.phase}")
