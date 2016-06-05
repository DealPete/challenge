from rationals import newton_square_root

total = 0

for i in [x for x in range(1,101) if not x in [1,4,9,16,25,36,49,64,81,100]] :
	(num, denom) = newton_square_root(i,11)
	num *= 10**101
	k = num // denom
	l = str(k)
	n = sum([int(z) for z in l[:100]])
	total += n
	print("Done", i, " Total =", total)
	
print(total)