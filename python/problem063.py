# This problem was asked by Microsoft.
# 
# Given a 2D matrix of characters and a target word, 
# write a function that returns whether the word can be 
# found in the matrix by going left-to-right, or up-to-down.
# 
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']] 
# 
# and the target word 'FOAM', you should return true, since 
# it's the leftmost column. Similarly, given the target word 
# 'MASS', you should return true, since it's the last row.

def check_curr_char(matrix, word, i, j, count):
    if word[count] == matrix[i][j]:
        return count + 1
    elif word[0] == matrix[i][j]:
        return 1
    else:
        return 0

def is_word_present(matrix, word):
    word_length = len(word)
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        count = 0
        for j in range(cols):
            if word_length - count > cols - j:
                break
            count = check_curr_char(matrix, word, i, j, count)
            if count == len(word):
                return True
    for j in range(cols):
        count = 0
        for i in range(rows):
            if word_length - count > rows - i:
                break
            count = check_curr_char(matrix, word, i, j, count)
            if count == len(word):
                return True
    return False

matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]
print(is_word_present(matrix, "FOAM"))
print(is_word_present(matrix, "MASS"))

matrix = [['A', 'A', 'B', 'C'],
          ['O', 'A', 'Q', 'P'],
          ['A', 'B', 'D', 'E'],
          ['M', 'D', 'S', 'S']]
print(is_word_present(matrix, "BDE"))
print(is_word_present(matrix, "ABD"))
print(is_word_present(matrix, "BDB"))
print(is_word_present(matrix, "OAMA"))