# Chaosbutton
![Chaosbutton in action](images/chaosbutton.jpg)
A large red button connected to a Raspbeery Pi bringing chaoos and mayhem to your kubernetes-based service by killing a pod by random

## How to create an OpenShift service account with a token that does not expire
```
oc create sa chaosbutton
oc describe sa chaosbutton | grep "Tokens:"
# get the secret name of the "Token"
oc describe secret chaosbutton-token-asd42 | grep "token:"
# copy the token and use below
```
## How to install on Raspberry Pi
```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo deb http://apt.kubernetes.io/ kubernetes-stretch main > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install git python3-pip kubectl
pip3 install RPi.GPIO kubernetes
git clone https://github.com/arska/chaosbutton.git
cd chaosbutton
kubectl config set-cluster appuio --server='https://console.appuio.ch'
kubectl config set-credentials appuio --token='kjhbmjhvbnbvnbv' # get a valid token e.g. above
kubectl config set-context appuio --cluster=appuio --user=appuio
kubectl config use-context appuio
python3 app.py
```
# To install the systemd service to start at boot
```
cp chaosbutton.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable chaosbutton.service
```

# How to I configure which pod gets killed?
See "namespace" and "selector" constants in app.py.
namespace: the Kubernetes namespace (orr OpenShift project) name you want to operate in
selector: is the label=value by which the pods to be killed are filtered and from which one is selected by random

# How do I build the Button and the Raspberry pi?
I ordered my button locally in Switzerland from https://www.bastelgarage.ch/buzzer-taster-rot because it was the cheapest delivered to me.
By default this application uses pin 15 (see "channel" in app.py) on the raspberry pi IO header because pin 17 next to it has +3.3v power. connecting these to pins using the button is detected in this application.


