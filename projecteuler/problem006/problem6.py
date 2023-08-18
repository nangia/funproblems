



def sumofsquares(n):
    sum = 0
    for i in xrange(1,n+1):
        sum += i * i
    return sum
    
    
def squareofsum(n):
    sum = 0
    for i in xrange(1,n+1):
        sum += i
    return sum * sum


#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print(sumofsquares(100) - squareofsum(100))