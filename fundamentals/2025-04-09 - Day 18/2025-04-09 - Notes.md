# 2025-04-09 - Notes
## Generators
- `yield` keyword makes a function a generator and returns an iterator implicitly
- The generator object is created when the function is invoked not upon encountering the `yield` keyword
- the function's execution frame is paused at the `yield` statement, holding all it's variables and environment until the next execution
- At the end of the function a `StopIteration` exception is raised

```python
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(gen) # <generator object simple_gen at 0x12049c300>
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # raises StopIteration exception
```

### Use cases
- Reading large datasets and returning chunks of it at a time
- getting the next value from an infinite series
- making a network request to a server that will take a long time 

### Generator comprehensions
when using round brackets in a comprehensions behind the scenes this is a generator
**This is not a tuple comprehension but a generator**
```python
comp = (n*2 for n in range(5))
print(comp) # <generator object <genexpr> at 0x1204aea80>
```

### Coroutines
- computation that can be suspended and resumed later
- Generators are coroutines
- This let's us do async programming in python
    - doing several things at the same time
    - waiting for a processes to complete


### A custom async manager:
```python
from time import time
def wait_for_me(time_to_wait):
    start_time = time()
    while time() < start_time + time_to_wait:
        yield # yields none
    print(f'waited for {time() - start_time} seconds')
    
    yield True
    
wait_for_me(3)

tasks = [wait_for_me(3),wait_for_me(5), wait_for_me(10)]

while len(tasks):
    for task in tasks:
        try:
            next(task)
        except StopIteration:
            tasks.remove(task)
```





