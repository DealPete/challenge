def cancel(num, denom) :
	for n in num[:] :
		if n in denom :
			num.remove(n)
			denom.remove(n)
	return (num, denom)

def permute(l) :

	if len(l) == 1 :
		yield l
		
	for i in range(len(l)) :
		for j in permute(l[:i] + l[i+1:]) :
			yield [l[i]] + j
		