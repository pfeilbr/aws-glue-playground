# aws-glue-playground

learn and experiment with [aws glue](https://aws.amazon.com/glue/)

## Steps to Run [`scripts/example-notebook-script-01.py`](scripts/example-notebook-script-01.py) in SageMaker notebook

see [`scripts/example-notebook-script-01.py`](scripts/example-notebook-script-01.py)

1. upload data.csv to S3
1. create glue crawler for data.csv which results in a table in glue database being created
    > you can verify by previewing the data in athena
1. create aws glue Dev Endpoint
    > no need to specify ssh key
1. create SageMaker notebook
    > SageMaker notebook works just like Zepplin notebook, but less setup steps.
1. open SageMaker notebook and past in code from [`scripts/example-notebook-script-01.py`](scripts/example-notebook-script-01.py)
