# This problem was asked by Twitter.

# Given a list of numbers, create an algorithm that arranges 
# them in order to form the largest possible integer. For example, 
# given [10, 7, 76, 415], you should return 77641510.

import math
  
def build_number(numbers):
    n = 0
    digits = 1
    multiplier = 1
    for i in range(len(numbers)-1, -1, -1):
        n += numbers[i] * multiplier
        digits = int(math.log10(n))
        multiplier = 10 ** (digits+1)
    return n

def arrange(numbers):
    return arrange_rec(numbers, 0, len(numbers) - 1, 0)

def arrange_rec(nums, l, r, curr_max):
    if l==r: 
        return max(build_number(nums), curr_max)
    else: 
        for i in range(l,r+1): 
            nums[l], nums[i] = nums[i], nums[l] 
            curr_max = arrange_rec(nums, l+1, r, curr_max) 
            nums[l], nums[i] = nums[i], nums[l]
    return curr_max
 
print(arrange([10, 7, 76, 415]))