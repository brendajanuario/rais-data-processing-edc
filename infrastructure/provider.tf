provider "aws" {
  region = "us-east-2"
}

#centralize terraform state files
terraform {
  backend "s3" {
    bucket = "terraform-state-309083126863"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}
