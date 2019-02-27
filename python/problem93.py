# This problem was asked by Apple.
# Given a tree, find the largest tree/subtree that is a BST.
# Given a tree, return the size of the largest tree/subtree that is a BST.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largestBST(node):
    if not node:
        return None, 0
    if not node.left and not node.right:
        return node, 1
    largestLeft, sizeLeft = largestBST(node.left)
    largestRight, sizeRight = largestBST(node.right)
    if largestLeft and largestRight:
        if largestLeft == node.left and largestRight == node.right \
            and node.left.value < node.value \
            and node.right.value > node.value:
            return node, sizeLeft + sizeRight + 1
    elif largestLeft and largestLeft == node.left \
        and node.left.value < node.value:
        return node, sizeLeft + 1
    elif largestRight and largestRight == node.right \
        and node.right.value > node.value:
        return node, sizeRight + 1
    if sizeLeft > sizeRight:
        return largestLeft, sizeLeft
    else:
        return largestRight, sizeRight

largest, count = largestBST(None)
print(largest, count) # Should print: None, 0

largest, count = largestBST(Node(1))
print(largest.value, count) # Should print: 1, 1

largest, count = largestBST(Node(2, Node(1)))
print(largest.value, count) # Should print: 2, 2

largest, count = largestBST(Node(1, right=Node(2)))
print(largest.value, count) # Should print: 1, 2

largest, count = largestBST(Node(1, left=Node(2)))
print(largest.value, count) # Should print: 2, 1

largest, count = largestBST(Node(2, right=Node(1)))
print(largest.value, count) # Should print: 1, 1

largest, count = largestBST(Node(2, Node(1), Node(3)))
print(largest.value, count) # Should print: 2, 3

largest, count = largestBST(Node(1, Node(2), Node(3)))
print(largest.value, count) # Should print: 3, 1

root = Node(4, Node(2, Node(1), Node(3)))
largest, count = largestBST(root)
print(largest.value, count) # Should print: 4, 4

root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(8), Node(7)))
largest, count = largestBST(root)
print(largest.value, count) # Should print: 2, 3

root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
largest, count = largestBST(root)
print(largest.value, count) # Should print: 4, 7

root = Node(4, Node(2, Node(1), Node(3, Node(2.5))), Node(6, Node(5), Node(7)))
largest, count = largestBST(root)
print(largest.value, count) # Should print: 4, 8
