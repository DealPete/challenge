from functools import reduce

max_k = 12000

p = lambda x : reduce(lambda y, z : y * z, x)
s = lambda x : reduce(lambda y, z : y + z, x)
factors = [2, 2]
cur_factor = 0
mini = { x : 0 for x in range(2, max_k + 1)}

cont = True

while cont :
	prod = p(factors)
	d = prod - s(factors)
	leng = len(factors) + d
	if leng > max_k :
		if factors[cur_factor] == 2 :
			cont = False
		cur_factor += 1
		if cur_factor == len(factors) :
			factors += [2]
		else :
			factors[cur_factor] += 1
		for z in range(cur_factor) :
			factors[z] = factors[cur_factor]
	else :
		if not mini[leng] or mini[leng] > prod :
			mini[leng] = prod
			#print("Minimum of length", leng, "is", prod, "for factors", factors)
		factors[0] += 1
		cur_factor = 0

minset = { mini[x] for x in mini.keys() }		
print(s(minset))