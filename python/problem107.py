# This problem was asked by Microsoft.
# 
# Print the nodes in a binary tree level-wise. For example, 
# the following should print 1, 2, 3, 4, 5.
#   1
#  / \
# 2   3
#    / \
#   4   5

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def print_by_levels(root):
    if not root:
        return
    curr_level = [root]
    while curr_level:
        next_level = []
        for node in curr_level:
            print(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        curr_level = next_level

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_by_levels(root)