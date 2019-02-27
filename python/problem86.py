# This problem was asked by Google.

# Given a string of parentheses, write a function to compute 
# the minimum number of parentheses to be removed to make the 
# string valid (i.e. each open parenthesis is eventually closed).
# 
# For example, given the string "()())()", you should return 1. 
# Given the string ")(", you should return 2, since we must 
# remove all of them.

def countToRemove(text):
    parens = []
    count = 0
    for c in text:
        if c == ')':
            if len(parens) > 0:
                parens.pop()
            else:
                count += 1
        else:
            parens.append(c)
    return count + len(parens)

print(countToRemove("()())()")) # should print 1
print(countToRemove(")(")) # should print 2
print(countToRemove("(((()())))()))")) # should print 2