##Write a function to find the 2nd largest element in a binary search tree. ↴
##
##Here's a sample binary tree node class:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_2nd_largest_BST(root):
    if root != None:
        first = root.val
        second = root.val
        search(first, second, root)
    else:
        return None
    

def search(first, second, root):

    if root != None:
        print(root.val)
        print(first)
        print(second)
        if root.val > first:
            temp = first
            first = root.val
            second = temp
        if root.val < first and root.val > second:
            second = root.val
        search(first, second, root.left)
        search(first, second, root.right)
        ##debugging required
    else:
        return

    return second

def main():
    a = Node(3)
    b = Node(1)
    c = Node(8)
    d = Node(9)
    e = Node(2)
    a.left = b
    a.right = c
    b.left = d
    d.right = e
    find_2nd_largest_BST(a)
