# 🛡️ Cloud Security Engine

> **Bridging the gap between finding vulnerabilities and building automated defenses.**

## 📖 Overview
This repository documents a structured 180-day portfolio of hands-on cloud security labs focused on **Infrastructure as Code (IaC)**, **serverless security**, and **defensive cloud architecture**.

**Core Philosophy:** Security is not just a checkbox; it is a scalable, automated architecture. This project focuses on "Security-by-Design," moving beyond manual auditing to building self-healing systems.

---

## 📈 Learning Roadmap

| Phase | Duration | Focus Area | Status 
|-------|----------|-----------|--------|
| **Phase 1** | **Weeks 1–4** | **Secure Networking & Serverless Identity** | **Active (Day 13)** |
| Phase 2 | Weeks 5–8 | Infrastructure as Code (Terraform) | Pending |
| Phase 3 | Weeks 9–12 | Threat Detection & Auto-Remediation | Pending |
| Phase 4 | Weeks 13–16 | DevSecOps & Pipeline Security | Pending |
| Phase 5 | Weeks 17–20 | AI Security & Governance | Pending |
| Phase 6 | Weeks 21–24 | Capstone & Cloud Security Specialization | Pending |

---

## 🚀 Completed Labs

### 🌐 Phase 1: Infrastructure & Networking Foundation
* **Day 01-02:** **Setup & Hardening / VPC Architecture**
    * Designed a multi-tier VPC with public/private subnet isolation and Route Table management.
* **Day 03-05:** **Compute Hardening & Zero Trust**
    * Implemented EC2 security hardening, vulnerability assessments, and Identity Remediation.
* **Day 06-07:** **High Availability & Connectivity**
    * Configured NAT Gateways for egress-only connectivity and built a Multi-AZ web architecture.
* **Day 08-09:** **Resilient Architecture**
    * Deployed a **Highly Available 3-Tier Architecture** using **Application Load Balancers (ALB)** and **Auto Scaling Groups (ASG)** to ensure self-healing capabilities.



### 🤖 Phase 2: Serverless AI & Identity
* **Day 10-11:** **AI Image Intelligence**
    * Built a serverless system using **AWS Lambda** and **Amazon Rekognition** for automated facial comparison.
* **Day 12-13:** **The Identity Vault: Serverless Biometric Authentication**
    * Engineered **Least-Privilege IAM Policies** to restrict service-to-service communication.
    * Integrated **Amazon DynamoDB** to maintain an automated audit trail of all access attempts (Success/Failure).



---

## 🔒 Security Principles Applied
1.  **Least Privilege:** All IAM roles are restricted to specific Resource ARNs; zero "Full Access" or "Admin" policies used.
2.  **Attack Surface Reduction:** Using Private Subnets and NAT Gateways to prevent direct internet exposure.
3.  **Auditability:** 100% of identity verification attempts are logged in a NoSQL database for incident response.

---

## � About
**Hasibur Rahman** | Cloud Security Engineer | CompTIA Security+ Certified

Specialized in cloud architecture, infrastructure hardening, serverless security, and biometric authentication systems.

---
*This repository is updated daily/weekly as part of the #CloudSecurity180 challenge.*