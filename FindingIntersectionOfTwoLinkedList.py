class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def intersect(a, b):
    currA = a
    currB = b
    while (currA != None):
        while (currB != None):
            if currA == currB:
                print(str(currA.val) + "intersect")
                break
            else:
                currB = currB.next

        currB = b
        currA = currA.next
