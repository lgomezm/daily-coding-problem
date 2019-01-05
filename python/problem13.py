# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest 
# substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring 
# with k distinct characters is "bcb".

def solution(text, k):
    max_length = float('-inf')
    for i in range(len(text)):
        curr_length = 0
        seen = set()
        j = i
        while j < len(text) and len(seen) <= k:
            seen.add(text[j])
            curr_length += 1
            j += 1
        if curr_length - 1 > max_length:
            max_length = curr_length - 1
    return max_length

print(solution('abcbabdaabcd', 3))