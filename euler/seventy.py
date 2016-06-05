from integer import digits_hash
from integer import primes
from integer import primeFactors
from integer import sumdigits

d = {}

for x in range(2, 10000000) :
	if not x in d.keys() :
		for y in range(x + x, 10000000, x) :
			if y in d.keys() :
				d[y].add(x)
			else :
				d[y] = {x}
		d[x] = {x}

m = 5000

for x in range(2, 10000000) :
	denom = num = 1
	for k in d[x] :
		num *= k - 1
		denom *= k
	tx = (x * num) // denom
	if sumdigits(tx) == sumdigits(x) :
		if digits_hash(tx) == digits_hash(x) :
			z = x / tx
			if z < m :
				m = z
				print("{} has quotient {}".format(x, z))