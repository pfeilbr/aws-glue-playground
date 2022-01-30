import os
import subprocess
 
# inspect the glue execution environment

# printing environment variables
print(os.environ)

result = subprocess.run(['aws', 'sts', 'get-caller-identity'], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))


for directory_path in os.environ['PATH'].split(":"):
    result = subprocess.run(['find', directory_path], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))


result = subprocess.run(['curl', 'https://www.google.com'], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))
