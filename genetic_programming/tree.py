import random
from typing import lookup_rtype, rtype, params


class UnsatisfiableType(Exception):
    pass


class Node(object):
    def __init__(self, f, allowed_functions=None):
        self.f = f
        self.rtype = f.rtype
        allowed_children = self.f.allowed_children()
        if allowed_functions is not None:
            allowed_children = [[child for child in child_list if child in allowed_functions] for child_list in allowed_children]
        if not all(allowed_children):
           raise UnsatisfiableType("{} has a parameter that cannot be satisfied.".format(self.f.func_name))
        self.children = [Node(random.choice(child_list)) for child_list in allowed_children]
        self.num_children = len(self.children)

    def evaluate(self):
        return self.f(*[child.evaluate() for child in self.children])


class Input(object):
    def __init__(self, value, name):
        self.value = value
        self.func_name = name
    def set(self, value):
        self.value = value
    def __call__(self):
        return self.value


def make_input(return_type, initial_value=None, name=''):
    new_input = Input(initial_value, name or 'input_' + str(return_type))
    rtype(return_type)(params()(new_input))
    return new_input


def build_tree(rtype, allowed_functions=None):
    starting_functions = set(lookup_rtype(rtype))
    if allowed_functions is not None:
        allowed_functions = frozenset(allowed_functions)
        starting_functions &= allowed_functions
    starting_functions = list(starting_functions)
    if not starting_functions:
        raise UnsatisfiableType()
    for __ in xrange(99999):
        try:
            return Node(random.choice(starting_functions), allowed_functions)
        except RuntimeError:
            pass
    else:
        raise RuntimeError("Unable to construct program, consider raising recursion depth limit.")