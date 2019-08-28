# This problem was asked by Epic.
#
# The "look and say" sequence is defined as follows: beginning with 
# the term 1, each subsequent term visually describes the digits 
# appearing in the previous term. The first few terms are as follows:
# 1
# 11
# 21
# 1211
# 111221
#
# As an example, the fourth term is 1211, since the third term consists
# of one 2 and one 1.
#
# Given an integer N, print the Nth term of this sequence.

def next_term(term):
    next = []
    prev = term[0]
    count_prev = 1
    for i in range(1, len(term)):
        curr = term[i]
        if curr != prev:
            next.append(count_prev)
            next.append(prev)
            prev = curr
            count_prev = 1
        else:
            count_prev += 1
    next.append(count_prev)
    next.append(prev)
    return next

def look_and_say(n):
    if n < 0:
        raise Exception('n must be greater than 0')
    elif n == 1:
        return "1"
    term = [1, 1]
    for _ in range(2, n):
        term = next_term(term)
    return ''.join([str(i) for i in term])
        
print(look_and_say(1))
print(look_and_say(2))
print(look_and_say(3))
print(look_and_say(4))
print(look_and_say(5))