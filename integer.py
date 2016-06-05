"""computations involving the integers."""

def nCr(n, r) :
	if n - r > r :
		return nCr(n, n - r)
	top = bottom = 1
	for k in range(n - r + 1, n + 1) :
		top *= k
	for k in range(1, r + 1) :
		bottom *= k
	return top // bottom

def base10to2(n) :
	""" returns strings containing base 2 representation of n """
	b, p = '', 1
	while p <= n :
		if n % (p * 2) >= p :
			b = '1' + b
		else :
			b = '0' + b
		p *= 2
	return b

def bell(n) :
	""" returns dictionary containing the first n Bell numbers """
	B = {1:1}

	t = [[1]]

	for x in range(2, n) :
		lr = t[-1]
		nr = [lr[-1]]
		for y in lr :
			nr.append(nr[-1] + y)
		t.append(nr)
		B[x] = nr[0]
	
	return B
	
def collatz(n) :
	s = []
	while n != 1 :
		s.append(n)
		if (n % 2 == 0) :
			n //= 2
		else :
			n = 3*n + 1
	
	s.append(1)
	return s

def d(n) :
	return s(n) - n

def digits_hash(k) :
	"""If two numbers have fewer than 15 digits, then their
	digit hashes will agree only if the have the same digits.
	"""
	s = 0
	for i in str(k) :
		s += 15**int(i)
	
	return s

def digitsToNumber(l) :
	t = 0
	for i in range(len(l)) :
		t += 10**i * l[i]
	return t
	
def factor(n) :
	""" returns set of divisors of n """
	s = set()
	for i in range(1, int(n**.5) + 1) :
		if n % i == 0 :
			s.add(i)
			s.add(n//i)
	return s

def fib(n) :
	i, j = 1, 1
	for k in range(2,n) :
		i, j = j, i + j
	return j

def palin(n) :
	""" return: Is n palindromic? """
	s = str(n)
	while len(s) > 1 :
		if s[0] == s[-1] :
			s = s[1:-1]
		else :
			return False
	return True

def part(n) :
	""" Returns a list of the number of partitions of the first n integers. """
	
	l = [1]
	
	for i in range(1, n + 1) :
		total = 0
		for k in range(1, i + 1) :
			k1 = i - k * (3 * k - 1) // 2
			if k1 >= 0 :
				k1 = l[k1]
			else :
				k1 = 0
		
			k2 = i - k * (3 * k + 1) // 2
			if k2 >= 0 :
				k2 = l[k2]
			else :
				k2 = 0
			total += (-1)**(k + 1) * (k1 + k2)
			
			if k1 <= 0 : break
			
		l.append(total)
		
	return l

def partition(n, l = []) :
	"""Partitions the integer n

	n is the integer to be partitioned.
	l is a list of permissible summands in the partition.

	sorting l from largest to smallest improves speed dramatically.
	
	"""
	
	if l == [] :
		l = list(range(1, n + 1))
		l.sort(reverse = True)
		
	if len(l) == 1 :
		if n % l[0] == 0 :
			return 1
		else :
			return 0

	t = 0
	for i in range(n // l[0] + 1) :
		t += partition(n - i * l[0], l[1:])

	return t
	
def prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):   
        if not num % i or not num % (i + 2):
            return False
    return True

def primeFactors(n, lp) :
	""" lp is a list of primes """
	d = {}
	for p in lp :
		while not n % p :
			if p in d :
				d[p] += 1
			else :
				d[p] = 1
			n //= p
		if n == 1 :
			break
	return d

def uniquePrimeFactors(n) :
	""" return: dictionary of unique prime factors for first n integers. """
	d = {1:set()}

	for x in range(2, n + 1) :
		if not x in d.keys() :
			for y in range(x + x, n + 1, x) :
				if y in d.keys() :
					d[y].add(x)
				else :
					d[y] = {x}
			d[x] = {x}
			
	return d

def primPythaTriples(maxC = 10) :
	from math import floor
	""" return: set of primitive pythagorean triples (a, b, c) with c <= maxC. """
	f = floor(maxC **.5)
	upf = uniquePrimeFactors(f)
	s = set()
	
	for m in range(2, f + 1) :
		for n in [x for x in range(1, m) if (m - x) % 2 and upf[m] & upf[x] == set()] :
			s.add((m**2 - n**2, 2*m*n, m**2 + n**2))
	
	return s

def pythaTriples(maxC = 10) :
	""" return: set of pythagorean triples (a, b, c) with c <= maxC. """
	ppt = primPythaTriples(maxC)
	pt = set()
	
	for (a, b, c) in ppt :
		k = 1
		while k*c <= maxC :
			pt.add((k*a, k*b, k*c))
			k += 1
	
	return pt
	
def primes(n) :
	""" return: list of primes <= n. """
	i = 2
	a = set(range(2,n + 1))
	
	while i*i <= n :
		if i in a :
			j = i
			while i*j <= n :
				if i*j in a :
					a.remove(i*j)
				j = j + 1
		i = i + 1
	
	l = list(a)
	l.sort()
	return l
	
def s(n) :
	return sum(factor(n))

def sumdigits(n) :
	s = 0
	for i in str(n) :
		s += int(i)
	
	return s

def totients(n) :
	""" return: dictionary of totients for first n integers. """

	d = UniquePrimeFactors(n)
	
	t = {1:1}
	
	for x in range(2, n + 1) :
		denom = num = 1
		for k in d[x] :
			num *= k - 1
			denom *= k
		t[x] = (x * num) // denom
		
	return t



# Polygonal Numbers	
	
def triangles(n) :
	return [i*(i+1)//2 for i in range(1, n + 1)]

def pentagons(n) :
	return [i * (3*i - 1) // 2 for i in range(1, n + 1)]

def hexagons(n) :
	return [i * (2*i - 1) for i in range(1, n + 1)]
