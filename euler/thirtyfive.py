import prime

a = prime.primes(1000000)

t = 0

for j in range(1000000) :
	s = str(j)
	circular = True
	for i in range(len(s)) :
		if not int(s) in a :
			circular = False
			break
		s = s[-1] + s[:-1]
	
	if circular == True :
		t += 1
		print(j)

print(t)