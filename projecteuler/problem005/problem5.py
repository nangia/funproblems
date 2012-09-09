
"""
Function Euclid(a,b)
if b = 0 return a
return(Euclid(b; a(modb)))
end Euclid.
"""
def gcd(a,b):
    while(b!=0):
        a, b = b, (a % b)
    return a

def lcm(a,b):
    return a * b / gcd(a,b)




# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

lcmsofar = 1
for i in xrange(1,21):
    lcmsofar = lcm(lcmsofar, i)
print lcmsofar
    