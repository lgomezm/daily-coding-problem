# This problem was asked by Microsoft.
# 
# Given an unsorted array of integers, find the length 
# of the longest consecutive elements sequence.
# 
# For example, given [100, 4, 200, 1, 3, 2], the longest 
# consecutive element sequence is [1, 2, 3, 4]. Return 
# its length: 4.
# 
# Your algorithm should run in O(n) complexity.

def longest_seq(numbers):
    s = set()
    for n in numbers:
        s.add(n)
    max_length = 1
    for n in numbers:
        prev = n - 1
        next = n + 1
        length = 1
        while prev in s:
            s.remove(prev)
            prev -= 1
            length += 1
        while next in s:
            s.remove(next)
            next += 1
            length += 1
        max_length = max(max_length, length)
    return max_length

print(longest_seq([100, 4, 200, 1, 3, 2]))