from math import floor

n = [floor(3 * x / 7) for x in range(1,1000001)]

min = 1
minnum = 0

for i in range(1000000) :
	if (i + 1) % 7 :
		k = n[i]/(i + 1)
		if 3/7 - k < min :
			min = 3/7 - k 
			minnum = i

print("{}/{} is to the left of 3/7.".format(n[minnum], minnum + 1))