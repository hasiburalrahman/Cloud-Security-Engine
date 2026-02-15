output "vpc_id" {
  value = aws_vpc.main_vpc.id
}

output "secret_arn" {
  value = aws_secretsmanager_secret.vpc_secret.arn
}