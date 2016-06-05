import math

def factChain(n) :
	timeToStop = False
	k = n
	l = [n]
	while not timeToStop :
		z = [math.factorial(int(x)) for x in str(k)]
		k = sum(z)
		if k in l :
			timeToStop = True
		else :
			l += [k]

	return l
	
total = 0
for i in range(1000001) :
	k = factChain(i)
	if len(k) == 60 :
		total += 1

print(total)