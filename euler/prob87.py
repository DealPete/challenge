from integer import primes

upper = 50000000
p = primes(int(upper**.5 + 1))
ex = set()

total = 0

for k in [x for x in p if x**4 < upper] :
	for l in [x for x in p if x**3 + k**4 < upper] :
		for m in [x for x in p if x**2 + k**4 + l**3 < upper] :
			j = m**2 + k**4 + l**3
			if not j in ex :
				total += 1
				ex.add(j)
#				print(j)

print(total)