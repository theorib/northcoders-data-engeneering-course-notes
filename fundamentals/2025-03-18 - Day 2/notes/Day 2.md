# Day 2
## Functions
- Abstractions:
    Hiding away some functionality / complexity
- Parameters => variables that have values assigned when the function is invoked
- parameters are the actual variables written in the function
- arguments are the actual values we pass to a function

### positional Arguments
Their order matter.
```python
greet_person('sarah', 'oliver')
```

### Keyword arguments
order does not matter
```python
greet_person(name2='sarah', name1='oliver')
```

### multiple arguments (as a tuple)
```python

def greet_person(*args):
    for arg in args:
        print(f'Hello {arg.capitalize()}! Loverly to meet you!')

```

### multiple keyword arguments (as a dictionary)
They become a dictionary and values can be accessed via their keys, they can be looped through as well as any other dictionary would

```python

def greet_person(**kwargs):
    for arg in args:
        print(f'Hello {arg.capitalize()}! Loverly to meet you!')

```


## Modules and Imports
Modules exist for the purpose of sharing objects

### Importing a whole module
```python
import filename_no_extensions

filename_no_extensions.function_1()
print(filename_no_extensions.variable_1)

```

### Importing a named parts of a module
```python
from filename_no_extensions import function_1, variable_1

function_1()
print(variable_1)

```

### Importing all named parts
Be cautious as if there are naming clashes this way of importing will override things
```python
from filename_no_extensions import *
function_1()
print(variable_1)

```

### dealing with naming clashes
```python
from filename_no_extensions import function_1, variable_1 as variable_other
function_1()
print(variable_other)

```
### function calls or code executed in imported modules
function calls or code executed in imported modules will be executed when we import the module

### `__name__`
`__name__` will generally be the name of the module, unless it is the file being ran, in which case `__name__ == "__main__"`

A common pattern is to check if the file is being imported or if it's the current running file
```python

if __name__ == "__main__":
    print('something')

```
### filename clashes
if you import a built-in module which has the same name as a local module in your project they will crash and 

### importing modules from subfolders
```python
from sub_folder_name.filename_no_extensions import *
function_1()
print(variable_1)

```

### silver rule
We can import anything from the same directory or subdirectories
### golden rule
We can import anything that is in the search path

### adding new paths to the search path


 Hardcoding new paths into python's search path
```python
import sys

sys.path.append(
    '/Users/theorib/Development/Northcoders/northcoders-data-engeneering-course-notes')  
```

#### Defining a PYTHONPATH for the next command
```bash 
PYTHONPATH=$(pwd) pyton file_to_run.py
```

#### Defining a PYTHONPATH for the duration of the terminal session
Adding the current project directory in vs code as the PYTHONPATH for as long as that terminal session lasts
```bash
export PYTHONPATH=$(pwd)   
```

In the command line to append multiple values to PYTHONPATH we use collons to separate them:
```bash
export PYTHONPATH=/path_1:/path_2 
```