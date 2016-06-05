d = dict()

for i in range(1,1000) :
	moduli = {0}
	w = 1
	while w < i:
		w *= 10
		
	while w not in moduli :
		moduli.add(w)
		w = w % i
		if w != 0 :
			while w < i :
				w *= 10
			
	d.update({i: len(moduli)})
	
print(d)
	
	