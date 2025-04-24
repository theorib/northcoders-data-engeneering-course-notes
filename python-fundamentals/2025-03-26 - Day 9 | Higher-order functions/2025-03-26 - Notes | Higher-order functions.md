# 2025-03-26 - Notes.md
## Higher-order functions
Higher-order functions either:
- take another function as an argument
- return another function

### Testing HOFunctions
- we need to make sure when we arrange the test that we pass it something measurable\
- if we are passing arguments to the functions that were passed as arguments we should test that those arguments are reaching the function correctly when called

```python
def test_argument_func_runs():
    # arrange
    call_count = 0
    def test_func():
        nonlocal call_count
        call_count += 1
    num_repeats = 3
    
    # act
    repeater(test_func, num_repeats)

    # assert
    assert call_count == num_repeats

```

Glassbox, white box, clear box, open box, transparent, structural testing

#### Types of Functions (per return)
- Iteratee function | is a function called on every iteration of a loop
- 