terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0360c520857e3138f" # Example AMI ID for eu-north-1
  instance_type = "t2.medium"

  tags = {
    Name = "Jenkins Server"
  }
}
