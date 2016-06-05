for i in range(2,9999999) :
	t = 0
	for j in str(i) :
		t += int(j)**6
	if t == i :
		print(i)
		