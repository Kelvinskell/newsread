# Define policy document
data "aws_iam_policy_document" "assume_role" {
    statement {
        effect = "Allow"

        principals {
            type = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }
        actions = ["sts:AssumeRole"]
    }
}

 # Create task execution role
resource "aws_iam_role" "server_role" {
    name = "PROJECTXROLE"
    path = "/"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json

    inline_policy {
        name = "project_x_inline_policy_ec2_read_access"
        policy = jsonencode(
            {
        "Version": "2012-10-17",
        "Statement":  [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ])
}
    }