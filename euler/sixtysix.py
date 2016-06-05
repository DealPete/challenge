from itertools import count
from rationals import *

def is_square(apositiveint):
  if apositiveint == 1 :
    return True
  if apositiveint/1 != apositiveint//1 :
    return False
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True
  
l_num = 0
lx_value = 0
ly_value = 0

for i in [x for x in range(1,1001) if not is_square(x)] :
	for j in count(1) :
		(x, y) = nth_convergent(i, j)
		if x**2 - i * y**2 == 1 :
			print("For i =", i, "the minimal solution is x =", x)
			if lx_value < x :
				l_num = i
				lx_value = x
				ly_value = y
			break

print("The largest x value is {} for D = {}. y = {}".format(lx_value, l_num, ly_value))
		