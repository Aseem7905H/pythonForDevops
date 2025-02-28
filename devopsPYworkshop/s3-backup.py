""" This script takes a backup from local to AWS S3 """

import boto3

# Initialize S3 resource
s3 = boto3.resource("s3")  # Fixed typo

def show_buckets(s3):
    """ List all S3 buckets """
    print("\nExisting S3 Buckets:")
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region="ap-south-1"):
    """ Create an S3 bucket in the specified region """
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print(f"S3 bucket '{bucket_name}' created successfully!")

# Set your bucket name
bucket_name = "demo-for-workshop"

# Create a new bucket
#create_bucket(s3, bucket_name)

# Show available buckets
#show_buckets(s3)

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name,Body=data)
    print("backup uploaded successfuly")

file_name = "/home/aseem-hasan/python/devopsPYworkshop/backup_2025-02-23.tar.gz"
upload_backup(s3,file_name , bucket_name ,"my_backup.tar.gz")
             