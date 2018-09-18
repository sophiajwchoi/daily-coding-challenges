##remove a node from a doubly linked list?
##


def delete_Node_from_Doubly_LL(head, k):
    if k == None:
        return 
    curr = head
    while curr != None:
        if curr.next == k:
            curr.next = k.next
            k.next.prev = curr
            break
        else:
            curr = curr.next
        
    return print_node(head)

def print_node(head):
    while head != None:
        print(head.val)
        head = head.next

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    c.next = d
    d.prev = c
    delete_Node_from_Doubly_LL(a, c)
