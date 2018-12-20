# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where 
# all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_unival_trees(node):
    if not node:
        return False, 0, -1
    elif not node.left and not node.right:
        return True, 1, node.value
    else:
        is_unival_l, count_l, value_l = count_unival_trees(node.left)
        is_unival_r, count_r, value_r = count_unival_trees(node.right)
        if is_unival_l and is_unival_r and node.value == value_l and node.value == value_r:
            return True, 1+count_l+count_r, node.value
        elif is_unival_l and not node.right and node.value == value_l:
            return True, 1+count_l, node.value
        elif is_unival_r and not node.left and node.value == value_r:
            return True, 1+count_r, node.value
        else:
            return False, count_l+count_r, -1


print(count_unival_trees(Node(1)))
print(count_unival_trees(Node(1).left))
print(count_unival_trees(Node(0, left=Node(1), right=Node(0, left=Node(1, Node(1), Node(1)), right=Node(0)))))