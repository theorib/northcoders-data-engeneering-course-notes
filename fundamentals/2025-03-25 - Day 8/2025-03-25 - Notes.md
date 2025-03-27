# 2025-03-25 - Notes.md
## Functional Programming
A programming paradigm or set of guidelines about how you might write good, robust programs with functions as your primary means of modeling systems
- Functions as abstractions
    We can call a function without needing to know/see it's complex inner workings
- Purity - generally ensuring immutability
- Functions are first class, they are just like other variables
- Deterministic, given a same input we get the same output
- Higher order functions
## Scope
- wether a variable is accessible or not accessible
- it works in a specific orders or precedence:
1. Local
2. Enclosing
3. Global
4. Builtins

## Namespaces
- A namespace is a mapping from names to objects (like a dictionary)
### Local Namespace
Created when a function is called and contains variables declared in the function body and it's parameters
`locals()` function returns everything in the local namespace

### Enclosing Namespace
When a function is **declared** inside another function this refers to the namespace of the 'outer' function

### Global Namespace
Contains any names declared on the main/root level of the program
`globals()` returns everything in the global namespace

### Builtins Namespace
Contains


**where a function is called is irrelevant, the variables it has access to are the ones of the scope of where it was declared**

**loops DO NOT have their own namespace**, a variable defined inside a loop is available in the global scope

### `nonlocal` and `global`
Are both keywords used when reassigning variables inside scopes different than global.

This will result in an UnboundLocalError
```python

def foo():
    num = 10

    def bar():
        num += 3
        print(num)
    
    bar()

foo()
```
To fix that we use the `nonlocal` keyword

`nonlocal` means please look for a nonlocal variable in the eclosing scope instead of creating a new one

```python

def foo():
    num = 10

    def bar():
        nonlocal num
        num += 3
        print(num)
    
    bar()

foo()

```
similarly, `global` means please look for a global variable in the instead of creating a new one

This is normally not good practice so use it mindfully

```python

num = 10
def foo():

    def bar():
        global num
        num += 3
        print(num)
    
    bar()

foo()

```