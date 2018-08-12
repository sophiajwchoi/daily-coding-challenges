def minimalTree(arr):
    index = len(arr) // 2
    root = arr[index]
    insert_BST(None, root)
    for x in arr:
            insert_BST(root, x)
    printBST(root)

def printBST(root):
    if root != None:
        print(root.val)
        printBST(root.left)
        printBST(root.right)

def insert_BST(root, child):
    if root == None:
        root = child
    if root.val < child.val:
        if root.right != None:
            insert_BST(root.right, child)
        else:
            root.right = child
    elif root.val > child.val:
        if root.left != None:
            insert_BST(root.left, child)
        else:
            root.left = child

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def main():
    
    a = Node(2)
    b = Node(1)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    array = [b,a,c,d, e]
    minimalTree(array)        


