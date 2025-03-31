# 2025-03-27 - Notes
## Closures and Decorators
### Closures
a function remembers all the available variables from the environment and time in which it was initially declared

here we need the closure to be able to keep a counter that doesn't reset every time we call the function

**closures stay in memory for as long as the program is running and are not garbage collected**

For 

```python
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count =+1
        return count
    
    return count

my_counter = make_counter()
print(my_counter()) # Prints 1
print(my_counter()) # Prints 2
print(my_counter()) # Prints 3

theo_counter = make_counter()
print(my_counter()) # Prints 1
print(my_counter()) # Prints 2
print(my_counter()) # Prints 3
print(my_counter()) # Prints 4
print(my_counter()) # Prints 5
print(my_counter()) # Prints 6

print(my_counter()) # Prints 4

```

### Decorators
We will use decorators to modify the behaviour of a function
#### Recipe for a decorator
1. HOF that accepts a function
2. Inner function that modifies original function behaviour
    params need to match ip with the original function inputs
3. Return the inner function
4. Decoration happens specifically when we are defining a new function!

```python
def swap(func):
    def _wrap_func(a, b):
        return func(b, a)

    return _wrap_func

@swap
def subtract(a,b):
    return a - b

subtract(6,1)
```


Are decorators a shortcut for applying a very specific pattern of higher order functions into a function?
That pattern receives a function as an argument (the decorated function), and returns a new function. This new function modifies the behaviour of the decorated function.

Example of decorator returned from another higher order function 
```python
def multiply(num):
    def multiply_decorator(func)
        def multiply_wrapper(*args, **kwargs):
            return func(*args, **kwargs) * num
        return multiply_wrapper
    return multiply_decorator

@multiply(2)
def do_math(a, b):
    return a + b

do_math(2, 2) # result 8

```
