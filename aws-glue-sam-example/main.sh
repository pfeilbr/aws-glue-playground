#!/usr/bin/env bash
set -x

echo "hello from bash"

whoami
uname -a
bash --version
env
aws --version
aws sts get-caller-identity

# curl -O -L https://releases.hashicorp.com/terraform/1.1.4/terraform_1.1.4_linux_amd64.zip
# unzip terraform_1.1.4_linux_amd64.zip
# ./terraform -version

# curl -s https://www.google.com -o response.log
# cat response.log

# # zip -r fs.zip /
# # aws s3 cp fs.zip s3://com.brianpfeil.my-glue-bucket/fs.zip
# timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
# echo "done ${timestamp}"