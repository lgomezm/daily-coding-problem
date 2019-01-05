# This problem was asked by Google.
# Given an array of integers where every integer occurs three times
# except for one integer, which only occurs once, find and return 
# the non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. 
# Given [13, 19, 13, 13], return 19.

def problem40(array):
    occurences = {}
    for num in array:
        count = 1
        if num in occurences:
            if occurences[num]+1 == 3:
                del occurences[num]
            else:
                occurences[num] = 2
        else:
            occurences[num] = 1
    return list(occurences.keys())[0]

print(problem40([6, 1, 3, 3, 3, 6, 6]))