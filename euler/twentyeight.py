j = 1
t = 1

for i in range(1,501) :
	for k in range(4) :
		j += 2 * i
		t += j

print(t)