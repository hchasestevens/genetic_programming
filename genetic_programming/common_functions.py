from numbers import Real
from typing import params, rtype, func, constant


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
    try:
        return x % y
    except ZeroDivisionError:
        return float('inf')

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
    try:
        return x ** y
    except ZeroDivisionError:
        return float('nan')

one = constant(Real, 1)
zero = constant(Real, 0)
two = constant(Real, 2)
half = constant(Real, 0.5)

@params(func((Real, Real), Real), Real)
@rtype(func((Real,), Real))
def num_partial(fn, arg):
    return lambda x: fn(arg, x)

@params(func((Real,), Real), [Real])
@rtype([Real])
def num_map(fn, nums):
    return map(fn, nums)

empty_num_list = constant([Real], ())

@params(Real)
@rtype([Real])
def listify_num(num):
    return (num,)

@params([Real], Real)
@rtype([Real])
def num_append(nums, num):
    return tuple(nums) + (num,)

@params([Real], [Real])
@rtype([Real])
def num_extend(first_nums, second_nums):
    return tuple(first_nums) + tuple(second_nums)

@params([Real])
@rtype(Real)
def num_list_empty(nums):
    return bool(nums)

@params([Real])
@rtype(Real)
def num_list_head(nums):
    if nums:
        return nums[0]
    return float('nan')

@params([Real])
@rtype([Real])
def num_list_tail(nums):
    if nums:
        return nums[1:]
    return nums

@params([Real])
@rtype(Real)
def num_list_len(nums):
    return len(nums)

@params(Real, Real)
@rtype(Real)
def num_eq(first, second):
    return first == second

@params(Real, Real)
@rtype(Real)
def num_neq(first, second):
    return first != second

@params(Real)
@rtype(Real)
def num_not(num):
    return not bool(num)

@params(Real, Real)
@rtype(Real)
def num_and(first, second):
    return first and second

@params(Real, Real)
@rtype(Real)
def num_or(first, second):
    return first or second

@params(Real, Real)
@rtype(Real)
def num_xor(first, second):
    return first ^ second

if_types = (
    Real, [Real], 
    func((Real,), Real), func((Real, Real), Real),
    func(([Real],), Real), func(([Real],), [Real]), func((Real,), [Real]),
)
num_ifs = []
for if_type in if_types:
    @params(Real, if_type, if_type)
    @rtype(if_type)
    def _num_if(cond, first, second):
        return first if cond else second
    _num_if.func_name += '_' + str(if_type)
    num_ifs.append(_num_if)

@params(func(([Real],), Real))
@rtype(func(([Real],), Real))
def list_num_fun_id(f):
    return f

@params([Real], Real)
@rtype(Real)
def num_index(num_list, index):
    try:
        return num_list[int(index) % len(num_list)]
    except (ZeroDivisionError, OverflowError):
        return float('nan')