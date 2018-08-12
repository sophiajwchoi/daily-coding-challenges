class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def partitionLL(node, k):
    head = node
    tail = node
    
    while (node != None):
        nextNode = node.next
        if (node.val < k):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node

        node = nextNode
    tail.next = None

    printNode(head)

def printNode(a):
    while (a != None):
        print(a.val)
        a = a.next
