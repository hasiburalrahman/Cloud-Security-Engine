output "vpc_id" {
  description = "The ID of our Day 18 VPC"
  value       = aws_vpc.main_vpc.id
}

output "public_subnet_id" {
  description = "The ID of the Public (Front Porch) Subnet"
  value       = aws_subnet.public_subnet.id
}

output "private_subnet_id" {
  description = "The ID of the Private (Vault) Subnet"
  value       = aws_subnet.private_subnet.id
}

output "igw_id" {
  description = "The ID of our Internet Gateway"
  value       = aws_internet_gateway.igw.id
}