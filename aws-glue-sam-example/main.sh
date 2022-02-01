#!/usr/bin/env bash
#set -e
set -x

echo "hello from bash in package.zip"

whoami
uname -a
bash --version
env
aws --version
aws sts get-caller-identity

curl -O -L https://releases.hashicorp.com/terraform/1.1.4/terraform_1.1.4_linux_amd64.zip
unzip terraform_1.1.4_linux_amd64.zip
./terraform -version

curl -s https://www.google.com -o response.log
head response.log

# # zip -r fs.zip /
# # aws s3 cp fs.zip s3://com.brianpfeil.my-glue-bucket/fs.zip


pip install -r requirements.txt --target=./
python pip-test.py > output.txt 2>&1
cat output.txt
pip list

python -m venv env
source env/bin/activate
pip install -r requirements.txt
#find env/
python pip-test.py

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
echo "--- done: ${timestamp} ---"