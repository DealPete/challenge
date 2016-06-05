from math import floor

def rect(x, y) :
	return (x*(x+1)*y*(y+1))//4
	
closest = 2000000
clx = cly = 0

for x in range(1, 60) :
#	sr = floor((-1 + (1 + (32000000 / (x**2 + x)))**.5) / 2)
	k = rect(x, sr)
	l = rect(x, sr + 1)
	print("For x =", x, ", y =", sr, "or", sr + 1, "give", k, "and", l, ".")

	k = abs(2000000 - k)
	l = abs(2000000 - l)
	if closest > k :
		closest = k
		clx = x
		cly = sr
	if closest > l :
		closest = l
		clx = x
		cly = sr + 1
	print("Closest is", closest)

print("x = ", clx, " y =", cly)