from integer import palin
from integer import base10to2

t = 0

for i in range(1000000) :
	if palin(i) and palin(base10to2(i)) :
		print(i, base10to2(i))
		t += i
		
print(t)
