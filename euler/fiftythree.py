import gmpy2

total = 0

for i in range(10, 101) :
	for j in range(1, i) :
		if gmpy2.comb(i, j) >= 1000000 :
			total += 1

print(total)