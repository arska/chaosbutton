from kubernetes import client, config
from pprint import pprint
import random
import os
import RPi.GPIO as GPIO

namespace='appuio-salesdemo1'
selector='app=static-go'
channel=15 # pin 15 on the header, pin 17 next to it is 3.3v

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()

def chaos(channel):
    pods = v1.list_namespaced_pod(namespace=namespace, label_selector=selector)
    #for pod in pods.items:
    #    print("%s\t%s\t%s" % (pod.metadata.name,
    #                          pod.status.phase,
    #                          pod.spec.node_name))
    podname = random.choice(pods.items).metadata.name
    print("killing {0}".format(podname))
    v1.delete_namespaced_pod(podname, namespace, client.V1DeleteOptions(grace_period_seconds=0))

def my_callback(channel):
    print("called")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)

while True:
    pass

