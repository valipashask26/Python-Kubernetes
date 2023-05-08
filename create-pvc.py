from kubernetes import client, config

# Load the Kubernetes configuration file
config.load_kube_config()

# Create a Kubernetes client
v1 = client.CoreV1Api()

# Define the PVC configuration as a Python dictionary
pvc = {
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": "my-pvc"
    },
    "spec": {
        "accessModes": [
            "ReadWriteOnce"
        ],
        "resources": {
            "requests": {
                "storage": "1Gi"
            }
        }
    }
}

# Create the PVC using the Kubernetes API
v1.create_namespaced_persistent_volume_claim(namespace="default",body=pvc)
