import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

companies = glueContext.create_dynamic_frame.from_catalog(database="us-mortgage-companies", table_name="us_mortgage_companies")
print "Count: ", companies.count()
companies.printSchema()


companies=companies.drop_fields(['address2', 'phone'])
companies.toDF().show()

states = companies.select_fields(['statecode'])

glueContext.write_dynamic_frame.from_options(frame = states, connection_type = "s3", connection_options = {"path": "s3://aws-glue-playground-01/target/us-mortgage-companies/states/"}, format = "csv")
states.filter(lambda dr: dr['statecode'] == 'PA').toDF().show()

states.toDF().write.parquet('s3://aws-glue-playground-01/target/us-mortgage-companies/states/parquet')