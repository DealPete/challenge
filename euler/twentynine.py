n = set()

for i in range(2,101) :
	for j in range(2,101) :
		n.add(i**j)
		
print(len(n))