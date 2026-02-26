# Phase 2: Infrastructure as Code (Terraform)
## Project: Global Cloud Foundation (Day 15)

### 🎯 Objective
To transition from manual AWS management to **Infrastructure as Code (IaC)** by establishing a secure, versioned remote backend. This foundation ensures that all future security labs in this roadmap have a persistent "source of truth."

### 🛠️ Tools Used
* **Terraform:** Infrastructure orchestration.
* **AWS S3:** Remote state storage (Free Tier).
* **AWS CLI:** Programmatic access and authentication.
* **MacOS Terminal:** Local development environment.

### 🏗️ Architecture
1. **S3 Bucket:** Created with a unique random suffix to store `terraform.tfstate`.
2. **Versioning:** Enabled to allow recovery of previous infrastructure states if corruption occurs.
3. **Lifecycle Protection:** Configured `prevent_destroy` to ensure the core foundation isn't accidentally deleted during lab cleanups.

![Terraform Code Success](../assets/Day15-Terraform-resource.png)
![Bucket Creation](../assets/Day15-Terraform-bucket.png)

### 🚀 Key Learnings
* **State Management:** Understood that Terraform uses a "state file" to map code to real-world resources.
* **Backend Bootstrapping:** Learned the "Chicken and Egg" process of creating the storage bucket locally before migrating the state to the cloud.
* **Security Scoping:** Configured `.gitignore` to prevent sensitive infrastructure metadata from leaking to public version control.

---
*This project is part of my 180-Day Cloud Security Roadmap.*