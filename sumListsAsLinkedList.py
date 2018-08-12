class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sumLists(a, b):
    stack = []
    while (a != None || b != None || carry != False):
        carry = False
        remainder = (a + b) % 10
        stack.append(remainder)
        div = (a + b) / 10
        if (div >= 1):
            carry = True
        nextANode = a.next
        if (nextANode != None):
            nextANode.val += 1
        nextBNode = b.next
        elif (nextBNode != None):
            nextBNode.val += 1

    fo


    
