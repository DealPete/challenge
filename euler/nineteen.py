import datetime

d = datetime.date(1901,1,1)
t = datetime.timedelta(1)

c = 0

while d < datetime.date(2000,12,31) :
	if (d.weekday() == 6) and (d.day == 1) :
		c += 1
	d += t
