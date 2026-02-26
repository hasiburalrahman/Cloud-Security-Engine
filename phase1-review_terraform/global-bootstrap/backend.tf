terraform {
  backend "s3" {
    bucket  = "tf-state-roadmap-11cd2afd" 
    key     = "global/bootstrap/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}