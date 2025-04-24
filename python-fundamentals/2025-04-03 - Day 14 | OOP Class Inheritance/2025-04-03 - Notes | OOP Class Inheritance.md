# 2025-04-03 - Notes
## Class Inheritance
We start with class inheritance by passing a class as an argument when creating a new class:
```python
class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def speak(self):
        return 'meow!'
    def eat(self,food):
        return f'{self.name} is enjoying some tasty {food}'
    
class Lion(Cat):
    pass
```

### Method overriding
Method Resolution order  `.mro()`
Will show the order in which a class will look for methods or properties
```python
class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def speak(self):
        return 'meow!'
    def eat(self,food):
        return f'{self.name} is enjoying some tasty {food}'
    
class Lion(Cat):
    def __init__(self, name, has_mane):
        # if we use init again, we need to use super and pass it the same arguments as the parent so I can inherit all relevant behaviours
        # here we are overriding the colour argument because all lions are gold
        super().__init__(name, colour='gold')
        self.has_mane = has_mane

    def speak(self):
        # return super().speak()
        return 'ROAR!'

simba = Lion('Simba',  True)
print(simba.eat('meat'))
print(simba.speak())

print(Lion.mro()) # [<class '__main__.Lion'>, <class '__main__.Cat'>, <class 'object'>]



```

### Polymorphism
an instance of a child is also an instance of the parent
an instance of lion is also an instance of cat

This is why we don't want to try and remove characteristics of the parent on the child so this work as expected.

When overriding methods and properties, we want to return the same type and receive the same arguments of the same type

so if we call `isinstance` on an instance of `Lion` it will return true for both `Cat`, `Lion` as well as `object` which is the master parent class
you can also call `issubclass` to check if a class is a child of another class

### Composition
Composition is when we use a class as part of another class
Nothing special going on here, we just accept other classes as part of the inner workings of a class like any other object
```python

class Which:
    def __init__(self, name, spells, cat):
        self.name = name
        self.spells = spells
        self.cat = cat
    def describe(self):
        print(f'{self.name} is a formidable witch')
        print(f'She knows {len(self.spells)}')
        print(f'She has a lovelly cat called {self.cat.name}')

```

## Magic Methods or Dunder Methods (for double underscore)
###
 ```python
print("hello " + "there!") # "hello there!"
print("hello ".__add__("there!")) # "hello there!"

print(2 + 4) # 6
print([1,2,3]+['a','b','c']) # [1, 2, 3,'a', 'b', 'c']



```
