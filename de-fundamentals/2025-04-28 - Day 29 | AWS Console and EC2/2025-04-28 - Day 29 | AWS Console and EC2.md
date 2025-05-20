# 2025-05-06 - Day 34 | Lambda
## 
- default execution role
    - permission to upload logs to CloudWatch
    - permission to read/write to s3
    - permission for s3 to fire events when files are uploaded
    - permission for lambda to receive events


### notes to self
- add .tfstate to s3 state file
- lambda name as a variable to refer to programatically
- don't forget to allow a lambda to be a lambda 
```terraform
data "aws_iam_policy_document" "assume_role" {
statement {
    effect = "Allow"

    principals {
    type        = "Service"
    identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
}
}

resource "aws_iam_role" "iam_for_lambda" {
name               = "iam_for_lambda"
assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
```

`aws_iam_policy_document` is the small print (the whole law in that policy)
`aws_iam_policy` is the actual visa that says 'an instance of this policy'
`aws_iam_role_policy_attachment` is when we actually stamp the user's passport with tha policy

`assume_role_policy` in an `aws_iam_role` is the user's page that says they are who they are 

when adding roles for example for s3, make sure you add 

- assume role policy
- 