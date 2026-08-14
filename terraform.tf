terraform {
  required_version = ">= 1.6.0"
}

variable "project_name" {
  type    = string
  default = "evo-tech-kubernetes-platform"
}

output "project_name" {
  value = var.project_name
}

# Provider-free foundation.
# A production deployment can add AWS, Azure,
# or Google Cloud infrastructure here.
