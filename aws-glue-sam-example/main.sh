#!/usr/bin/env bash

echo "hello from bash"

whoami
uname -a
bash --version
aws --version
aws sts get-caller-identity

curl -O -L https://releases.hashicorp.com/terraform/0.11.2/terraform_1.1.4_linux_amd64.zip
unzip terraform_0.11.2_linux_amd64.zip
./terraform -version