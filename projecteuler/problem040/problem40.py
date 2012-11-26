#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789 10111213141516171819 2021...
# 
#It can be seen that the 12th digit of the fractional part is 1.
# 
#If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
#d1 d10 d100 d1000 d10000 d100000 d1000000



def sublistseq(num):
	numstr = str(num)
	for x in numstr:
		yield int(x)
	

def irrationanumberseq():
	for i in xrange(1,10):
		yield i
	insertnum = 1
	while True:
		for j in xrange(0,10):
			# put elements from sublistseq(insertnum)
			for subelem in sublistseq(insertnum):
				yield subelem
			yield j
		insertnum += 1

numsofinterest = [1,10,100,1000,10000,100000,1000000]
iter = 1
product = 1
for x in irrationanumberseq():
	if iter in numsofinterest:
		print iter, x
		product *= x
	if iter == numsofinterest[-1]:
		break
	iter += 1
print product
	