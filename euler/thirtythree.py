import fractions
from algebra import cancel
from integer import digitsToNumber

for i in range(10,99) :
	for j in range(i + 1, 100) :
		if i % 10 and j % 10 :
			f = cancel(list(str(i)), list(str(j)))
			f0 = digitsToNumber(f[0])
			f1 = digitsToNumber(f[1])
			if 0 < f0 < 10 and 0 < f1 < 10 :
				if fractions.Fraction(f0, f1) == fractions.Fraction(i, j) :
					print (i, j)