# This question was asked by Apple.
# Given a binary tree, find a minimum path sum from root to a leaf.
# For example, the minimum path in this tree is [10, 5, 1, -1], 
# which has sum 15.
#
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_min_path_sum(root):
    return find_min_path_sum_rec(root, 0)

def find_min_path_sum_rec(node, sum):
    if not node:
        return sum
    sum += node.value
    if not node.left and not node.right:
        return sum
    return min(find_min_path_sum_rec(node.left, sum), find_min_path_sum_rec(node.right, sum))

root = Node(10, Node(5, right=Node(2)), Node(5, right=Node(1, Node(-1))))
print(find_min_path_sum(root)) # Should print 15
root = Node(1, Node(2, Node(6), Node(7)), Node(3, Node(3), Node(5)))
print(find_min_path_sum(root)) # Should print 7