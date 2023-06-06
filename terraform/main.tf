# Create ECS Cluster and associated resources.

resource "aws_ecs_cluster" "cluster" {
  name = "newsread"
}

resource "aws_ecs_cluster_capacity_providers" "cluster" {
  cluster_name = aws_ecs_cluster.cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base                 = 0
    weight               = 100
    capacity_provider    = "FARGATE"
  }
}

resource "aws_ecs_service" "service" {
  name                              = "newsread-service"
  cluster                           = aws_ecs_cluster.cluster.id
  task_definition                   = aws_ecs_task_definition.tasks.arn
  desired_count                     = 1
  launch_type                       = "FARGATE"
  health_check_grace_period_seconds = 120
  force_new_deployment = true

  load_balancer {
    target_group_arn = aws_lb_target_group.tg.arn
    container_name   = "news"
    container_port   = 5000
  }

  network_configuration {
    subnets          = flatten([module.vpc.public_subnets[*]])
    security_groups  = [aws_security_group.ecs-sg.id]
    assign_public_ip = false
  }
}


# Create task definition
resource "aws_ecs_task_definition" "tasks" {
  family       = "newsread-tasks"
  network_mode = "awsvpc"
  skip_destroy = true
  requires_compatibilities = ["FARGATE"]
  cpu = 1024
  memory =2048
  execution_role_arn = aws_iam_role.ecs_role.arn
  container_definitions = jsonencode([
    {
      name      = "news"
      image     = "kelvinskell/newsread"
      cpu = 512
      essential = true
      logConfiguration: {
          "logDriver": "awslogs",
          "options": {
            "awslogs-group": "newsread",
            "awslogs-region": "us-east-1",
            "awslogs-stream-prefix": "newsread"
          }
      }
     environment: [
      { 
        name: "API_KEY"
        value: local.container_variables.API_KEY
      },
      {
        name: "SECRET_KEY"
        value: local.container_variables.SECRET_KEY
      },
      {
        name: "MYSQL_DB"
        value: local.container_variables.MYSQL_DB
      },
      {
        name: "MYSQL_HOST"
        value: local.container_variables.MYSQL_HOST
      },
      {
        name: "MYSQL_USER"
        value: local.container_variables.MYSQL_USER
      },
      {
        name: "DATABASE_PASSWORD"
        value: local.container_variables.DATABASE_PASSWORD
      },
      {
        name: "MYSQL_ROOT_PASSWORD"
        value: "local.container_variables.MYSQL_ROOT_PASSWORD"
      }
      ]
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
          protocol      = "http"
        }
      ]
    },

    {
      name      = "mysqldb"
      image     = "mysql:5.7"
      essential = true
      cpu = 512
      mountPoints: [
          {
            "sourceVolume": "newsread-vol",
            "containerPath": "/var/lib/mysql",
            "readOnly": false
          }
        ]
      logConfiguration: {
          "logDriver": "awslogs",
          "options": {
            "awslogs-group": "newsread",
            "awslogs-region": "us-east-1",
            "awslogs-stream-prefix": "newsread"
          }
      environment: [
        {
          name: "MYSQL_ROOT_PASSWORD"
          value: local.container_variables.MYSQL_ROOT_PASSWORD
        }
      ]
      portMappings = [
        {
          containerPort = 3306
          hostPort      = 3306
          protocol      = "tcp"
        }
      ]
    }
    }
  ])

  volume {
    name = "newsread-vol"

    efs_volume_configuration {
      file_system_id = aws_efs_file_system.efs.id
    }
  }
}

# Create Cloudwatch Log group
resource "aws_cloudwatch_log_group" "newsread" {
  name = "newsread"

  tags = {
    Environment = "prod"
  }
}