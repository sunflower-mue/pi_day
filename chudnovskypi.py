import math
from decimal import *
def pi_day(n):
	"""
	Compute pi using Chudnovsky's algorithm up to n-1 digits after the decimal point.

	"""

	#The algorithm
	
	num = Decimal(0)
	den = Decimal(0)
	sum = Decimal(0)
	pi = 0	
	getcontext().prec = n
	for k in range(n):
		num = ((-1)**k)*(math.factorial(6*k))*(13591409 + 545140134*k)

		den = math.factorial(3*k)*((math.factorial(k))**3)*((640320)**(3*k +
																			Decimal(1.5)))
			
		sum += Decimal(num)/ Decimal(den) 
	
	sum = Decimal(12)*sum
	pi = 1/sum
	return str(pi)


if __name__ == "__main__":
	
	print(pi_day(1000)) #Redirect output to a .txt file using chudnovskypi > file.txt for time and memory efficiency.

	
