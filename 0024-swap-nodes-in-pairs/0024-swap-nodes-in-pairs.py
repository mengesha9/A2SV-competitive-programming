# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        curr=head
        prev=dummy
        
        while curr and curr.next:
            
            first=curr.next
            second=curr.next.next
            
            first.next=curr
            curr.next=second
            prev.next=first
            
            prev=curr
            curr=second
            
            
        return dummy.next    
        
        
        
        
        