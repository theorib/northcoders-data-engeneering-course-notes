# 2025-04-11 - Notes
Python is single threaded by default

Typical asynchronous behaviour:
- When we don't know how long a task will take to complete

## Async

- multiprocessing
- threading

## non-blocking code
For when:
- Take a long time to execute
- The order in which operations happen does not matter


## Async Await
- for denoting things that are co routines
- awaiting is a blocking operation
- cannot use await outside an async function
- `async with` and `async for` are also valid syntaxes
- A function that you introduce with `async def` is a *coroutine*. It may use `await`, `return`, or `yield`, but all of these are optional. Declaring `async def noop(): pass` is valid
- Using `await` and/or `return` creates a **coroutine function**. To call a coroutine function, **you must `await` it** to get its results.
- Using `yield` in an an `async def` block, creates an asynchronous generator which can be iterated with `async for`. You cannot use `yield from` in these functions
- You can only use await in the body of coroutines.
- You can only use `await` on an object that is *awaitable*  (it has an `__await__` magic method defined) or is a *coroutine*
- `@asyncio.coroutine` was the old way of using a decorator to define a function as a coroutine but it uses generators in the background while normal `async` functions are **native coroutines**
-  `await` is analogous to `yield from`, and it often helps to think of it as such 
- The use of `await` is a signal that marks a **break point**. It lets a coroutine temporarily *suspend execution* and permits the program to come back to it later.

## `async for`
- You can use `async for` comprehensions to iterate over an async iterator (an async generator):
    `g = [i async for i in mygen()]`
- neither asynchronous generators nor comprehensions make the iteration concurrent. All that they do is provide the look-and-feel of their synchronous counterparts, but with the ability for the loop in question to give up control to the event loop for some other coroutine to run.



## Coroutine
A coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.

- any async function in python is a coroutine (but only after it's called)
- An async function becomes a coroutine after it's called, before that it's a function
- suspended and resumed

## Event Loop
-  Coroutines don’t do much on their own until they are tied to the event loop.
- By default, an async IO event loop runs in a single thread and on a single CPU core.
- `asyncio.run()`  is responsible for getting the event loop, running tasks until they are marked as complete, and then closing the event loop.
- There’s a more long-winded way of managing the asyncio event loop, with get_event_loop(). The typical pattern looks like this:
```python
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```
- Other coroutines can be executed with await. It is typical to wrap just main() in asyncio.run(), and chained coroutines with await will be called from there.
- You can use `create_task()` to schedule the execution of a coroutine object, followed by `
-  `asyncio.gather()` puts a collection of coroutines (futures) into a single future.  As a result, it returns a single future object, and, if you await asyncio.gather() and specify multiple tasks or coroutines, you’re waiting for all of them to be completed.
- Alternatively, you can loop over `asyncio.as_completed()` to get tasks as they are completed, in the order of completion. 
```python
async def main():
     t = asyncio.create_task(coro([3, 2, 1]))
     t2 = asyncio.create_task(coro([10, 5, 0]))
     print('Start:', time.strftime('%X'))
     for res in asyncio.as_completed((t, t2)):
         compl = await res
         print(f'res: {compl} completed at {time.strftime("%X")}')
     print('End:', time.strftime('%X'))
     print(f'Both tasks done: {all((t.done(), t2.done()))}')

a = asyncio.run(main())

```


## Gather
- when we use gather we pass it async function calls as separate arguments without awaiting them
`gather(async_func(),async_func_2(),async_func_3())`

## Example of Blocking Code:
```python
from time import time

def sleepygreet(name:str, time_to_wait:int):
    current_time = time()
    end_time = current_time + time_to_wait
    while time() < end_time:
        yield

    yield f'Good Morning {name}'

start_time = time()
num_calls = 0
for value in sleepygreet('Theo', 3):
    num_calls += 1
    if value:
        print(value)
        print(f'called next() {num_calls} times')
print(f'finished running in {time()- start_time}')
```

## Example of hand made async runner:
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

## Example

## Solving *RuntimeError: asyncio.run() cannot be called from a running event loop*
source [Solved: How to Fix ‘asyncio.run cannot be called from a running event loop’ Error in Jupyter Notebook](https://sqlpey.com/python/solved-how-to-fix-asyncio-run-cannot-be-called-from-a-running-event-loop-error-in-jupyter-notebook/)
```python
import nest_asyncio
nest_asyncio.apply()
```


### `yield from some_iterator` Is the same as
```python
for x in some_iterator:
    yield x
```
