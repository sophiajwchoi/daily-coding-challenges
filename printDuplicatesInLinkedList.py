class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(a):
    elements = {}
    curr = a
    prev = None
    while (curr != None):
        if curr.data not in elements:
            elements[curr.data] = 0
        elements[curr.data] += 1

        if (elements[curr.data] > 1):
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    printNode(a)

def printNode(b):
    if (b != None):
        print(b.data)
    while (b.next != None):
        print(b.next.data)
        b = b.next
        
