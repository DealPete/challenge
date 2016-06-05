from math import factorial

for i in range(10, 3000000) :
	if i == sum([factorial(int(x)) for x in str(i)]) :
		print(i)