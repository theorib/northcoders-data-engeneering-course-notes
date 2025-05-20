# Overview of Topics Covered in each sprint

## de-cats-rare-treasures
### PG-8000
- `pg8000.native`
    - `literal`
    - `identifier`
    - `Connection`
    - `run`
    - Utils:
        - `parse_db_response`
        - `get_table_column_names`
        - `run_db_query`
- `pg8000.exceptions`
    - `DatabaseError`
- `dotenv`
    `load_dotenv`
- `os`
    - `os.getenv()`
- `with open()`
- `FastAPI`
    - `@app.exception_handler`
    - `@app.get`
    - `@app.post`
    - `@app.patch`
    - `@app.delete`
    - `HTTPException`
    - `Request`
    - `TestClient`
- `pydantic`
    - `BaseModel`
- `enum`
- `pytest`
    - `pytest.ini`
    - `conftest`
    - `@pytest.fixture`
    - `@pytest.mark.it`
    - `fastapi.testclient.TestClient`
## de-async
- `asyncio` library
    - `asyncio.sleep`
    - `asyncio.Queue()`
    - `asyncio.Queue().join()`
    - `asyncio.Queue()put_nowait()`
    - `asyncio.Queue().task_done()`
    - `asyncio.Queue().get()`
    - `asyncio.create_task`
    - `asyncio.gather`
    - `asyncio.run`
    = `asyncio.Task()`
    = `asyncio.Task().cancel()`
- `aiohttp` library
    - `aiohttp.ClientSession`
- `pytest`
    - `@pytest.mark.asyncio`
- `pydantic`
    - `@validate_call`
### Topics
- Understand how to wait for async operations.
- Understand how to run multiple async operations simultaneously.
- Understand the use cases of async code.

## de-terraform-tasks
### Terraform
- `data`
    - `http`
    - `cloudinit_config`
    - `aws_regions`
    - `aws_caller_identity`
    - `aws_iam_policy_document`
- `resource`
    - `aws_s3_bucket`
    - `aws_s3_object`
    - `aws_instance`
    - `aws_iam_instance_profile`
    - `aws_iam_role`
    - `aws_iam_role_policy`
    - `aws_key_pair`
    - `aws_secretsmanager_secret`
    - `aws_secretsmanager_secret_version`
    - `aws_security_group`
    - `aws_vpc_security_group_ingress_rule`
    - `aws_vpc_security_group_egress_rule`
- `terraform`
    - `backend`
    - `required_providers`
- `provider`
    - `default_tags`
- `output`
- `locals`
- `variables`

## de-lambdas
- Terraform Advanced
    -`terraform`
        - `backend`
        - `required_providers`
    - `module`
    - `provider`
        `default_tags`
    - `resource`
        - `aws_lambda_function`
        - `aws_s3_bucket`

    - `vars`
    - `output`
    - `data`
        - `archive_file`
        - `aws_region`
        - `aws_caller_identity`
    - `iam`
        - `data`
            - `aws_iam_policy_document`
                - Actions:
                    - `logs:CreateLogGroup`
                    - `logs:CreateLogStream`
                    - `logs:PutLogEvents`
                    - `s3:PutObject`
                    - `sts:AssumeRole`
                - Identifiers:
                    - `lambda.amazonaws.com`
        - `resource`
            - `aws_iam_policy`
            - `aws_iam_role_policy_attachment`
            - `aws_iam_role`

