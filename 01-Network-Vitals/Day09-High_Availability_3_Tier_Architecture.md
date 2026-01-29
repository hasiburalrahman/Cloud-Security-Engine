# AWS Highly Available 3-Tier Architecture

**Date:** January 22, 2026 | **Level:** Intermediate / Advanced Networking

## 📌 Executive Summary

Successfully architected and deployed a secure, high-availability 3-tier application on AWS. The project focused on subnet isolation, load balancing, and secure administrative access using the EC2 Instance Connect Endpoint (EICE). Key achievements included resolving complex Linux service permissions and SELinux security contexts on Amazon Linux 2023.

---

## 🏗️ Architecture Design

The infrastructure is divided into three distinct logical layers across two Availability Zones (AZs) to ensure zero downtime.

| Layer | Component | Description |
|-------|-----------|-------------|
| **Web Tier** | Application Load Balancer (ALB) | Distributed across Public Subnets for internet-facing traffic |
| **Application Tier** | EC2 Instances in ASG | Private Subnets (no public IPs), managed by Auto Scaling Group |
| **Data Tier** | Amazon RDS MySQL | Isolated Private Subnets for database persistence |
| **Management** | EC2 Instance Connect Endpoint | "Bastionless" private SSH access without bastion hosts |

![VPC Architecture Diagram](./assets/day8_vpc_map.png)

---

## 🔐 Security & Networking Implementation

Implemented "Security Group Chaining" to restrict traffic flow using the principle of least privilege:

| Component | Allowed Traffic |
|-----------|-----------------|
| **ALB Security Group** | HTTP (80) from `0.0.0.0/0` |
| **App-Tier Security Group** | HTTP (80) only from ALB-SG |
| **Database Security Group** | MySQL (3306) only from App-Tier SG |
| **EICE Access** | SSH (22) only from EICE network range |

---

## 🛠️ Troubleshooting & Implementation

### 1. Network Handshake Verification

Validated connectivity between application and data tiers using Netcat. Even though instances are not publicly routable, they can still make updates through the NAT Gateway. 

![Network Test Netcat](./assets/day9-netcat-test.png)

**Steps:**
- Installed `netcat` utility on Application tier instances
- Verified database connectivity over private network 

```bash
nc -zv <rds-endpoint-url> 3306
```

![Network Database](./assets/day9-netcat-database.png)

### 2. Resolving File Permission Issues (404 Error)

**Problem:** Amazon Linux 2023 returned 404 errors despite files existing in `/var/www/html`

**Solutions Applied:**
- **Path Audit:** Used `namei -l` to verify directory traversal permissions
- **SELinux Reset:** Executed `restorecon -v` to restore proper security contexts for PHP-FPM
- **Service Override:** Created Systemd override to disable `ProtectHome`, enabling PHP service access to web root

![Permission Configuration](./assets/day9-permissions.png)

**Note:** Manual permission configuration required on additional ASG instances for consistency.

### 3. High Availability & Configuration Drift

**Problem:** ASG-launched instances had missing PHP scripts due to configuration drift

**Solution:** Updated Launch Template User Data to automate `dbtest.php` creation, ensuring every new instance launches in a ready state.

---

## ✅ Final Results

The fully functional architecture successfully:
- Routes requests through the Application Load Balancer
- Executes application logic on private EC2 nodes
- Retrieves data from isolated RDS MySQL instances

![Successful End-to-End Test](./assets/day9-SUCCESS.png)

---

## 🧹 Cost Optimization & Cleanup

All resources were decommissioned in the following order to optimize AWS spending:

1. Auto Scaling Group & Launch Templates (terminated instances)
2. NAT Gateways (stopped hourly billing)
3. Elastic IPs (released to avoid idle charges)
4. RDS Database (deleted without final snapshot)
5. Application Load Balancer & VPC (final cleanup)

---

## Key Learnings

✓ Multi-AZ architecture design for high availability  
✓ Security Group chaining for zero-trust networking  
✓ EC2 Instance Connect Endpoint for secure bastionless access  
✓ Linux service permissions and SELinux troubleshooting  
✓ Launch Template configuration for infrastructure consistency  
✓ AWS cost optimization strategies