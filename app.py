from kubernetes import client, config
from pprint import pprint
import random
import os
import RPi.GPIO as GPIO
import logging
import threading

LOGFORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOGFORMAT)

namespace='appuio-salesdemo1'
selector='app=static-go'
channel=15 # pin 15 on the header, pin 17 next to it is 3.3v
maxparallel=5

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
    logging.debug("killing {0}".format(podname))
    v1.delete_namespaced_pod(podname, namespace, client.V1DeleteOptions(grace_period_seconds=0))

def newthread(channel):
    if threading.active_count() < maxparallel:
        logging.info("starting new thread")
        threading.Thread(target=chaos, args=(channel,)).start()
    else:
        logging.info("not starting new thread since {1} already more than {0} running".format(maxparallel, threading.active_count()))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(channel, GPIO.RISING, callback=newthread, bouncetime=200)

while True:
    pass

