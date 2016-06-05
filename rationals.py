from integer import sumdigits
from math import floor
	
def newton_square_root(n, i = 10) :
	""" Iterates Newton's method i times for square root of n. """
	num = denom = 1
	
	for j in range(i) :
		num1 = (num ** 2) + n * (denom ** 2)
		denom1 = 2 * num * denom
		num = num1
		denom = denom1
	
	return (num, denom)
	
def nth_convergent(r, n) :
	""" nth convergent of root r """

	cf = continued_fraction_root(r)
	
	k = cf[0]
	if n == 1 :
		return (k, 1)
		
	cf = cf[1:]
	
	for i in range(n, 1, -1) :
		cv = cf[(i - 2) % len(cf)]
		if i == n :
			num = 1
			denom = cv
		else :
			num = cv * denom + num
			num, denom = denom, num
	
	num += k * denom
	
	return (num, denom)
		
	
def continued_fraction_root(n) :
	q = floor(n**.5)
	ans = [q]
	a = 1
	c = q
	cond = True
	while cond:
		d = (n - c**2) / a
		t = floor((n**.5 + c)/d)
		a = d
		c = t*a - c
		if a == 1 and c == q :
			cond = False
		ans.append(t)
	return ans