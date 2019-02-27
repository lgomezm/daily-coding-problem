# This problem was asked by Microsoft.
# Suppose an arithmetic expression is given as a binary tree. 
# Each leaf is an integer and each internal node is one of 
# '+', '−', '∗', or '/'.
# Given the root to such a tree, write a function to evaluate it.
# For example, given the following tree:
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
def evaluate(root):
    if root:
        if not root.left and not root.right:
            return root.value
        if root.value == '+':
            return evaluate(root.left) + evaluate(root.right)
        elif root.value == '-':
            return evaluate(root.left) - evaluate(root.right)
        elif root.value == '*':
            return evaluate(root.left) * evaluate(root.right)
        elif root.value == '/':
            return evaluate(root.left) / evaluate(root.right)
    return 0

root = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
print(evaluate(root))