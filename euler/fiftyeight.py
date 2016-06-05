from integer import prime

j = 1
t = 1
i = 0

cont = True

primes_found = 0

while cont :
	i += 1
	
	for k in range(4) :
		j += 2 * i
		if prime(j) :
			primes_found += 1
		
	ratio = primes_found / (4 * i + 1)
	
	print("For length {}, the ratio is {}".format(2*i + 1, ratio))
	
	if  ratio < 0.1 :
		cont = False
		
print(2 * i + 1)