# 1. Create the IAM Group
resource "aws_iam_group" "auditors" {
  name = "Security_Auditors"
}

# 2. Create the "MFA Required" Policy
# This is a 'Deny-All-Without-MFA' guardrail
resource "aws_iam_policy" "mfa_enforcement" {
  name        = "EnforceMFA"
  description = "Denies all access if MFA is not enabled"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "DenyAllExceptListedIfNoMFA"
        Effect = "Deny"
        NotAction = [
          "iam:CreateVirtualMFADevice",
          "iam:EnableMFADevice",
          "iam:ListMFADevices",
          "iam:ListUsers",
          "iam:GetUser"
        ]
        Resource = "*"
        Condition = {
          BoolIfExists = {
            "aws:MultiFactorAuthPresent" = "false"
          }
        }
      }
    ]
  })
}

# 3. Attach the policy to the group
resource "aws_iam_group_policy_attachment" "mfa_attach" {
  group      = aws_iam_group.auditors.name
  policy_arn = aws_iam_policy.mfa_enforcement.arn
}