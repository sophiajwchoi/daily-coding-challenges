#Delete the middle node of a linkedList

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteMidNode(c):
    d = c.next
    c.val = d.val
    c.next = d.next

def printNode(a):
    while (a != None):
        print(a.val)
        a = a.next
