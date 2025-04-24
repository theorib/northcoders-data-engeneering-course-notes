# 2025-03-24 - Notes
## `is` operator is a reference comparison (checking if the same in memory)
## `==` tests for value equality
Are these two objects equal in values even though different allocation in memory is possible. Example:
```python
list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 == list2 # True
list1 is list2 # False

```

## Primitives (object interning)
Primitive immutable values will have both equality of value and equality of memory address.

```python

string1 = 'hello'
string2 = 'hello'
print(string1 == string2) # True
print(string1 is string2) # True

```

## Testing
```bash

pip install -r requirements.txt

```

```python
import pytest

@pytest.mark.it('test description')
def test_empty_list():
    
```