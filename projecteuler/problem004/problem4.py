

# put each digit in array (in reverse order) and total length of array
def convertoreversedarray(num):
    result = []
    len = 0
    while (num != 0):
        remainder = num % 10
        num /= 10
        len += 1
        result.append(remainder)
    return (result, len)
        


def isPalindrome(num):
    reversedarray, len = convertoreversedarray(num)
    halflen = len /2 
    for i in xrange(halflen):
        #print reversedarray[i]
        #print reversedarray[len - i-1]
        if reversedarray[i] != reversedarray[len - i-1]:
            return False
    return True

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest = 1
for i in xrange(101, 1000):
    for j in xrange(101, 1000):
        product = i * j
        if isPalindrome(product):
            if product > largest:
                largest = product
if largest != 1:
    print largest
else:
    print "None"
                
            
            