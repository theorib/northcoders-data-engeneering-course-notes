# 2025-04-24 - Notes
## Integration Testing
This gets the whole fastapi package and the testing dependency
```bash
pip install "fastapi[all]"
pip install httpx
```

```python
from fastapi.testclient import TestClient

```

## Unit Testing
- verify the behaviour of individual units of code, example functions, methods, etc.

## Integration Testing
- Verify that various units of code work together appropriately 

## Pytest Fixtures



## Kyle Notes to myself
- createa a function that receives a query string and returns a full database response already parsed
- format response taking columns, data, label
- putting an `__init__.py` file on a folder turns that folder into a module, exposing everything available inside that file


## Kyle Notes

- On get_review_by_id, on lines 19 and 24, when you use `literal()` why do you still use the :review_id notation instead of an f string directly since the data is already sanitized?

- When you are only running tests on a specific test function with `pytest file_name.py::test_my_test` is it not easy to not check if you broke something on the other tests since you are not always running them?

- On the very first tests you are writing for each class, (status_code) you are never seeing them fail first...

- On `post_new_game`, on line 49 you ended up skipping using the `literal()` function to escape your data


