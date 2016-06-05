import integer

t, y = 1, set()
m = 0

while len(y) < 500 :
	y = integer.factor(integer.triangle(t))
	if len(y) > m :
		m = len(y)
		print("The factors of", integer.triangle(t), "are", y)
		print("It has", m, "factors.")
		input()		
	t += 1
