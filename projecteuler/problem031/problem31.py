
def coincombo(total, coincombinationlist):
	if len(coincombinationlist) == 1:
		div = total / coincombinationlist[0]
		rem = total % coincombinationlist[0]
		if rem == 0:
			denomination = coincombinationlist[0]
			thetuple = ( div,  denomination)
			yield [ thetuple ]
	else:
		firstcoin = coincombinationlist[0]
		restlist = coincombinationlist[1:]
		
		maxfirstcoins = total / firstcoin
		rem = total % firstcoin
		
		for firstcoinnumber in xrange(0, maxfirstcoins + 1):
			remainingamount = total - (firstcoinnumber * firstcoin)
			for remresult in coincombo(remainingamount, restlist):
				remresult.insert(0, (firstcoinnumber, firstcoin))
				yield  remresult
			
total = 200
#coins = [1, 2, 5, 10, 20, 50, 100, 200]
# resuls are much faster if you put these in reverse order
coins = [200, 100, 50, 20, 10, 5, 2, 1]
count = 0
for combination in coincombo(total, coins):
	count += 1
	#print combination
print(count)
