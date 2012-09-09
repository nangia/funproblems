

def triangleseq(n):
    # The infinite sequence of triangular numbers
    while (1):
        yield n*(n+1)/2
        n += 1
        
def pentagonalseq(n):
    # The infinite sequence of pentagonal numbers
    while(1):
        yield n*(3*n-1)/2
        n +=1
        
def hexagonalseq(n):
    # The infinite sequence of hexagonal numbers
    while(1):
        yield n*(2*n-1)
        n += 1
        
def seqmatcher(seqa, seqb):
    # Given two infinite sequences, this gives an infinite sequence where of matching
    # numbers of these two sequences
    a = seqa.next()
    b = seqb.next()
    while (1):
        if (a == b):
            yield a
            a = seqa.next()
            b = seqb.next()
        elif (a < b):
            a = seqa.next()
        else:
            b = seqb.next()

def pentagonalandhexagonalseq(n):
    # The infinite sequences of numbers which are pentaonal and hexagonal
    return seqmatcher(pentagonalseq(n), hexagonalseq(n))

def pentagonalandhexagonalandtriangularseq(n):
    # The infinite sequence of numbers that are triangle, pentagonal and hexagonal
    return seqmatcher(pentagonalandhexagonalseq(n), triangleseq(n))

for x in pentagonalandhexagonalandtriangularseq(1):
    if x > 40755:
        print x
        break 
