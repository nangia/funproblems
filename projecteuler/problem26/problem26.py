

def divseqhelper(numerator, denominator):
    quotient = numerator / denominator
    remainder = numerator % denominator
    while (remainder != 0):
        numerator = remainder * 10
        quotient = numerator / denominator
        remainder = numerator % denominator
        yield [quotient, remainder]

def checkindexinresult(number, thelist):
    index = 0
    for [quot, remainder] in thelist:
        if (remainder == number):
            return index
        index += 1
    return None
    

def computeresulthelper(numerator, denominator):
    if numerator == denominator:
        return [1, [], None]
    if (numerator > denominator):
        nondecimalpart = numerator / denominator
        numerator = numerator - (nondecimalpart * denominator)
    else:
        nondecimalpart = 0
    result = []
    index = None
    for [resultpart,remainder] in divseqhelper(numerator,denominator):
        if (remainder == 0):
            return [nondecimalpart, result.append([resultpart,remainder]), None]
        else:
            index = checkindexinresult(remainder, result)
            if index != None:
                return [nondecimalpart, result, index]
            else:
                result.append([resultpart,remainder])

def numrepeating(numerator, denominator):
    [nondecimal, fraction, index] = computeresulthelper(numerator, denominator)
    if index == None:
        return 0
    return len(fraction) - index
       
max = 0
maxindex = -1

for i in xrange(1,1000):
    computeresulthelper(1,i)
    cyclelen = numrepeating(1,i) 
    if cyclelen > max:
        max = cyclelen
        maxindex = i
print(maxindex)
