import algebra
from integer import primes

pp = set()

print(pr)

p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for l in algebra.permute(p) :
	property = True
	for j in range(1,8) :
		n = l[j] * 100 + l[j + 1] * 10 + l[j + 2]
		if n % pr[j - 1] :
			property = False
			break
	if property == True :
		print(l)