# create Application Load Balancer
resource "aws_lb" "alb" {
  name                       = "newsread-alb"
  internal                   = false
  load_balancer_type         = "application"
  security_groups            = [aws_security_group.alb-sg.id]
  subnets                    = flatten([module.vpc.public_subnets[*]])
  enable_deletion_protection = false

  tags = {
    Environment = "prod"
  }
}

# Create target group
resource "aws_lb_target_group" "tg" {
  name        = "tf-example-lb-tg"
  port        = 5000
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = module.vpc.vpc_id
  health_check {
    enabled             = true
    healthy_threshold   = 2
    interval            = 60
    matcher             = "200-299"
    path                = "/"
    port                = 5000
    protocol            = "HTTP"
    timeout             = 10
    unhealthy_threshold = 4
  }
}

# Create listener
resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.alb.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type = "forward"
    forward {
      target_group {
        arn = aws_lb_target_group.tg.arn
      }
      stickiness {
        enabled  = true
        duration = 120
      }
    }
  }
  tags = {
    Name        = "newsread-alb-listener"
    Environment = "prod"
  }
}

# Print DNS Name
output "dns_name" {
  value = aws_lb.alb.dns_name
}