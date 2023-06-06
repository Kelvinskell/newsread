# Define policy document
data "aws_iam_policy_document" "assume_role" {
  statement {
        effect = "Allow"

        principals {
            type = "Service"
            identifiers = ["ecs-tasks.amazonaws.com"]
        }
        actions = ["sts:AssumeRole"]
    }
}

# Create task execution role
resource "aws_iam_role" "ecs_role" {
  name               = "NewsReadRole"
  path               = "/"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json

  inline_policy {
    name = "newsread_inline_policy_ecs_task_execution"
    policy = jsonencode(
      {
        "Version" : "2012-10-17",
        "Statement" : [
          {
            "Effect" : "Allow",
            "Action" : [
              "ecr:GetAuthorizationToken",
              "ecr:BatchCheckLayerAvailability",
              "ecr:GetDownloadUrlForLayer",
              "ecr:BatchGetImage",
              "logs:CreateLogStream",
              "logs:PutLogEvents"
            ],
            "Resource" : "*"
          }

        ]
      }
    )
  }
}