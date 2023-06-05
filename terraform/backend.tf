# I AM GOING TO USE AN S3 BUCKET AS BACKEND
# IF YOU WANT TO FOLLOW THROUGH WITH THIS, YOU MUST ALSO HAVE AN S3 BUCKET AND DYNAMODB DATABASE

terraform {
  backend "s3" {
    bucket = "terraform-s3-backend-1001"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  profile = "terraform"
}