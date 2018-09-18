##Write a function to find the 2nd largest element in a binary search tree. 
##
##Debugging in process

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_insert(root, node):
    if root:
        if root.val < node.val:
            if root.left != None:
                binary_insert(root.left, node)
            else:
                root.left = node
        if root.val > node.val:
            if root.right != None:
                binary_insert(root.right, node)
            else:
                root.right = node
    else:
        root = node
        
def find_largest_BST(root):          
    if root:
        curr = root

        while curr:
            if not curr.right:
                return curr.val
            curr = curr.right
            
def find_2nd_largest_BST(root):

    if root != None and (root.left != None and root.right != None):
            search(first, second, root.left)
            if root.val > first:
                temp = first
                first = root.val
                second = temp
            if root.val < first and root.val > second:
                second = root.val
            search(first, second, root.right)
            ##debugging required
        else:
            return
        search(first, second, root.right)

        return second

def search2(li, root):

    if root != None:
        li.append(root)
        search2(li, root.left)
        search2(li,root.right)

    return li

def main():
    a = Node(3)
    b = Node(1)
    c = Node(8)
    d = Node(9)
    e = Node(2)
    binary_insert(a, b)
    binary_insert(a, c)
    binary_insert(a, d)
    binary_insert(a, e)
    li = []
    li = search2(li, a)
    print(li[-2])
