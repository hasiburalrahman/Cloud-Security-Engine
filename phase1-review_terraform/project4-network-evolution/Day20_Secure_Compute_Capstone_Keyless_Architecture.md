# Day 20: Secure Compute Capstone - Keyless Architecture

**Date:** 2026  
**Phase:** Phase 1 — Secure Networking & Identity  
**Project:** Capstone

---

## Overview

This project is the final capstone for Phase 1 (Secure Networking & Identity). It deploys a high-performance ARM64 (Graviton) instance that is completely invisible to the public internet. By eliminating SSH (Port 22) and using AWS Systems Manager (SSM), a zero-trust management plane is established.

---

## Infrastructure Details

### 1. Secure Networking

Unlike standard configurations that open Port 22 for SSH, this VPC has zero inbound ports open.

- **Public Subnet:** Used only to allow the instance to reach the AWS SSM API.
- **Security Group:** Configured with an egress-only policy — no inbound rules.

![Security Group Screenshot](assets/Day20_Security_Group.png)

### 2. Identity-Based Access (SSM)

Instead of a static `.pem` key file, AWS Systems Manager (SSM) is used for access.

- **The Handshake:** The EC2 instance uses an IAM Instance Profile to prove its identity to AWS.
- **The Tunnel:** The connection is an outbound HTTPS (TLS 1.2) tunnel. The server initiates an outbound connection to AWS rather than accepting inbound connections.

![SSM Connection Screenshot](assets/Day20_SSM_Connection.png)

---

## Advanced Security: Why Graviton?

The `t4g.small` instance type was selected for three security reasons:

### 256-bit DRAM Encryption

The Graviton processor features dedicated hardware that encrypts all data moving between the CPU and RAM with AES-256.

- **Why it matters:** Even with physical access to the hardware, memory data would be unreadable.
- **Security Benefit:** Protection against cold boot attacks and side-channel memory snooping.

### IMDSv2 Enforcement

Amazon Linux 2023 enforces Instance Metadata Service Version 2 (IMDSv2). This requires a session-oriented token to access instance metadata, neutralizing SSRF (Server-Side Request Forgery) attacks.

---

## Lab Validation

After connecting via the browser-based SSM terminal, the environment was verified with:

- **Architecture Check:** `uname -m` → Expected output: `aarch64` (Graviton Silicon)
- **Identity Check:** `aws sts get-caller-identity` → Expected output: IAM Role `Day20-SSM-Role`

![Terminal Output Screenshot](assets/Day20_Terminal.png)

---

## Cost Optimization & Cleanup

- **T4 Standard Mode:** "Unlimited Mode" was disabled in Terraform to prevent CPU burst charges.
- **Automated Teardown:** `terraform destroy` was run to remove the public IP and instance, ensuring no ongoing charges.

![Terraform Destroy Screenshot](assets/Day20_Destroy.png)
