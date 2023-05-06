from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Create a Kubernetes API client
core_v1 = client.CoreV1Api()

# Define the Pod object using a dictionary
pod = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": "my-pod"
    },
    "spec": {
        "volumes": [
            {
                "name": "my-pvc",
                "persistentVolumeClaim": {
                    "claimName": "my-claim"
                }
            }
        ],
        "containers": [
            {
                "name": "my-container",
                "image": "my-image:latest",
                "volumeMounts": [
                    {
                        "name": "my-pvc",
                        "mountPath": "/mnt/data"
                    }
                ]
            }
        ]
    }
}

# Create the Pod in Kubernetes
core_v1.create_namespaced_pod(
    namespace="default",
    body=pod
)

print("Pod created successfully!")
