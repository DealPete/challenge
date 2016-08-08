def shift(n, c):
	if not c.isalpha():
		return c
	newOrd = ord(c) + n
	if (c.islower() and newOrd > 122) or (c.isupper() and newOrd > 90):
		newOrd -= 26
	return chr(newOrd)

def caesar(n, msg):
	return ''.join(list(map(lambda c: shift(n, c), msg)))
