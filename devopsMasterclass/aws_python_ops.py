import boto3

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

for bucket in s3.buckets.all():
    print(bucket)

print("ec2") 
for ins in ec2.instances.all():
    print(ins)

s3.Bucket("orignal-image-bucket").download_file("Screenshot From 2025-02-18 23-22-27.png","demo.png")

