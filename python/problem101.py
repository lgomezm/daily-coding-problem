# This problem was asked by Alibaba.
#
# Given an even number (greater than 2), return two prime 
# numbers whose sum will be equal to the given number.
#
# A solution will always exist. See Goldbach’s conjecture
# (https://en.wikipedia.org/wiki/Goldbach%27s_conjecture).
#
# Example:
# Input: 4
# Output: 2 + 2 = 4

# If there are more than one solution possible, return the 
# lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c, d] is another 
# solution with c <= d, then [a, b] < [c, d] if 
# a < c OR a==c AND b < d.

import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def eval(n):
    if n <= 2 or n % 2 != 0:
        raise ValueError("Input must be an even number greater than 2")
    for i in range(2, int(n/2) + 1):
        j= n - i
        if isPrime(i) and isPrime(j):
            return i, j
    return -1, -1 # Execution should never reach this line.

print(eval(4)) # should print 2, 2
print(eval(6)) # should print 3, 3
print(eval(8)) # should print 3, 5
print(eval(10)) # should print 5, 5
print(eval(12)) # should print 5, 7
print(eval(100)) # should print 3, 97