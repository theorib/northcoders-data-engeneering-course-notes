def greet_person(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(f'Hello {value.capitalize()}! Loverly to meet you!')


greet_person(first='canis', second='panis')


def iife():
    print('invoked')


print(iife())
