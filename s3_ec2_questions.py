# S3
import boto3
import botocore
from botocore.client import Config

access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = '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'

# 1. Upload a file
s3 = boto3.client('s3',
                  aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)
# change the target file name, bucket name and save name

source_filename = 'S3_testfile1.txt'
bucket_name = 'jingwen-exercise'
source_savename = 'S3_testfile.txt'
# upload your file into s3 bucket
s3.upload_file(source_filename, bucket_name, source_savename)
print("finished")


# 2.Download a file
# solution 1
import boto3
import botocore
from botocore.client import Config

access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = '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'
s3 = boto3.client('s3',
                  aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)
bucket_name = 'jingwen-exercise' # replace your bucket name
source_filename = 'S3_script.txt' # replace your target file name on your bucket
source_savename = 'S3_download.txt' # save on your computer
s3.download_file(bucket_name, source_filename, source_savename)
print("finished")

# solution 2
import boto3
import botocore
access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = 'ROTmnhv2l03surTAWvwF6lsW5VmCkr2PaMPgTney'
BUCKET_NAME = 'jingwen-exercise' # replace with your bucket name
KEY = 'S3_script.txt' # replace with your object key
file_localname = 'S3_download.txt' # replace with your save name in local computer
s3 = boto3.resource('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key
                    )
try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, file_localname )
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

print("finished")


# 3. Download all files in a folder
import boto3
access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = 'ROTmnhv2l03surTAWvwF6lsW5VmCkr2PaMPgTney'
bucket_name = 'jingwen-exercise' # replace your bucket name

s3 = boto3.client('s3',
                  aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)

list=s3.list_objects(Bucket=bucket_name)['Contents']
for key in list:
    s3.download_file(bucket_name, key['Key'], key['Key'])

print("finished")

#EC2
# 1. create an instance
import logging
import boto3
from botocore.exceptions import ClientError

access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = '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'

# create a function to launch new instance
def create_ec2_instance(image_id, instance_type, keypair_name):
    ec2 = boto3.client('ec2',
                       aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key
                       )
    try:
        # launch new instance
        instance = ec2.run_instances(ImageId=image_id,
                                     InstanceType=instance_type,
                                     KeyName=keypair_name,
                                     MinCount=1,
                                     MaxCount=1,
                                     Monitoring={
                                         'Enabled': False
                                     }
                                     )
    except ClientError as e:
        logging.error(e)
        return None
    return instance['Instances'][0]

# Assign customized values
image_id = 'ami-0c64dd618a49aeee8' # choose AMI ID
instance_type = 't2.micro' # choose instance type
keypair_name = 'jingwenexercise' # choosing an exiting key pair name

# run function to launch intance
create_ec2_instance(image_id, instance_type, keypair_name)
print("finished")

# 2. terminate an instance
import boto3
access_key = 'AKIAIFZOGGUYIAPZQG2Q'
secret_key = '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'

ec2 = boto3.client('ec2',
                   aws_access_key_id=access_key,
                   aws_secret_access_key=secret_key
                   )
#get the detailed infomation of each instances
descri_instance = ec2.describe_instances()
print(descri_instance)
# stop an instance, replace the instance id since we already know each instance id from the result of descri_instance
ec2.stop_instances(InstanceIds=['i-080dd68bd0bc31d9a'])
# start an instance, replace the instance id
# ec2.start_instances(InstanceIds=['i-00217d4f640fbd4a4'])
ec2.terminate_instances(InstanceIds=['i-0592e8d5a3fc84c75'])
print("finished")
