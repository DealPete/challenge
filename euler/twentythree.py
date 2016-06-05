import integer

abun = set()
perf = set()
defic = set()

for i in range(1,28123) :
	s = integer.d(i)
	if s < i :
		defic.add(i)
	elif s > i :
		abun.add(i)
	else :
		perf.add(i)

cant = set()

for i in range(1, 28123) :
	can = False
	for j in range(12, i) :
		if j in abun and i - j in abun :
			can = True
			break
	if not can :
		cant.add(i)

print(sum(cant))