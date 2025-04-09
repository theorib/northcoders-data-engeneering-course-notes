# 2025-04-08 - Notes
## Iterators and Iterables
In order to be iterable an object needs a `__iter__` method. It returns an iterator object

An **iterator object** has an `__iter__` method which returns itself and a `__next__` object which returns the next item from the iterator. The `StopIteration` exception is what tells `for` loops to stop the iteration

### Iterator Protocol
A new Iterator is created for an iterable every time we loop over an object, when the iterator is finished it's dumped

All Iterators are iterables but not all iterables are iterators (they both have an `__iter__`)
But if you have an iterable, it's `__iter__` method will return an iterator

### Custom For Loop
```python

def my_for(iterable, action_func):
    iterator = iter(iterable)

    try:
        item = next(iterator)
        action_func(item)
        my_for(iterator, action_func)
    except StopIteration:
        pass

```

iter() returns itself if what is passed is an iterator object, otherwise it returns a new iterator object if what was passed was an iterable

An iterator object always returns itself when `__iter__` is called an iterable always returns an instance of it's linked iterator whenever `__iter__` is called on it