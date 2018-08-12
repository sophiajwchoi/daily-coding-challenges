#Detect a loop in a linkedList

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detectLoop(a):
    nodeMap = {}
    curr = a
    while curr != None:
        if curr not in nodeMap:
            nodeMap[curr] = 0
        else:
            return True
        nodeMap[curr] += 1
        curr = curr.next

    return False
