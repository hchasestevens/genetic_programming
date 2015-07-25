from genetic_programming import *

input_1 = make_input([Real])
test_suite = (
    ([1,2,3], 6),
    ([4,5,6], 15),
    ([3,4,5], 12),
    ([10,0,1], 11),
    ([5,5,10], 20),
)
max_successes = 0
good_node = None
for i in xrange(5000000):
    if not (i % 1000):
        print i
    try:
        node = build_tree(Real)
        successes = 0
        for input_val, expected in test_suite:
           input_1.set(input_val)
           if node.evaluate() == expected:
               successes += 1
        if successes > 0:
            print i, ('!' * successes)
            if successes > max_successes:
                good_node = node
                max_successes = successes
        if successes == len(test_suite):
            break
    except (TypeError, ValueError, OverflowError):
        pass
else:
    print 'failed'

import pdb
pdb.set_trace()