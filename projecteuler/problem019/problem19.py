


def isLeap(year):
	# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

	
def daysInMonth(month, year):
	""" Thirty days has September,
	 April, June and November. (9, 4, 6, 11)
	 All the rest have thirty-one,
	 Saving February alone, (2)
	 rest (31)
	"""	
	if (month == 4) or (month == 6) or (month == 9) or (month == 11):
		return 30
	elif (month == 2):
		if isLeap(year):
			return 29
		else:
			return 28
	else:
		return 31

def daysInYear(year):
	if isLeap(year):
		return 366
	return 365
		
def dayDifference(d,m,y):
	# how many days ahead is this date from 01-Jan-1900
	assert(y >= 1900)
	assert(d >= 1)
	assert(d <= daysInMonth(m,y))
	assert( (m>=1) and (m<=12))
	
	# sum of days till (y  - 1) starting year 1900
	sum = 0
	for theyear in xrange(1900, y):
		sum += daysInYear(theyear)
	
	# sum up the days before this month 
	for themonth in xrange(1, m):
		sum += daysInMonth(themonth, y)
	sum += d
	sum -= 1
	return sum
	
	
	
	

"""
You are given the following information, but you may prefer to do some research for yourself.
 1 Jan 1900 was a Monday.
 Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
 A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

sunday_count = 0
for year in xrange(1901, 2001):
	for month in xrange(1, 13):
		if 6 == (dayDifference(1, month, year) % 7):
			sunday_count += 1
			
print sunday_count

