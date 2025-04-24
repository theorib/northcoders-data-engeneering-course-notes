# 2025-03-31 - Notes
## Recursion
- Functions that call themselves
- Produces a looping behaviour
- if it creates an infinite loop, python stops recursion execution to a 1000 times by default (this can be changed)
### questions
- What are the advantages of recursion? Memory usage?
- Why use recursion?
### Characteristics
- Base case: When recursion is no longer needed
- Recursive case: When recursion should happen and the function calls itself
    - Recursive Step: another step where it gets closer to the base case
    - Recursive Call: function calls itself

#### Use cases
- generally nice in dynamic problems where you don't know the limits
- can be very elegant and concise
- if you don't know how many nesting levels there will be, do it again
- if doing multiple nested loops and we don't know how deep we need to loop 
#### Notes
- a lot of the times we will need to return the function call in a recursive function otherwise it doesn't work
#### Examples
```python



def print_all_nested(nums):
    for element in nums:
        if type(element) == list:
            print_all_nested(element)
        # else here is very important otherwise it would print the list even after it had recursively gone into it
        else:
            print(element)

print_all_nested([1,2,[3,[4]],[5,[6,[7]]],[[[8,[9,[10]]]]]])

```

Factorial:
```python

def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)

```


###
