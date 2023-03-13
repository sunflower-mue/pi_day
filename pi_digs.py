import numpy as np
from numpy.testing._private.utils import _integer_repr

def pi_digits():
	
	'''
	Return an n length  numpy array of pi digits after the decimal

	'''

	#store in an n length  list of int the pi digits after the decimal then convert list to a numpy array
	pi_dig = []
	file_path = '/home/mueletshezi/github/piday/digits.txt'
	with open(file_path,'r') as file:
		while True:
			char = file.read(1)
			
			if char in [' ', "\n"]:
				break
			else:
				pi_dig.append(char)

	pi_dig = pi_dig[2:]
	pi_dig = list(map(int, pi_dig))
	pi_digits = np.asarray(pi_dig)
	
	return pi_dig



if __name__ == "__main__":
	print(pi_digits())
	print(len(pi_digits()))
