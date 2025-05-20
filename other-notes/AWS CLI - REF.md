# AWS CLI
## AWS CLI Credentials
```bash
aws configure --profile new_profile_name
```
then follow the prompts

listing profiles
```bash
aws configure list-profiles
```

changing default profile
```bash
export AWS_PROFILE=profile_name
```

run a command as a profile
```bash
aws s3 ls --profile profile_name
```

check aws current profile
```bash
aws configure list
```