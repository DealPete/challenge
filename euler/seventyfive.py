from integer import uniquePrimeFactors

upf = uniquePrimeFactors(1225)

d = {}

for m in range(1,1225) :
	for n in [x for x in range(1, m) if (m - x) % 2 and upf[m] & upf[x] == set()] :
		k = 1
		s = 2*k*m*(m+n)

		while s <= 1500000 :
			if s in d.keys() :
				d[s] += 1
			else :
				d[s] = 1
			k += 1	
			s = 2*k*m*(m+n)

			

print(len([d[x] for x in d.keys() if d[x] == 1]))