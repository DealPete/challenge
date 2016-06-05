def digits_hash(k) :
	"""If two numbers have fewer than 15 digits, then their
	digit hashes will agree only if the have the same digits.
	"""
	s = 0
	for i in str(k) :
		s += 15**int(i)
	
	return s