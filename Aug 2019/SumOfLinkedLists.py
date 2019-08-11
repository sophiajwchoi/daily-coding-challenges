# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = head =  ListNode(0)
        cond = 0
        
        while (l1 or l2 or cond):
            v1,v2 = l1.val if l1 else 0, l2.val if l2 else 0

            if (v1 + v2 + cond > 10):
                cond = 1
            else:
                cond = 0
            curr.val = v1 + v2 + cond % 10
            l1, l2= l1.next if l1 else None, l2.next if l2 else None
            if (l1 or l2 or cond):
                curr.next = ListNode(0)
                curr = curr.next

        return head
    
