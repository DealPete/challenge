trange = 10000
pentagonal = [(i * (3 * i - 1)) // 2 for i in range(1, trange)]
pn = set(pentagonal)

#for i in range(1, trange - 2) :
#	if pentagonal[i] + pentagonal[i + 1] in pn and pentagonal[i + 1] - pentagonal[i] in pn :
#		print([i,j])



for i in range(trange - 1) :
	for j in range(i, trange - 1) :
		if pentagonal[i] + pentagonal[j] in pn and pentagonal[j] - pentagonal[i] in pn :
			print([i,j])
			