# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        curr=dummy
        while curr.next and curr.next.next:
            fast=curr.next.next
            slow=curr.next
            slow.next=fast.next
            curr.next=fast
            curr.next.next=slow
            curr=curr.next.next
        return dummy.next    
        
        
        
        
        