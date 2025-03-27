# Day 4
## Tuples
We can create tuples in many different ways, including writing two variables separated by a comma for example:
```python

return variable1, variable2 # this will become a tuple

```

`tuple(1,2)`

### switching values with tuples
```python
(a, b) = (b, a)
```

### 

## Dictionaries
### Unpacking
```python
def create_dictionary(**new_dictionary):
    return new_dictionary

create_dictionary(dog='bingo', cat='Spike')
```

## Sets
- Cannot take mutable arguments
- not ordered

## Comprehensions
- We loose access to the variables defined within the comprehension

## Multiple Ifs 

We can add multiple ifs like so:

```python

list = [let1 + let2 for let2 in 'xyz' for let1 in 'abc' if let1 != 'b' if let2 != 'z']
print(list)

```


## Nested loops in list comprehensions
- if we nest loops in list comprehensions, the first loop is always the outer loop, the next loop is the inner loop and so on and so forth

```python
list = [let1 + let2 for let1 in 'abc' for let2 in 'xyz']
print(list)

```
is the same as 

```python

```python

list = []
for let1 in 'abc':
    for let2 in 'xyz':
        list.append(let1+let2)

print(list)

```

```
## Dictionary Comprehension

Walrus operator
```python

dic_comp = {x : str(rem) for x in range(15) if (rem := x% 3) == 0}
print(dic_comp)

```
