from integer import d

amicable = set()

for i in range(1,10001):
	if i == d(d(i)) and d(i) != i :
			amicable.add(i)

print(sum(amicable))