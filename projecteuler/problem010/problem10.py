

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


#Find the sum of all the primes below two million.
sum = 0
for aprime, aprimesquare in primenumberanditssquaregenerator():
    if aprime > 2000000:
        break
    #print aprime
    sum += aprime
print(sum)