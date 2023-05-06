from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Create a Kubernetes API client
apps_v1 = client.AppsV1Api()

# List deployments in the "default" namespace
deployments = apps_v1.list_namespaced_deployment(namespace="default") #give correct NS

# Print the name of each deployment
for deployment in deployments.items:
    print(deployment.metadata.name)
