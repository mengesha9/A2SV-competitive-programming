# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast=head.next
        slow=head
        
        while head and head.next:
            fast=fast.next.next
            slow=slow.next
        n=slow.next
        slow.next=prev=None

        while n:
            cur=n
            n=n.next
            prev=cur
            cur=n.next
        slow=head    
           
        while slow and prev:
            temp1,temp2=slow.next,prev.next
            slow.next=prev
            prev.next=slow.next
            prev.next=temp2
            slow.next=temp1
            
            
            
            
            
            
            
            
       
    
    
  










    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        
        slow = head
        fast = head.next
        
		# Find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        n = slow.next
        slow.next = prev = None
        
		# Reverse the second half
        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp
            
        slow = head
        
		# Join first and second half
        while slow and prev:
            
            tmp1 = slow.next
            tmp2 = prev.next
            slow.next = prev
            prev.next = tmp1
            slow = tmp1
            prev = tmp2
        
        return head
        
        # An Upvote will be encouraging
        