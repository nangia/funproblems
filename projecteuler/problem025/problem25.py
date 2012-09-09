

def fibseq():
	yield 1
	yield 1
	last = 1
	lastlast = 1
	while (1):
		last, lastlast = (last + lastlast), last
		yield last
		
def numdigits(num):
	if num == 0:
		return 1
	count = 0
	while (num != 0):
		count += 1
		num /= 10
	return count
	
term = 0
for fibnum in fibseq():
	fibnumdigits = numdigits(fibnum)
	term += 1
	if  fibnumdigits >= 1000:
		print term, fibnumdigits
		break
	

		
		