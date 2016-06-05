def palin():
	t, u, v = 999, 999, True
	while v :
		w = ((t*u) % 10) * 100 + ((t*u % 1000) // 100) + (((t*u) % 100) // 10) * 10
		if (t * u) < 100000 :
			u = 999
			t = t - 1
		elif ((t * u) // 1000 == w) :
			print (t, u, t * u, w)
			if t < 900 :
				v = False
		u = u - 1
	
