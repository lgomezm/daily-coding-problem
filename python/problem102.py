# This problem was asked by Lyft.
# 
# Given a list of integers and a number K, return which 
# contiguous elements of the list sum to K.
# 
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, 
# then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

from collections import deque

def find_contiguous_sum(numbers, k):
    i, sum = 0, 0
    contiguous = deque([])
    while i < len(numbers) and sum < k:
        n = numbers[i]
        if sum + n <= k:
            contiguous.append(n)
            sum += n
            i += 1
        elif contiguous:
            sum -= contiguous.popleft()
    if sum == k:
        return contiguous
    return []

print(find_contiguous_sum([1, 2, 3, 4, 5], 9))
print(find_contiguous_sum([1, 2, 3, 4, 5], 7))
print(find_contiguous_sum([1, 2, 3, 4, 5], 10))
print(find_contiguous_sum([1, 2, 3, 4, 5], 11))