provider "aws" {
  region = "us-east-1"
}

module "ec2-instance" {
    source              = "./modules/ec2-instance"
    ami_value           = "ami-0360c520857e3138f"
    instance_type_value = "t2.micro"
    subnet_id_value     = "subnet-0bf30c65af9d1c04f"
  
}

# Calling the S3 module
module "s3" {
  source = "./modules/s3"

  bucket_name         = "rajendra-demo-module-s3"
  versioning_enabled  = true
  encryption_algorithm = "AES256"

  tags = {
    Environment = "Dev"
    Owner       = "Rajendra"
  }
}