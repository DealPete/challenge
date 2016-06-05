import time
from integer import primes, primeFactors
from itertools import count

startTime = time.time()

pl = primes(10000)
t = 0

for i in count(647) :
	if len(primeFactors(i, pl)) == 4 :
		t += 1
	else :
		t = 0
	if t == 4 :
		print(i)
		break
		
endTime = time.time()
print("Algorithm took", endTime - startTime, "seconds.")