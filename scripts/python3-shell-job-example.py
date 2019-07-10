import datetime
import time
import boto3
import sys
import os
import importlib

print('sys.argv:\n{}\n\n'.format(sys.argv))
print('os.environ:\n{}\n\n'.format(os.environ))

# only run the following if running in aws glue environment (not availble locally)
if 'GLUE_INSTALLATION' in os.environ:
    aws_glue_utils = importlib.import_module('awsglue.utils')
    args = aws_glue_utils.getResolvedOptions(sys.argv,
                                             ['example_argument_0',
                                              'example_argument_1'])
    print('example_argument_0 is {}\n\n'.format(args['example_argument_0']))
    print('example_argument_1 is {}\n\n'.format(args['example_argument_1']))

ts = time.time()
timestamp_string = datetime.datetime.fromtimestamp(
    ts).strftime('%Y-%m-%d_%H.%M.%S')

s3 = boto3.client('s3')

bucket_name = 'aws-glue-playground-01'
bucket_directory = 'tmp'

print('__file__: {}'.format(__file__))

script_file_path = os.path.abspath(__file__)
print('script_file_path: {}'.format(script_file_path))

script_directory_path = os.path.dirname(script_file_path)
print('script_directory_path: {}'.format(script_directory_path))

local_file_path = os.path.abspath(
    '{}/{}-hello.txt'.format(script_directory_path, timestamp_string))
print('local_file_path: {}'.format(local_file_path))

local_file_name = os.path.basename(local_file_path)
print('local_file_name: {}'.format(local_file_name))

open(local_file_path, "w").write('Hello, world!')
key = '{}/{}'.format(bucket_directory, local_file_name)
s3.upload_file(local_file_path, bucket_name, key)
os.remove(local_file_path)
