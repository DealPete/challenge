from math import floor

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
