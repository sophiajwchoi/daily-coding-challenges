##is a binary tree balanced?
##A binary tree is balanced if for each node it holds that the number of inner nodes
##in the left subtree and the number of inner nodesin the right subtree differ by at most 1.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def is_balanced(root):
    if root is None:
        return True
    return (is_balanced(root.right) and is_balanced(root.left) \
            and abs(getHeight(root.left) - getHeight(root.right)) <= 1)

