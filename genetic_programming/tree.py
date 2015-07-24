
import random

class Node(object):
    def __init__(self, f, allowed_functions=None):
        self.f = f
        allowed_children = self.f.allowed_children()
        if allowed_functions is not None:
            allowed_children = [[child for child in child_list if child in allowed_functions] for child_list in allowed_children]
        assert all(allowed_children), "{} has a parameter that cannot be satisfied.".format(self.f.func_name)
        self.children = [Node(random.choice(child_list)) for child_list in allowed_children]
        self.num_children = len(self.children)

    def evaluate(self):
        return self.f(*[child.evaluate() for child in self.children])


def build_tree(rtype, allowed_functions=None):
    pass