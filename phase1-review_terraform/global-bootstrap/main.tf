resource "random_id" "t_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "terraform_state" {
  bucket = "tf-state-roadmap-${random_id.t_suffix.hex}"

  lifecycle {
    prevent_destroy = true 
  }
}

resource "aws_s3_bucket_versioning" "enabled" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}
