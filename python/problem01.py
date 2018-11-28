# This problem was recently asked by Google.
# Given a list of numbers and a number k, return 
# whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.

def evaluate(numbers, k):
    visited = set()
    for n in numbers:
        if k - n in visited:
            return True
        visited.add(n)
    return False

line = input()
k = int(input())
numbers = []
for s in line.split(' '):
    numbers.append(int(s))
print(evaluate(numbers, k))