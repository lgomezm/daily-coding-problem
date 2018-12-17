# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be 
# decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' 
# is not allowed.

def count_ways(message, k):
    if k == 0:
        return 1
    s = len(message) - k
    if message[s] == '0':
        return 0
    result = count_ways(message, k-1)
    if k >= 2 and int(message[s:s+2]) <= 26:
        result += count_ways(message, k-2)
    return result

def count_ways_to_decode(message):
    return count_ways(message, len(message))

print(count_ways_to_decode('2222'))