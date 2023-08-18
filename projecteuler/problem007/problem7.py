




# check if num is divisible by any of the primes so far
def check_divisible_by_primes(num, primelist):
    for aprime in primelist:
        if (num % aprime == 0):
           # this is divisible by a prime already existing
           # so cannot be prime
           return True
    return False

def primenumbergenerator():
    primessofar = [2, 3]
    yield 2
    yield 3
    num = 4
    while(1):
        if not check_divisible_by_primes(num,primessofar):
        # found a prime
        # add to end of primesofar list
            primessofar.append(num)
            yield num
        num += 1      

#What is the 10 001st prime number?

num = 10001
for aprime in primenumbergenerator():
    num -= 1
    if num == 0:
        print(aprime)
        break