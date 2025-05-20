# Pytest REF

## `pytest.ini`
```toml
[pytest]
addopts = -rP --testdox
pythonpath = .
verbosity_assertions = 3
verbosity_test_cases = 3
```

## Pytest Fixtures

### Creating a `conftest.py` file
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from db.run_seed import seed_db

@pytest.fixture(autouse=True)
def seed_test_db():
    seed_db()

@pytest.fixture
def client():
    return TestClient(app)
```

