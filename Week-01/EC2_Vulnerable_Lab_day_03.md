# Lab Day 3: EC2 Security Hardening & Vulnerability Assessment

## 📋 Objective

To provision a Linux-based cloud asset, simulate unauthorized access attempts, and perform an internal security audit to establish a baseline hardening score. This lab demonstrates the identification, remediation, and validation of security misconfigurations in AWS EC2 instances.

---

## 🏗️ Infrastructure Deployment

### Environment Specifications

| Component | Specification |
| :--- | :--- |
| **Platform** | AWS EC2 |
| **Operating System** | Ubuntu 24.04 LTS |
| **Storage** | 8 GiB gp3 (Encrypted at rest) |
| **Initial Security State** | Port 22 open to `0.0.0.0/0` (Highly Vulnerable) |

### Initial Configuration

The EC2 instance was provisioned with default security group settings, exposing SSH (port 22) to the entire internet (`0.0.0.0/0`), creating a significant security risk.

---

## 🔍 Threat Simulation & Log Analysis

### Attack Simulation

To demonstrate the vulnerability, an unauthorized SSH login attempt was simulated using an invalid username.

### Log Monitoring

System authentication logs were monitored in real-time using:

```bash
tail -f /var/log/auth.log
```

### Observed Log Evidence

```
sshd[13162]: Invalid user hacker-bot from [Source_IP]
sshd[13162]: Connection reset by invalid user hacker-bot [preauth]
```

### Key Finding

**Security Impact:** The server successfully logged the attempt, but the open firewall allowed the connection to reach the SSH daemon, consuming system resources and increasing the attack surface. This demonstrates that:

- Attackers can probe the system without being blocked at the network layer
- System resources are consumed processing invalid connection attempts
- Log files grow unnecessarily from failed authentication attempts
- The system is exposed to brute-force attacks from any IP address

---

## 🛠️ Remediation (Hardening)

### Perimeter Hardening Strategy

To mitigate the risk of brute-force attacks and unauthorized scanning, **Perimeter Hardening** was implemented at the AWS Security Group level.

### Remediation Steps

1. **Modified AWS Security Group Inbound Rules**
   - **Before:** SSH (Port 22) source: `0.0.0.0/0`
   - **After:** SSH (Port 22) source: `My IP` (specific IP address)

2. **Implementation Method**
   - Accessed AWS EC2 Console → Security Groups
   - Edited inbound rules for the associated security group
   - Removed the permissive `0.0.0.0/0` rule
   - Added a restricted rule allowing only the authorized IP address

### Verification

**Result:** Subsequent connection attempts from unauthorized IPs were dropped by the AWS Network Fabric at the security group level, resulting in:
- ✅ No new log entries on the host for unauthorized attempts
- ✅ Reduced attack surface (99.99% reduction in accessible IPs)
- ✅ Protection against brute-force attacks
- ✅ Lower system resource consumption

---

## 🔬 Internal Vulnerability Audit

### Security Audit Tool

Utilized **Lynis**, an open-source security auditing tool, to perform a comprehensive internal scan of the operating system.

### Initial Hardening Index

**Score: 63/100**

### Key Findings

| Category | Finding | Impact |
| :--- | :--- | :--- |
| **Firewall** | Internal UFW was inactive | Defense-in-depth opportunity missed |
| **Malware Protection** | No malware scanner (ClamAV) detected | No automated threat detection |
| **Compliance** | SSH banner not implemented | Missing security notice |
| **Kernel Hardening** | Suggestions for additional hardening | Potential for improved security posture |

### Audit Insights

The audit revealed opportunities for **defense-in-depth** security:
- **Network Layer:** Security group hardening (✅ Completed)
- **Host Layer:** UFW firewall inactive (⚠️ Opportunity for improvement)
- **Application Layer:** SSH configuration could be further hardened
- **Monitoring:** Malware scanning not implemented

---

## ✅ Validation

### Post-Remediation Verification

#### 1. Network-Level Protection

- **Test:** Attempted SSH connection from unauthorized IP
- **Result:** Connection dropped at AWS Security Group level
- **Evidence:** No entries in `/var/log/auth.log` for unauthorized attempts

#### 2. Authorized Access Verification

- **Test:** SSH connection from authorized IP address
- **Result:** Successful connection maintained
- **Evidence:** Legitimate access preserved

#### 3. Security Group Configuration

```bash
# Verify security group rules
aws ec2 describe-security-groups \
    --group-ids <SECURITY_GROUP_ID> \
    --query 'SecurityGroups[0].IpPermissions[*].[IpProtocol,FromPort,ToPort,IpRanges[0].CidrIp]' \
    --output table
```

**Expected Output:**
```
| tcp  | 22  | 22  | <AUTHORIZED_IP>/32 |
```

### Validation Results

- ✅ **Perimeter Security:** SSH access restricted to authorized IP
- ✅ **Attack Surface Reduction:** Unauthorized connection attempts blocked at network layer
- ✅ **Log Reduction:** No unauthorized attempts reaching the host
- ✅ **Service Availability:** Legitimate access maintained

---

## 📊 Metrics & Impact

| Metric | Before | After | Improvement |
| :--- | :--- | :--- | :--- |
| **SSH Attack Surface** | Global (`0.0.0.0/0`) | Single IP (`/32`) | 99.99% reduction |
| **Unauthorized Log Entries** | All attempts logged | Blocked at network layer | 100% reduction |
| **Brute-Force Vulnerability** | High | Low | Significant reduction |
| **Hardening Index** | 63/100 | Baseline established | Foundation for improvement |

---

## 🧹 Conclusion & Resource Hygiene

### Lab Completion

The lab was concluded by performing proper **resource hygiene**:

1. **Terminated EC2 Instance**
   - Ensured no "zombie assets" remain in the account
   - Prevented unnecessary billing charges

2. **Deleted Security Group**
   - Removed the custom security group created for this lab
   - Maintained clean AWS account state

### Key Takeaways

1. **Network-Level Controls:** Security groups provide the first line of defense and should follow the Principle of Least Privilege
2. **Defense in Depth:** Multiple layers (Security Groups, UFW, SSH config) provide comprehensive protection
3. **Logging & Monitoring:** Real-time log monitoring helps identify attack patterns
4. **Automated Auditing:** Tools like Lynis provide baseline security assessments
5. **Resource Management:** Proper cleanup prevents cost accumulation and security risks

---

## 🔗 Related Resources

- [AWS Security Groups Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)
- [Lynis Security Auditing Tool](https://cisofy.com/lynis/)
- [CIS Ubuntu Linux 24.04 Benchmark](https://www.cisecurity.org/benchmark/ubuntu_linux)

---

## 📝 Lab Metadata

- **Lab Date:** Day 3
- **Environment:** AWS EC2 (Ubuntu 24.04 LTS)
- **Region:** [N.Virgina]
- **Tools Used:** AWS Console, Lynis, SSH, tail
- **Hardening Index:** 63/100 (Baseline)

---

**Next Steps:** Continue hardening with host-level firewall (UFW), SSH configuration improvements, and malware scanning implementation.
