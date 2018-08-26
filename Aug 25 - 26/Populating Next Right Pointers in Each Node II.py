##Given a binary tree
##
##struct TreeLinkNode {
##  TreeLinkNode *left;
##  TreeLinkNode *right;
##  TreeLinkNode *next;
##}
##Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
##
##Initially, all next pointers are set to NULL.
##
##Note:
##
##You may only use constant extra space.
##Recursive approach is fine, implicit stack space does not count as extra space for this problem.
##
##
##

# Definition for binary tree with next pointer.
class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

from collections import deque

    # @param root, a tree link node
    # @return nothing
def connect(root):
    queue = deque()
    queue.append(root)
    while queue:
        length = len(queue)
        prev = None
        for i in range(length):
            curr = queue.popleft()
            if prev != None:
                prev.next = curr
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
            prev = curr
        curr.next = None

def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

def main():
    a = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    a.left = b
    a.right = c
    connect(a)
