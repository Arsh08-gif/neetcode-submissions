# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        prev = None
        curr = head
        nxt = head.next

        while(curr != None):
            curr.next = prev
            prev = curr
            curr = nxt
            if curr != None:
                nxt = curr.next
        
        return prev
        