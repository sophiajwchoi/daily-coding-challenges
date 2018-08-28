##Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
##
##For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
##
##    1
##   / \
##  2   2
## / \ / \
##3  4 4  3
##But the following [1,2,2,null,3,null,3] is not:
##    1
##   / \
##  2   2
##   \   \
##   3    3
##Note:
##Bonus points if you could solve it both recursively and iteratively.
       
##Iterative approach with input as a list    
def is_Tree_Symmetric_with_Array(arr):
    stack = [arr[-1]]
    for i in range(-2, - len(arr) - 1, -1):
        if len(stack) == 0 or stack[-1] != arr[i] :
            stack.append(arr[i])
        else:
            stack.pop()
    if len(stack) == 1 and arr[0] == stack[0]:
        return True
    else:
        return False

##Recursive approach with Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def is_Tree_Symmetric_with_Root(root):
    if root == None:
        return
    else:
        return is_Tree_Symmetric_recursion(root.left, root.right)
def is_Tree_Symmetric_recursion(left, right):
    if left == None and right == None:
        return True
    if left.val != right.val:
        return True
    return is_Tree_Symmetric_recursion(left.left, right.right) and is_Tree_Symmetric_recursion(left.right, right.left) 



def main():
    is_Tree_Symmetric_with_Array([1,1,3])
    is_Tree_Symmetric_with_Array([1,2,2,None,3,None,3])
    is_Tree_Symmetric_with_Array([1,2,2,3,4,4,3])
    is_Tree_Symmetric_with_Array([1,None, None])
    a = Node(1)
    b = Node(2)
    c = Node(2)
    d = Node(3)
    e = Node(4)
    f = Node(4)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    is_Tree_Symmetric_with_Root(a)
    
    
