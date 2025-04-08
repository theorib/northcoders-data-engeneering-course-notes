# 2025-04-04 - Notes
## Errors and Exceptions
### Two broader categories of errors:
#### Syntax error
- The code cannot be parsed and therefore cannot run
#### Exceptions
- When something goes wrong despite the code being sound enough to execute
- it doesn't necessary indicates a problem
- Exceptions are `raised` not thrown

```python
import pytest

class HorridTurnipsError(Exception):
    pass


def find_item(collection,index_or_key,default):
    try:
        result = collection[index_or_key]
        if result == 'turnips':
            raise HorridTurnipsError('Joe hates turnips')
        return result
    # to handle multiple error types we add the types in a tuple
    except (KeyError,IndexError):
        return default
    except TypeError:
        return 'collection must be type of dict or list'
    # this is a catch all errors for really unforeseen exceptions
    except Exception as error:
        print(f'unexpected problem {str(error.value)}')
    # finally even trumps returns statements
    finally:
        print('doing important cleanup')
        

    # here python 
def test_raises_exception_if_found_turnips():
    with pytest.raises(HorridTurnipsError) as error:
        find_item(['apple', 'turnips'], 1, 'a')
    # we can assert that the error message (value) is what we want but we don't have to line 33 and 32 would be enough for pytest to work
    assert str(error.value) == 'Joe hates turnips'
```

### Testing Exceptions
```python



```
