provider "aws" {
  region = "ap-south-1" # Change as needed
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Change to your region's AMI ID
  instance_type = "t2.micro"
  tags = {
    Name = "Terraform-EC2-Instance"
  }
}
