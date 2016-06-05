from integer import sumdigits

def nth_convergent(n) :

	denom = 1
	if n % 3 == 0 :
		num = (n//3) * 2
	else :
		num = 1

	if n == 1 :
		num = 2
		denom = 1
	
	for i in range(n,1,-1) :
		if i == 2 :
			k = 2
		elif i % 3 == 1 :
			k = ((i - 1)//3) * 2
		else :
			k = 1
		num, denom = denom, num
		num = k * denom + num

	print("{}/{}\n".format(num, denom))
	print(sumdigits(num))