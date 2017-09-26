import numpy as np
import sys

inputs = sys.argv[1:]
a = float(inputs[0])
b = float(inputs[1])
c = float(inputs[2])
n = float(inputs[3])
decimal_places = int(inputs[4]) # must be int for np.around to take it

# Check for a hit in Fermat's Last Theorem, with a ceratin degree of accuracy (decimal_places)

def check_fermat(a, b, c ,n, decimal_places):
	# check input format
	# make sure it fits theorem
	if n <= 2:
		print 'n cannot be less than or equal to 2'

	if a <= 0 or b <= 0 or c <= 0:
		print 'a, b or c cannot be negative'


	# (a^n + b^n)^1/12
	a_b = [a**n, b**n]
	a_b = np.around(np.power(np.sum(a_b), 1/float(n)), decimals = decimal_places)

	c = np.around(c, decimals = decimal_places)

	# check: (a^n + b^n)^1/12 = c
	check = a_b == c

	if check == True:
		# will save results in future to make stats
		# only save hits on decimal accuracy
		print 'it works!'


check_fermat(a, b, c ,n, decimal_places)

