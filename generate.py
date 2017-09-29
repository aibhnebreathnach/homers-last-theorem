'''
Script to generate data to feed fermat.py

upper_bounds = array of upper bounds for numbers to test (1 -> upper_bound) for each [a/b, n]

Intended to use at the start of every fermat.py script to save writing to file.
But may have to write to file if numbers get to big to hold in memory

ARGS = (a/b, n)
'''
import sys

upper_bounds = sys.argv[1:]

def generate(upper_bounds):
	a_b_bound = int(upper_bounds[0])
	n_bound = int(upper_bounds[1])

	a_to_upper = range(1, a_b_bound + 1) # a -> upper bound
	b_to_lower = a_to_upper[::-1] # lower bound <- b

	# list of tuples of a and b
	a_b_tuples = []

	# Fill arrays 1 -> upper_bound
	for index in range(len(a_to_upper)):
		a_b_tuples.append((a_to_upper[index], b_to_lower[index]))

	# Get the set of sorted tuples, removes duplicate permutations. ie (10, 1) and (1, 10)
	a_b_tuples = set(tuple(sorted(l)) for l in a_b_tuples)

	n_bound = range(3, n_bound + 1) # n > 2, therefore 3 -> upper bound

	data_dict = {'a_b' : a_b_tuples, 'n' : n_bound}

	return data_dict
