# This problem was asked by Facebook.
# Given a positive integer n, find the smallest number of squared 
# integers which sum to n.
# For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.
# Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.

import math 

def is_integer(n):
    return n % 1 == 0

def decompose(n):
    if n <= 0:
        raise Exception('n should be greater than 0')
    elif n in [1, 2, 3]:
        return n
    sqr_root = math.sqrt(n)
    if is_integer(sqr_root):
        return 1
    min_count = float('inf')
    for i in range(4, n):
        sqr_root = math.sqrt(i)
        if is_integer(sqr_root):
            count = 1 + decompose(n - i)
            if count < min_count:
                min_count = count
    return min_count

print(decompose(13))
print(decompose(27))
print(decompose(20))
print(decompose(120))
