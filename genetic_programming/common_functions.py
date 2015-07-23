from numbers import Real
from typing import *


# Arithmetic

@params(Real, Real)
@rtype(Real)
def add(x, y):
    return x + y

@params(Real, Real)
@rtype(Real)
def sub(x, y):
    return x - y

@params(Real, Real)
@rtype(Real)
def mod(x, y):
    return x % y

@params(Real, Real)
@rtype(Real)
def mul(x, y):
    return x * y

@params(Real, Real)
@rtype(Real)
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return float('inf')

@params(Real, Real)
@rtype(Real)
def exp(x, y):
    return x ** y

@params(func((Real, Real), Real), Real)
@rtype(func((Real,), Real))
def num_partial(fn, arg):
    return lambda x: fn(arg, x)

@params(func((Real,), Real), [Real])
@rtype([Real])
def num_map(fn, nums):
    return map(fn, nums)