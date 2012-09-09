
def fact(n):
    product = 1
    while (n != 0):
        product *= n
        n -= 1
    return product

def ncr(n, r):
    return fact(n)/(fact(r))/(fact(n-r))

count = 0
for n in xrange(1, 101):
    for r in xrange(0,n+1):
        if ncr(n,r) > 1000000:
            count += 1
print count