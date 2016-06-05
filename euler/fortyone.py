
from itertools import permutations
from integer import *

for p in permutations(range(7, 0, -1)) :
	d = digitsToNumber(p[::-1])
	if prime(d) :
		print(d)
		break
	else :
		print(d, "is not prime.")