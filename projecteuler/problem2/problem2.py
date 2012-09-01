

def fibsequence():
	yield 1
	yield 2
	num = 2
	prev = 1
	while (1):
		num, prev = (num + prev), num
		yield num
		

sum = 0
for i in fibsequence():
	if i > 4000000:
		break
	if (i% 2 == 0):
		sum+= i
print sum	
