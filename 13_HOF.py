# HOF 
from typing import Callable

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):
    return func(x, y)

print(apply(add, 2, 1))

CallableFunction = Callable[[int, int], int]

add2 : CallableFunction = lambda x, y: x + y 

sub2 : CallableFunction = lambda x, y: x - y

apply2 : Callable[[CallableFunction, int, int], int] = lambda func, x, y: func(x, y)

print(apply2(add2, 2, 1))