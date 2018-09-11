##Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
##
##Example:
##Given a binary tree 
##          1
##         / \
##        2   3
##       / \     
##      4   5    
##Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
##
##Note: The length of path between two nodes is represented by the number of edges between them.

class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def diameter_BST(root):
    if root != None:
        l_height = getHeight(root.left)
        r_height = getHeight(root.right)

        l_diameter = diameter_BST(root.left)
        r_diameter = diameter_BST(root.right)

    else:
        return 0
    return max(l_height + r_height, max(l_diameter, r_diameter))


def getHeight(node):
    if node == None:
        return 0
    else:
        return 1 + max(getHeight(node.left), getHeight(node.right))


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    print(diameter_BST(a))
