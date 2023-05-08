import base64
import yaml
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Get the service account token from the config file
with open('./<filename>/var.yaml', 'r') as f:
    cfg = yaml.safe_load(f)

token = cfg["vars"]["token"]
ns = cfg["vars"]["namespace"]
secret = cfg["vars"]["secret_name"]
sa = cfg["vars"]["service_account_name"]

# Create the Kubernetes client
api = client.CoreV1Api()

# Convert the token to base64 encoding
token_b64 = base64.b64encode(token.encode("utf-8")).decode("utf-8")

# Create the secret object
secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": secret,
        "annotations": {
            "kubernetes.io/service-account.name": sa
        }
    },
    "type": "kubernetes.io/service-account-token",
    "data": {
        "token": token_b64
    }
}

# Create the secret in the namespace
api.create_namespaced_secret(namespace=ns, body=secret)

print("Secret created successfully.")
