class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def deepestNodeInner(node, level):
    if node == None:
        return 0, 0
    if node.left == None and node.right == None:
        return node.value, level
    else:
        deepestR, levelR = deepestNodeInner(node.right, level+1)
        deepestL, levelL = deepestNodeInner(node.left, level+1)
        if levelL > levelR:
            return deepestL, levelL
        else:
            return levelR, levelR

def deepestNode(root):
    if root == None:
        raise ValueError("Invalid root")
    return deepestNodeInner(root, 1)[0]

root = Node("a", Node("b", Node("d")), Node("c"))
print(deepestNode(root))
