# Use data source to reference secrets manager secret
data "aws_secretsmanager_secret_version" "vars" {
    secret_id = "newsread7"
}

# Use locals to grab the decrypted key from secret manager
locals {
    container_variables = jsondecode(
        data.aws_secretsmanager_secret_version.vars.secret_string
    )
}