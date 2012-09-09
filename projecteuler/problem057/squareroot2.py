

def numofdigits(num):
	if num == 0:
		return 1
	result = 0
	while num != 0:
		result += 1
		num /= 10
	return result


def squareroottwoseq():
	#[1; 2, 2, 2 ....] 
	yield 1
	while (1):
		yield 2


def continuedfraccalc(infiniteseq):
	# p(i) = a(i)p(i-1) + pi-2 
	# qi = aiqi-1 + qi-2 
	# p-1 = 0, p0 = 1, q-1 = 1, and q0 = 0.
	first = True
	for a in infiniteseq():
		if first:
			p = a # p(1)
			q = 1 # q(1)
			plast = 1 # plast = p0
			qlast = 0 # q(0)
			plasttolast = 0 # p(-1)
			qlasttolast = 1 # q(-1)

			first = False
		else: 
			p, plast, plastlast = (a * p + plast), p, plast
			q, qlast, qlastlast = (a * q + qlast), q, qlast
		yield (p, q)
		
			

if __name__ == "__main__":
	num = 1
	count = 0
	for (numerator, denominator) in continuedfraccalc(squareroottwoseq):
		if num > 1000:			
			break
		if numofdigits(numerator) > numofdigits(denominator):
			count += 1
		num += 1
	print count
		

	
