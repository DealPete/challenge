from itertools import combinations
from integer import primes
from integer import prime

p = primes(10000)

def pp(a, b) :
	if prime(int(str(a) + str(b))) and prime(int(str(b) + str(a))) :
		return True
	else :
		return False

def program() :		
	for a1 in range(1, len(p) - 1) :
		print("a1 = " + str(a1))
		for a2 in range(a1 + 1, len(p) - 1) :
			print("a1 = {}, a2 = {}".format(a1, a2))
			if pp(p[a1], p[a2]) :
				for a3 in range(a2 + 1, len(p) - 1) :
					if pp(p[a1], p[a3]) and pp(p[a2], p[a3]) :
						for a4 in range(a3 + 1, len(p) - 1) :
							if pp(p[a1], p[a4]) and pp(p[a2], p[a4]) and pp(p[a3], p[a4]) :
								for a5 in range(a4 + 1, len(p) - 1) :
									if pp(p[a1], p[a5]) and pp(p[a2], p[a5]) and pp(p[a3], p[a5]) and pp(p[a4], p[a5]) :
										print ("A set of five prime pairs is {}, {}, {}, {}, {}.".format(p[a1], p[a2], p[a3], p[a4], p[a5]))
										return

#for i in permutations(p, 5) :
#	good = True
#	print(i)
#	for j in permutations(i, 2) :
#		if prime( int(str(j[0]) + str(j[1])) ) == False :
#			good = False
#			break
#	if good == True :
#		print(i)
#		break