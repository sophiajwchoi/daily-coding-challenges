class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def kthLastElement(head, k):
    stack = []
    curr = head
    while (curr != None):
        stack.append(curr)
        curr = curr.next
    i = 0
    while (i < k):
        PoppedNode = stack.pop()
        i += 1
    print (PoppedNode.val)
