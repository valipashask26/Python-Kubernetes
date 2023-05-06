from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Create a Kubernetes API client
apps_v1 = client.AppsV1Api()

# Define the deployment object using a dictionary
deployment = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "my-deployment",
        "labels": {
            "app": "my-app"
        }
    },
    "spec": {
        "replicas": 3,
        "selector": {
            "matchLabels": {
                "app": "my-app"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "my-app"
                }
            },
            "spec": {
                "imagePullSecrets": [
                    {
                        "name": "my-secret"
                    }
                ],
                "containers": [
                    {
                        "name": "my-container",
                        "image": "my-image:latest",
                        "ports": [
                            {
                                "containerPort": 80
                            }
                        ]
                    }
                ]
            }
        }
    }
}

# Create the deployment in Kubernetes
apps_v1.create_namespaced_deployment(namespace="default",body=deployment)   #define correct NS

print("Deployment created successfully!")
