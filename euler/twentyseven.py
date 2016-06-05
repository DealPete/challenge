import prime

p = prime.primes(999000)
p10000 = {x for x in p if x < 10000}

amax = 0
bmax = 0
pnum = 0

for b in p10000 :
	for a in range(-9999,10000) :
		n = 0
		while n**2 + a*n + b in p :
			n += 1
		if n > pnum :
			amax, bmax, pnum = a, b, n
			
print("n =", 71, "  a =", amax, "  b =", bmax, ".  a*b =", amax*bmax)