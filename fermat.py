import numpy as np
import sys
import generate as gen

'''
Script to check for solutions to Fermat's Last Theorem to a certain degree of accuracy

Upper bounds on values a/b and n to test to decimal_places accuracy
filepath for output of hits
ARGS = (a/b, n. decimal_places, filepath)

'''
inputs = sys.argv[1:]

data = gen.generate([inputs[0],inputs[1]])
decimal_places = int(inputs[2])
filepath = inputs[3]

# Check for a hit in Homer's Last Theorem, with a ceratin degree of accuracy (decimal_places)
def check_fermat(a, b, n, decimal_places):

	results_csv = []

	# check input format
	# make sure it fits theorem
	if n <= 2:
		print 'n cannot be less than or equal to 2'

	if a <= 0 or b <= 0:
		print 'a or b cannot be negative'


	# (a^n + b^n)^1/12
	a_b = [a**n, b**n]
	a_b = np.around(np.power(np.sum(a_b), 1/float(n)), decimals = decimal_places)


	# check: a_b = integer, therfore (a^n + b^n)^1/n = c
	if (a_b).is_integer():
		c = a_b	
		# result in csv = a, b, c, n, decimal_places
		results_csv.append( '%d,%d,%d,%d, %d' % (a, b ,c, n, decimal_places) )
		print 'Hit: %d + %d = %d  PWR = %d DEC = %d' % (a, b, c, n, decimal_places)



# Save a hit in Homer's Last Theorem to file in csv
# CSV in format : a,b,c,n,decimal_places each seperated by a newline
def save_hits(filepath, results_csv):
	file = open(filepath, 'w')
	for result in results_csv:
		file.write(result + '\n')
	file.close();



# Check data for hits
for pwr in data['n']:
	for pair in data['a_b']:
		check_fermat(pair[0], pair[1], pwr, decimal_places)

# not saving hits yet, still testing

