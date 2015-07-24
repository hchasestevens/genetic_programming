from genetic_programming import *

@params([Real], Real)
@rtype(Real)
def num_index(num_list, index):
    return num_list[index % len(num_list)]

input_1 = make_input([Real])
test_suite = (
    ([1,2,3], 6),
    ([4,5,6], 15),
    ([3,4,5], 12),
)
for i in xrange(1000000):
    if not (i % 1000):
        print i
    try:
        node = Node(add)
        successes = 0
        for input_val, expected in test_suite:
           input_1.set(input_val)
           if node.evaluate() == expected:
               successes += 1
        if successes > 0:
            print i, ('!' * successes)
            good_node = node
        if successes == len(test_suite):
            break
    except (RuntimeError, TypeError, ZeroDivisionError, ValueError):
        pass
else:
    print 'failed'

import pdb
pdb.set_trace()