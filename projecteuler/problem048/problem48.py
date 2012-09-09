


def pow(a,b):
	product = 1
	while (b != 0):
		product *= a
		b -= 1
	return product
	
sum = 0
for i in xrange(1,1001):
	sum += pow(i,i)
print sum % 10000000000