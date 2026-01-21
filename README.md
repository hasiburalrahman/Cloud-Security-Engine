# Cloud Security Engine: 180-Day Transformation

> **From Vulnerability Management to Cloud Security Architecture**

## Overview

This repository documents a structured 180-day learning journey to transition from traditional vulnerability and threat management into cloud security engineering. It serves as a portfolio of technical work focused on Infrastructure as Code (IaC), security automation, and defensive cloud architecture.

**Core Philosophy:** In modern cloud environments, identifying vulnerabilities is straightforward—remediating them at scale is where value is created. This project focuses on building self-healing cloud infrastructure through automated guardrails that prevent misconfigurations before they occur.

---

## Technology Stack

- **Cloud Platforms:** AWS (primary), Azure (secondary)
- **Infrastructure as Code:** Terraform, OpenTofu, Packer
- **Automation & Scripting:** Python (Boto3/Azure SDK), Bash, GitHub Actions
- **Security Standards:** NIST Cybersecurity Framework 2.0, OWASP Top 10, Zero Trust Architecture
- **Compliance Frameworks:** CIS Benchmarks, SOC2 requirements

---

## Learning Roadmap

| Phase | Duration | Focus Area | Status |
|-------|----------|-----------|--------|
| Month 1 | Weeks 1–4 | Cloud Architecture & Networking | In Progress |
| Month 2 | Weeks 5–8 | Infrastructure as Code (Terraform) | Pending |
| Month 3 | Weeks 9–12 | Identity & Access Management | Pending |
| Month 4 | Weeks 13–16 | Detection & Auto-Remediation | Pending |
| Month 5 | Weeks 17–20 | AI Security & LLM Guardrails | Pending |
| Month 6 | Weeks 21–24 | Certification & Capstone Project | Pending |

---

## Project Structure

### [Week 01: The Secure Foundation](./Week-01/)

**Objectives:**
- Design a multi-tier VPC with public/private subnet isolation
- Implement least-privilege IAM roles and policies
- Configure cost monitoring and alerting mechanisms

**Deliverables:**
- VPC architecture documentation
- Hardening scripts and configuration templates
- IAM policy templates following Zero Trust principles
- Cost optimization configurations

---

## Security & Compliance

This repository is intended for educational purposes. All sensitive data, including credentials and API keys, are protected through `.gitignore` exclusions and secret management tools. No production secrets, tokens, or sensitive information are committed to this codebase.

---

## License

This project is licensed under the MIT License—see [LICENSE](./LICENSE) file for details.
