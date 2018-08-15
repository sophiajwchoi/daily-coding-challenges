from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def list_of_depths(root):
    returnList = []
    queue = deque()
    queue.append(root)

    
    while len(queue) != 0:
        l = list()
        count = len(queue)
        while count != 0:
            r = queue.popleft()
            node = Node(r.val)
            l.append(node)
            if (r.left != None):
                queue.append(r.left)
                
            if (r.right != None):
                queue.append(r.right)
            count -= 1


        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        if (len(l) != 0):
            l[len(l) - 1].next = None
        returnList.append(l)

    return returnList

def print_lists_of_Depths(l):
    for x in l:
        for y in x:
            print(y.val, end ="")
        print("")

def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    print_lists_of_Depths(list_of_depths(a))
        
    
