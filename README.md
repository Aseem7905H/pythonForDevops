🚀 AWS Automation Project – S3 Backup & EC2 Deployment via Python and Terraform
🧾 Overview

This project demonstrates end-to-end AWS automation using Python (boto3) and Terraform.
It performs the following tasks automatically:

Lists AWS S3 Buckets and EC2 Instances

Creates local backups using Python’s shutil module

Uploads backup archives to AWS S3

Deploys a new EC2 instance using Terraform

This script is ideal for DevOps automation, cloud backup management, and infrastructure provisioning workflows.

🏗️ Project Architecture
+--------------------------+
|   Local Environment      |
|--------------------------|
| Python Script:           |
| - Backup local files     |
| - Upload to S3           |
| - Trigger Terraform      |
+--------------------------+
            |
            v
+--------------------------+
|       AWS Cloud          |
|--------------------------|
| S3  → Backup Storage     |
| EC2 → Created via TF     |
+--------------------------+

⚙️ Technologies Used

Python 3.x

boto3 (AWS SDK for Python)

Terraform (for Infrastructure as Code)

AWS S3 (Storage for backups)

AWS EC2 (Compute instance deployment)

📂 Project Structure
aws-automation/
│
├── backup_script.py          # Handles local backup and S3 upload
├── terraform_script.py       # Runs Terraform commands via subprocess
├── main.py                   # Integrates all automation tasks
├── terraform/
│   ├── main.tf               # Terraform EC2 instance configuration
│
└── README.md                 # Project documentation

🔧 Setup Instructions
1️⃣ Prerequisites

AWS account with access to S3 and EC2

Installed and configured:

Python 3.x

AWS CLI
 (run aws configure)

Terraform

2️⃣ Python Dependencies

Install required Python modules:

pip install boto3

🧠 Step-by-Step Workflow
🔹 1. List S3 Buckets and EC2 Instances
import boto3

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

for bucket in s3.buckets.all():
    print(bucket.name)

for instance in ec2.instances.all():
    print(instance.id)

🔹 2. Create a Local Backup

The following function compresses your source folder into a .tar.gz backup file.

import shutil, datetime, os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f'backup_{today}.tar.gz')
    shutil.make_archive(backup_file_name.replace('.tar.gz',''), 'gztar', source)


Example:

source = "/home/aseem-hasan/python/devopsMasterclass"
destination = "/home/aseem-hasan/python/devopsPYworkshop"
backup_files(source, destination)

🔹 3. Upload Backup to AWS S3
def upload_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully!")


Example:

upload_backup(s3, "/path/to/backup.tar.gz", "demo-for-workshop", "my_backup.tar.gz")

🔹 4. Automate EC2 Instance Creation with Terraform

The script executes Terraform commands directly from Python using the subprocess module.

import subprocess

def run_terraform():
    subprocess.run(["terraform", "init"], check=True)
    subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
    print("EC2 Instance created successfully!")


Terraform configuration (main.tf):

provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform-EC2-Instance"
  }
}

🧩 Complete Automation Flow

Run the Python script

It takes a local backup

Uploads it to your AWS S3 bucket

Invokes Terraform to provision a new EC2 instance

Verifies successful deployment

🛡️ Security Recommendations

Use AWS IAM roles or credentials stored in AWS CLI profiles.

Avoid hardcoding access keys in code.

Encrypt sensitive files before uploading to S3.

📘 Example Output
Existing S3 Buckets:
- demo-for-workshop
- orignal-image-bucket

EC2 Instances:
- i-0ab123c456def7890

Backup created: backup_2025-02-23.tar.gz  
Backup uploaded successfully!  
Terraform initialized...  
EC2 Instance created successfully!

🧰 Future Improvements

Automate periodic backups using CRON or AWS Lambda

Add SNS notification after successful deployment

Implement error handling & logging for AWS API calls

Store backup metadata in DynamoDB

🧑‍💻 Author

Aseem Hasan
DevOps & Cloud Enthusiast | Python & Terraform Automation
