# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive 
# integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.

You can modify the input array in-place.

def findSmallestNotContained(numbers):
	s = set()
	max = 0
	for n in numbers:
		if n > 0:
			s.add(n)
			if n > max:
				max = n
	for i in range(1, max):
		if not i in s:
			return i
	return max+1

line = input()
numbers = []
for s in line.split(' '):
    numbers.append(int(s))
print(findSmallestNotContained(numbers))