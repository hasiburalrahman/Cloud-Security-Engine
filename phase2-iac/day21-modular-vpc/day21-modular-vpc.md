# Day 21: Modular VPC Architecture
## Phase 2: Infrastructure as Code (Terraform)

### 🎯 Objective
Transition from monolithic Terraform configurations to a professional, modular directory structure. This lab establishes a reusable networking foundation using input variables and output values to ensure scalability and "Dry" (Don't Repeat Yourself) code principles.

### 🏗️ Architecture Overview
This project deploys a secure, baseline AWS networking environment:
* **VPC:** Custom CIDR block (10.0.0.0/16) with DNS Hostnames enabled.
* **Internet Gateway:** Attached to the VPC for public egress/ingress.
* **Public Subnet:** A segmented network area with `map_public_ip_on_launch` enabled.
* **Route Table:** Configured with a default route (`0.0.0.0/0`) pointing to the IGW.



### 📂 Folder Structure
```text
day-21-modular-vpc/
├── providers.tf   # AWS Provider & Versioning
├── variables.tf   # Input definitions (Region, CIDR, Project Name)
├── main.tf        # Core resource logic (VPC, Subnet, IGW)
├── outputs.tf     # Exported resource IDs for downstream use
└── terraform.tfstate # Local state (Ignored by Git)