# This problem was asked by Facebook.
#
# There is an N by M matrix of zeroes. Given N and M, write a function 
# to count the number of ways of starting at the top-left corner and 
# getting to the bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there 
# are two ways to get to the bottom-right:
#  Right, then down
#  Down, then right
# 
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

def count_ways(n, m):
    arr_len = min(n, m)
    times = max(n, m) - 1
    previous = [ 1 for i in range(arr_len) ]
    current = [ 1 for i in range(arr_len)]
    for _ in range(times):
        current[arr_len-1] = 1
        i = arr_len - 2
        while i >= 0:
            current[i] = current[i+1] + previous[i]
            i -= 1
        previous = current
    return previous[0]

print(count_ways(5, 5))