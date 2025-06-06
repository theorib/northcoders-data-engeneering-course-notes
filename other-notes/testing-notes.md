# Testing Notes
## General
- Test for **Purity** checking if new objects are being created
- Test for **value mutation** of the original arguments passed
- Test for **empty lists**, **empty strings**, etc
- Always test with the **simples possible inputs** first
- Test for correct exceptions raised with `with pytest.raises():`

## Higher order Functions
- check that HOF receives or returns a function
- If relevant, check that HOF function can receive **`n` positional arguments**
- If relevant, check that HOF function can receive **`n` keyword arguments**
- Check that all **arguments** passed are correctly **received by decorated function** 
- Check **number of function invocations** in decorator

## Decorators
- Check that decorator **returns a function**
```python

from types import FunctionType

@pytest.mark.it('check that do_twice returns a function')
def test_return_func():
    @do_twice
    def dummy():
        pass

    assert isinstance(dummy, FunctionType)
```
- Check that all **arguments** passed are correctly **received by decorated function** 
- Check **number of function invocations** in decorator
- If relevant, check that the decorated function can receive **`n` positional arguments**
- If relevant, check that the decorated function can receive **`n` keyword arguments**

## Iterators
- always check that the iterator **returns itself** when passed to the **`iter()`** function

## OOP
- check that classes are storing values in **all relevant properties**