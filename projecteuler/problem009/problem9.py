


def breakintotwo(num):
    assert(num != 0)

    for i in xrange(1,num):
        yield(i, num - i)
            
def breakintothree(num):
    for i in xrange(1, num):
        for tuple in breakintotwo(num - i):
            yield (i, tuple[0], tuple[1])
            
            
def isPythagoreanTriplet(a,b,c):
    if a*a + b*b == c* c:
        return True
    return False

for a, b, c in breakintothree(1000):
    
    if isPythagoreanTriplet(a,b,c):
        print(a * b * c)
            
    
            