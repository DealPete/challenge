import integer
l, num = 0, 0

for i in range(1,999999) :
	s = integer.collatz(i)
	if len(s) > l :
		num = i
		l = len(s)
		print(i, "has a sequence of length", len(s), ":", s)
		input()
	