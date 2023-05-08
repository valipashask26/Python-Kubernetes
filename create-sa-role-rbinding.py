### this code created SA, ROLE and ROLEBACK

from kubernetes import client, config
import yaml

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api = client.CoreV1Api()
rbac_api = client.RbacAuthorizationV1Api()

# Load the configuration from the YAML file
with open('./<filename>/var.yaml') as f:        #remove this reading and directly mention the values
    cfg = yaml.safe_load(f)

ns = cfg["vars"]["namespace"]
sa = cfg["vars"]["service_account_name"]
role = cfg["vars"]["role_name"]
rolebinding = cfg["vars"]["role_binding_name"]

# Create a new service account
sa_manifest = {
    "apiVersion": "v1",
    "kind": "ServiceAccount",
    "metadata": {
        "name": sa,
    },
}
api.create_namespaced_service_account(namespace=ns, body=sa_manifest)

# Create a new role
role_manifest = {
    "apiVersion": "rbac.authorization.k8s.io/v1",
    "kind": "Role",
    "metadata": {
        "name": role,
    },
    "rules": [
        {
            "apiGroups": [""],
            "resources": ["configmaps","deployments", "secrets", "pods","services","ingresses"],
            "verbs": ["get", "list", "watch", "create", "update", "patch", "delete"],
        },
    ],
}
rbac_api.create_namespaced_role(namespace=ns, body=role_manifest)

# Create a new role binding
role_binding_manifest = {
    "apiVersion": "rbac.authorization.k8s.io/v1",
    "kind": "RoleBinding",
    "metadata": {
        "name": rolebinding,
    },
    "roleRef": {
        "apiGroup": "rbac.authorization.k8s.io",
        "kind": "Role",
        "name": role,
    },
    "subjects": [
        {
            "kind": "ServiceAccount",
            "name": sa,
            "namespace": ns,
        },
    ],
}
rbac_api.create_namespaced_role_binding(namespace=ns, body=role_binding_manifest)
