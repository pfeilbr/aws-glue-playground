import os
import sys
import subprocess
import boto3
 
# inspect the glue execution environment

def run(cmd, verbose=True):
    result = subprocess.run(cmd.split, stdout=subprocess.PIPE)    
    if verbose:
        print(result.stdout.decode("utf-8"))

s3_client = boto3.client('s3')
s3_client.download_file('com.brianpfeil.my-glue-bucket', 'package.zip', 'package.zip')
result = subprocess.run(['unzip', 'package.zip'])
result = subprocess.run(['ls'])
result = subprocess.run(['pwd'])
#s3_client.download_file('com.brianpfeil.my-glue-bucket', 'main.sh', 'main.sh')
#print(open('main.sh').read())

#result = subprocess.run(['chmod', '+x', 'main.sh'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))

result = subprocess.run(['bash', 'main.sh'], check=True)
sys.exit(result.returncode)
#print(result.stdout.decode("utf-8"))

# for directory_path in os.environ['PATH'].split(":"):
#     result = subprocess.run(['find', directory_path])
#     #print(result.stdout.decode("utf-8"))





# result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))

# result = subprocess.run(['bash', '--version'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))

# result = subprocess.run(['aws', '--version'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))


# printing environment variables
# print(os.environ)

# result = subprocess.run(['aws', '--version'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))


# result = subprocess.run(['aws', 'sts', 'get-caller-identity'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))

# result = subprocess.run(['find', '.'], stdout=subprocess.PIPE)
# print(result.stdout.decode("utf-8"))

# result = subprocess.run(['curl', '-s', 'https://www.google.com', '-o', 'response.log'], stdout=subprocess.PIPE)
# result = subprocess.run(['cat', 'response.log'], stdout=subprocess.PIPE)
# print(result.stdout)

