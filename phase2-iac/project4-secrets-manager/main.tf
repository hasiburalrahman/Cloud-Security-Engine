# --- 1. IDENTITY VERIFICATION ---
data "aws_caller_identity" "current" {}

# --- 2. THE SECURE VPC (NETWORKING) ---
resource "aws_vpc" "main_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "Day17-Secure-Network"
  }
}

# --- 3. THE SECRETS VAULT ---
resource "random_id" "suffix" {
  byte_length = 4
}

resource "random_password" "generated_pass" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

resource "aws_secretsmanager_secret_version" "pass_val" {
  secret_id     = aws_secretsmanager_secret.vpc_secret.id
  secret_string = random_password.generated_pass.result
}