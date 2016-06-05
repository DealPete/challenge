from integer import sumdigits

k = 0
	
for a in range (1, 100) :
	for b in range (1, 100) :
		z = sumdigits(a ** b)
		if z > k :
			print("a = {}, b = {}. The digital sum is {}".format(a, b, z))
			k = z