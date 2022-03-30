from kubernetes import client, config

namespace = "vshn-chaosbutton"
selector = "app=static-go"

config.load_kube_config()
api = client.CoreV1Api()

pods = api.list_namespaced_pod(namespace=namespace, label_selector=selector)

print(pods)
