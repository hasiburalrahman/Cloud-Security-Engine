#!/bin/bash
# Week 01: Basic Linux Hardening Script for AWS EC2 (Ubuntu)
# ---------------------------------------------------------

echo "[+] Starting Security Hardening"

# 1. Update and Upgrade System
echo "Updating system packages"
sudo apt-get update -y && sudo apt-get upgrade -y

# 2. Install Security Tools
echo "Installing UFW and Fail2Ban"
sudo apt-get install ufw fail2ban -y

# 3. Configure Firewall (UFW)
echo "Configuring Firewall"
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw --force enable

# 4. Automate Security Updates
echo "Enabling unattended-upgrades"
sudo apt-get install unattended-upgrades -y
sudo dpkg-reconfigure --priority=low unattended-upgrades

echo "Hardening Complete. Check /etc/ssh/sshd_config manually for root login status."

# 5. Create a Non-Root Admin User
NEW_USER="cloud-admin"
echo "Creating non-root user: $NEW_USER"

# Create user with a home directory and bash shell
sudo useradd -m -s /bin/bash "$NEW_USER"

# Add user to the 'sudo' group
sudo usermod -aG sudo "$NEW_USER"

# OPTIONAL: Copy your current SSH keys so you can log in as the new user
sudo mkdir -p /home/"$NEW_USER"/.ssh
sudo cp ~/.ssh/authorized_keys /home/"$NEW_USER"/.ssh/
sudo chown -R "$NEW_USER":"$NEW_USER" /home/"$NEW_USER"/.ssh
sudo chmod 700 /home/"$NEW_USER"/.ssh
sudo chmod 600 /home/"$NEW_USER"/.ssh/authorized_keys

echo "User $NEW_USER created and SSH keys copied."
