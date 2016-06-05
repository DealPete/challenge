pt = set()

for m in range(2,21) :
	for n in range(1, m) :
		for k in range(1, 1000 // (2*m*(m + n))) :
			pt.add((k*(m*m - n*n), k*2*m*n, k*(m*m + n*n)))

print(pt)

d = {}

for t in pt :
	if sum(t) in d :
		d[sum(t)] += 1
	else :
		d[sum(t)] = 1

print(d)