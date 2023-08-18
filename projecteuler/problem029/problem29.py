
store = {}

last = 100 + 1

for a in xrange(2, last):
	for b in xrange(2,last):
		store[pow(a,b)] = 1
print(len(store))