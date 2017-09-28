# Script to generate data to feed fermat.py

import numpy as np
import sys

upper_bounds = sys.argv[1:]


'''
upper_bounds = array of upper bounds for numbers to test (1 -> upper_bound) for each [a/b, n]

Intended to use at the start of every fermat.py script to save writing to file.
But may have to write to file if numbers get to big to hold in memory
'''
def gen(upper_bounds):
	a_b_bound = int(upper_bounds[0])
	n_bound = int(upper_bounds[1])

	# Fill arrays 1 -> upper_bound
	a_b_bound = np.array(range(1, a_b_bound + 1))
	n_bound = np.array(range(3, n_bound + 1)) # n > 2, therefore 3 -> upper bound

	data_dict = {'a_b_data' : a_b_bound, 'n_data' : n_bound}

	print data_dict

gen(upper_bounds)