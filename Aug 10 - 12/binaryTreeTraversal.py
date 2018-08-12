class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if (root.val > node.val):
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        elif (root.val < node.val):
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)
                
def inOrder(root):
    if (root != None):
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

def preOrder(root):
    if (root != None):
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if (root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)

    
