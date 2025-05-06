# 2025-05-01 - Day 32 | Terraform - Notes
## Terraform
- Infrastructure as code
- Declarative DSL (Domain Specific Language)
- Version Control
- testing
- state management
- declarative - order of writing is not important Terraform largely understands dependencies

### Configuring terraform
```terraform
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-west-2"
}
```

`terraform ini` from inside the `terraform` folder
`terraform plan` check the files to see if they are in the right format (won't make sure they work)
`terraform apply` 
`terraform destroy` remove everything that you created


## `terraform.lock` is a sensitive document, it should not be commited!!!
Add to your `.gitignore` file
```bash
# Terraform lock file
**/.terraform.lock.hcl

# Local .terraform directories
**/.terraform/*
```

##
Creating SSH Key Pairs
```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/my-key
```

## Data vs Resource
- Data already exists
- Resource is something we provision

## Terraform Types of Objects:
- `terraform`
- `variable`
- `provider`
- `resource` 
- `module` 


`ssh -i "/Users/theorib/.ssh/my-key" ubuntu@ec2-18-133-220-78.eu-west-2.compute.amazonaws.com`

## Important info on EC2 user_data
- User data shell scripts must start with a **shebang**, e.g: `#!/bin/bash`
- Scripts entered as user data are run as the **root user**, so do not use the sudo command
- any files you create will be owned by the **root user**; if you need a non-root user to have file access, you should modify the **permissions** accordingly
Sources: [user_data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-shell-scripts), [cloud-init User-data formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html#mime-multi-part-archive)


## Terraform Variable files
[.tfvars files](https://developer.hashicorp.com/terraform/language/values/variables#variable-definitions-tfvars-files)

## Cloud Init Resources
[cloudinit_config (Data Source)](https://registry.terraform.io/providers/hashicorp/cloudinit/latest/docs/data-sources/config)