for a in range(1,998) :
	for b in range(1, 1000 - a - 2) :
		if a**2 + b**2 == (1000 - a - b)**2 :
			print(a, "^2 + ",b, "^2 = ", (1000 - a - b))