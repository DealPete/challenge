import integer

pn = integer.primes(1000000)
pns = set(pn)

ocs = {i for i in range(3,1000000)}

for i in pn[:1000] :
	for j in range(1,100) :
		k = i + j**2 * 2
		if k in ocs :
			ocs.remove(k)

ocs = list(ocs)
ocs.sort()

for i in ocs :
	if i % 2 and not i in pns :
		print(i)
		break