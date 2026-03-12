# Day 16: Remote State Migration & IAM MFA Governance

## Overview

Infrastructure as Code (IaC) is only as secure as the state it manages. This lab transitions from a local state model to a professional **Remote Backend** architecture, and deploys an IAM Governance policy to enforce **Multi-Factor Authentication (MFA)** across the environment.

---

## The Architecture: Remote Backend & MFA Gatekeeper

### 1. The Remote Backend (S3 + Versioning)

A remote state backend was established in the cloud. By moving the `terraform.tfstate` file from a local machine to an S3 bucket, the following was achieved:

| Benefit | Description |
|---|---|
| **Durability** | S3 Versioning ensures that if a state file is corrupted, we can perform a "Point-in-Time" recovery. |
| **Security** | State files often contain sensitive metadata. We applied **AES-256 Server-Side Encryption** to protect data at rest. |
| **Persistence** | The "Bootstrap" bucket acts as the permanent anchor for all future 180 days of infrastructure. |

### 2. MFA Governance Policy (Zero Trust)

An IAM policy was authored to prevent unauthorized access even if a password is compromised.

- **Logic:** An `Explicit Deny` that triggers if the `aws:MultiFactorAuthPresent` condition is `false`.
- **Self-Service Loop:** Included specific `Allow` statements for IAM MFA actions, ensuring users can set up their own devices without needing an admin to unlock them.

---

## Implementation

### Step 1: The State Migration

The `backend.tf` was configured to point to the "Global Bootstrap" bucket created on Day 15.

```bash
terraform init -migrate-state
```

**Technical Outcome:** Terraform initialized the S3 backend, compared the local state to the cloud, and uploaded the "memory" of the bootstrap bucket into the bucket itself.

> **S3 State Objects after migration:**

![S3 State Objects](../assets/Day16-Objects.png)

---

### Step 2: Coding the MFA Guardrail

The `main.tf` in the `project3-mfa-governance` folder defined the following:

- **IAM Group:** `Security_Auditors` — to demonstrate group-based access control.
- **IAM Policy:** A JSON-encoded document enforcing MFA.

> **Terraform Build Output:**

![MFA Build Output](../assets/Day16-MFA_Build.png)

> **MFA Policy Document in AWS Console:**

![MFA Policy](../assets/Day16-MFA_Policy.png)

---

## Security Audit & Verification

Verification was performed using the **AWS IAM Policy Simulator**:

| Parameter | Value |
|---|---|
| **Context** | Simulated a user within the `Security_Auditors` group |
| **Action** | Attempted `s3:ListAllMyBuckets` |
| **Variable** | Set `aws:MultiFactorAuthPresent` to `false` |
| **Result** | Denied |

**Success Criteria:** The policy successfully blocked access, proving the "Gatekeeper" logic works.

> **Policy Simulation Result:**

![Policy Simulation](../assets/Day16-Policy_Simulation.png)

---

## Remote State: Why the Bootstrap Bucket?

Even though we destroy the lab projects (like the MFA group) every night to stay within the AWS Free Tier, the **Bootstrap Bucket remains**. It is the "Flight Recorder" of the account.

- **Ancestry** — It tracks the full history of the project.
- **Zombie Prevention** — It prevents orphaned AWS resources with no state file to manage them.
- **Locking** — It provides the locking mechanism required for professional cloud teams.

---

## Cleanup Log

| Action | Detail |
|---|---|
| **Resource Destruction** | `terraform destroy` executed in `project3-mfa-governance` |
| **State Integrity** | Confirmed `global/bootstrap/terraform.tfstate` remains in S3 |
| **Cost Impact** | **$0.00** — All resources utilized were Free Tier eligible |
