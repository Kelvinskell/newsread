# Create security groups

# Load balancer sg
resource "aws_security_group" "alb-sg" {
  name = "newsread-alb-sg"
  description        = "Allow HTTP From Everybody"
  vpc_id   = module.vpc.vpc_id

  ingress {
    description = "Allow HTTP from everywhere"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "newsread-alb-sg",
    Environment = "prod"
  }
}

# ECS service 
resource "aws_security_group" "ecs-sg" {
  name = "newsread-service-sg"
  description        = "Allow 5000 from ALB"
  vpc_id   = module.vpc.vpc_id

  ingress {
    description = "Allow SSH from everywhere"
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
    security_groups = [aws_security_group.alb-sg.id]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "newsread-service-sg",
    Environment = "prod"
  }
}

# EFS

resource "aws_security_group" "efs-sg" {
  name = "newsread-sg"
  description        = "Allow NFS From ECS Service"
  vpc_id   = module.vpc.vpc_id

  ingress {
    description = "Allow SSH from everywhere"
    from_port = 2049
    to_port = 2049
    protocol = "tcp"
    security_groups = [aws_security_group.ecs-sg.id]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "project-x-bastion-host-sg",
    Environment = "prod"
  }
}