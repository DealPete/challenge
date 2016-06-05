import equivalence
from integer import primes
from algebra import permute

d = primes(10000)

for i in d :
	if i < 1000 :
		d.remove(i)

def relation(a, b) :
	if list(str(a)) in permute(list(str(b))) :
		return True
	return False
	
sets, parts = equivalence.equivalence_partition(d, relation)

for q in sets :
	s = list(q)
	while len(s) >= 3 :
		a = s[0]
		s = s[1:]
		for t in s :
			dif = t - a
			if t + dif in s :
				print("Found it:", a, t, t + dif)
				break