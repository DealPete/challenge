from integer import primes
from itertools import combinations

p = primes(1000000)

def fours() :
	for i in {1, 7} :
		pr = set()
		for j in range(10) :
			k = int(str(j) * 3 + str(i))
			if k in p :
				pr.add(k)
		print(pr)

def fives() :
	for i in range(10) :
		for j in {1, 3, 7, 9} :
			for k in range(4) :
				pr = set()
				for m in range(10) :
					l = str(m) * 3 + str(j)
					l = l[:k] + str(i) + l[k:]
					l = int(l)
					if l in p :
						pr.add(l)
				if pr :
					print(pr)
					
def sixes() :
	for i in combinations({0, 1, 2, 3, 4}, 2) :
		for x1 in range(10) :
			for x2 in range(10) :
				for j in {1, 3, 7, 9} :
					pr = set()
					for k in range(10) :
						l = str(k) * 3 + str(j)
						l = int(l[:i[0]] + str(x1) + l[i[0]:i[1]] + str(x2) + l[i[1]:])
						if l in p :
							pr.add(l)
					if len(pr) == 8 :
						print(pr)