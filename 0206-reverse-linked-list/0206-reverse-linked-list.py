# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev=None
        
        if head == None:
            return head
        
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not head:
#             return None
#         newHead=head
#         if head.next:
#             newHead=self.reverseList(head.next)
#             newHead.next.next=
            
            
        
        
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     