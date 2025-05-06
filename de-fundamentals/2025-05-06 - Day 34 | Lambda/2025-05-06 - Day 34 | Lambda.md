# 2025-05-02 - Day 33 | More Terraform

### Terraform remote state
[Backend block configuration overview](https://developer.hashicorp.com/terraform/language/backend)
[Applied to S3](https://developer.hashicorp.com/terraform/language/backend/s3)
- we want to store state remotely in a bucket outside of the terraform infrastructure
```terraform
terraform {
  backend "s3" {
    bucket = "example-bucket"
    key    = "path/to/state"
    region = "eu-west-2"
  }
}
```

### Permissions
- A user can have a role
- A role is made of policies
- trust policy as well as policies

### Modules
