from integer import palin

def reverse(num) :
	return int(str(num)[::-1])

total = 0

for i in range(1, 10000) :
	k = i + reverse(i)
	for j in range(1, 50) :
		if palin(k) :
			break
		k = k + reverse(k)

	if j == 49 :
		total += 1
		
print(total)
	