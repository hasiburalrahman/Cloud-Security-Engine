Day 20: Secure Compute Capstone - The Keyless Architecture
🎯 Overview

This project represents the final capstone for Phase 1 (Secure Networking & Identity). We deployed a high-performance ARM64 (Graviton) instance that is completely invisible to the public internet. By eliminating SSH (Port 22) and using AWS Systems Manager (SSM), we have created a "Zero-Trust" management plane.
🏗 Infrastructure Details
1. Secure Networking (The "Fortress" Model)

Unlike standard tutorials that open Port 22 for SSH, this VPC has zero inbound ports open.

    Public Subnet: Used only to allow the instance to reach the AWS SSM API.

    Security Group: Configured with an "Egress-Only" policy.

    [PLACEHOLDER: Add your Security Group Screenshot here]
    Capture: Go to EC2 > Security Groups > Inbound Rules. It should show "No rules found".

2. Identity-Based Access (SSM Deep Dive)

Instead of a static .pem key (which can be stolen or lost), we use AWS Systems Manager (SSM).

    The Handshake: The EC2 instance uses an IAM Instance Profile (our "Passport") to prove its identity to AWS.

    The Tunnel: The connection is an outbound HTTPS (TLS 1.2) tunnel. This means the server "phones home" to AWS to ask if you want to talk to it.

    [PLACEHOLDER: Add your SSM Connection Screenshot here]
    Capture: Take a screenshot of the "Session Manager" tab inside the EC2 'Connect' menu before you hit the final connect button.

🔒 Advanced Security: Why Graviton?

We utilized the t4g.small instance type. In 2026, this is the gold standard for secure cloud compute for three reasons:
256-bit DRAM Encryption

The Graviton processor features dedicated hardware that encrypts every bit of data moving between the CPU and the RAM with AES-256.

    Why it matters: Even if a malicious actor physically accessed the AWS data center and "tapped" the motherboard memory traces, the data would be unreadable.

    Security Benefit: Provides protection against "Cold Boot" attacks and side-channel memory snooping.

IMDSv2 Enforcement

By using Amazon Linux 2023, we enforce the Instance Metadata Service Version 2. This requires a session-oriented "token" to access instance metadata, which effectively neutralizes SSRF (Server-Side Request Forgery) attacks—one of the most common ways cloud servers are breached.
💻 Lab Validation (Terminal Output)

Once logged into the server via the browser-based SSM terminal, we confirmed the environment with the following commands:

    Architecture Check: uname -m

        Expected Output: aarch64 (Confirms Graviton Silicon).

    Identity Check: aws sts get-caller-identity

        Expected Output: Shows the IAM Role Day20-SSM-Role.

    [PLACEHOLDER: Add your Terminal Output Screenshot here]
    Capture: A screenshot of the black SSM terminal window showing the results of both commands above.

💰 Cost Optimization & Cleanup

To adhere to the AWS Credit System constraints:

    T3/T4 Standard Mode: We explicitly disabled "Unlimited Mode" in Terraform to prevent CPU burst charges.

    Automated Teardown: Finalized the lab by running terraform destroy to remove the Public IP and Instance, ensuring no overnight charges.

    [PLACEHOLDER: Add your Terraform Destroy Screenshot here]
    Capture: Your Mac terminal showing "Destroy complete! Resources: 7 destroyed".