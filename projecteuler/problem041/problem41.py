

# check if num is divisible by any of the primes so far
def check_divisible_by_primes(num, primelist):
    for aprime, aprimesquare in primelist:
        if (num % aprime == 0):
            # this is divisible by a prime already existing
            # so cannot be prime
            return True
        if (aprimesquare >= num):
            # this means that aprime is already greater than square root of num
            return False
    return False

# generates an infinite sequence of prime number and its square
def primenumberanditssquaregenerator():
    primessofar = [(2,4), (3,9)]
    yield (2,4)
    yield (3,9)
    num = 4
    while(1):
        if not check_divisible_by_primes(num,primessofar):
        # found a prime
        # add to end of primesofar list
            numsquare = num * num
            resulttuple = (num, numsquare)
            primessofar.append(resulttuple)
            yield resulttuple 
        num += 1   
     
def numofdigits(num):
    if num == 0:
        return 1
    count = 0
    while (num != 0):
        count += 1
        num /= 10
    return count
           
   
def num2array(num):
    if num == 0:
        return [0]
    result = []
    while (num != 0):
        remainder = num % 10
        num = num / 10
        result.append(remainder)
    result.sort()
    return result
        

def checkequal(a,b):
    if len(a) != len(b):
        return False
    for i in xrange(len(a)):
        if a[i] != b[i]:
           return False
    return True
        
def ispandigital(num):
    return checkequal(num2array(num), range(1,numofdigits(num)+1)) 
  
  
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""    
lastprime = 1
for prime, primesquare in primenumberanditssquaregenerator():
    # if prime is greater then 9 digits, then we are done
    if prime > 999999999:
        break
    if ispandigital(prime):
        lastprime = prime
        print(lastprime)

print(lastprime)
    
