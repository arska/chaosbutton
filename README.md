# Chaosbutton

A large red button connected to a Raspbeery Pi bringing chaoos and mayhem to your kubernetes-based service by killing a pod by random

## How to install on Raspberry Pi

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo deb http://apt.kubernetes.io/ kubernetes-stretch main > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install git python3-pip kubectl
pip3 install RPi.GPIO kubernetes
git clone https://github.com/arska/chaosbutton.git
cd chaosbutton
kubectl config set-cluster appuio --server='https://console.appuio.ch'
kubectl config set-credentials appuio --token='kjhbmjhvbnbvnbv' # get a valid token e.g. from the openshift web gui top right -> copy logiin command
kubectl config set-context appuio --cluster=appuio --user=appuio
kubectl config use-context appuio
python3 app.py

# To install the systemd service to start at boot
sudo systemctl daemon-reload
sudo systemctl enable sample.service
