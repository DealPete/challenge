from integer import primes

p = primes(1000000)

def longest_sequence(n) :
	t = 0
	for i in [pr for pr in p if pr > n] :
		t += i
		if t in p :
			print(t)
		if t > 1000000 :
			break