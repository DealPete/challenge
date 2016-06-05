import integer

d = integer.uniquePrimeFactors(12000)

total = 0

for i in range(2, 12001) :
	for j in range(1, i) :
		if d[i] & d[j] == set() and 1/3 < j/i and j/i < 1/2 :
			total += 1
			
print(total)