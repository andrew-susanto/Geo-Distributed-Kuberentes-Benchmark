#!/bin/bash
# run chmod +x ./prepdocker.sh
# run using sh -x ./prepdocker.sh
apt-get update
swapoff -a 
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt-get update
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo mkdir /etc/docker
cat <<EOF | sudo tee /etc/docker/daemon.json
{
"exec-opts": ["native.cgroupdriver=systemd"],
"log-driver": "json-file",
"log-opts": {
"max-size": "100m"
},
"storage-driver": "overlay2"
}
EOF

sudo systemctl enable docker
sudo systemctl daemon-reload
sudo systemctl restart docker

docker login --username xxx --password xxx
docker pull andrewsusanto/djangotracingapp:latest

cat > .env << EOF
DEBUG=False
DATABASE_POSTGRE=True
DATABASE_NAME=xxx
DATABASE_USER=xxx
DATABASE_PASSWORD=xxx
DATABASE_HOST=xxx
DATABASE_PORT=5432
SECRET_KEY=xxx
DJANGO_ALLOWED_HOSTS=xxx
DJANGO_CSRF_TRUSTED_ORIGIN=xxx
EOF

docker run --detach --env-file .env -p 0.0.0.0:80:80 andrewsusanto/djangotracingapp