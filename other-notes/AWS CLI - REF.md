# AWS CLI
## AWS CLI Credentials
[Other approach](https://dev.to/aws-builders/switch-between-aws-accounts-in-your-cli-like-never-before-l9b) on switching profiles


```bash
aws configure --profile new_profile_name
```
then follow the prompts

listing profiles
```bash
aws configure list-profiles
```

switching current profile
```bash
export AWS_PROFILE=new_profile_name
```

run a command as a specific profile
```bash
aws s3 ls --profile new_profile_name
```

check aws current profile
```bash
aws configure list
```

check current profile with aws cli
```bash
aws sts get-caller-identity
```

credentials get stored at:
`~/.aws/credentials`
And the file looks like
```toml
[default]
aws_access_key_id = YOUR_DEFAULT_ACCESS_KEY
aws_secret_access_key = YOUR_DEFAULT_SECRET_KEY

[personal]
aws_access_key_id = YOUR_PERSONAL_ACCESS_KEY
aws_secret_access_key = YOUR_PERSONAL_SECRET_KEY

[work]
aws_access_key_id = YOUR_WORK_ACCESS_KEY
aws_secret_access_key = YOUR_WORK_SECRET_KEY
```

region and output format get stored at:
`~/.aws/config`
```toml
[default]
region = us-west-2
output = json

[profile personal]
region = us-west-1
output = text

[profile work]
region = eu-west-1
output = json
```