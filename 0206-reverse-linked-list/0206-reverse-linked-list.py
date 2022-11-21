# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        q=[]
        temp=head 
        while temp:
            q.append(temp)
            temp=temp.next
        
    
        temp=head=q.pop()
        while len(q)>0:
            temp.next=q.pop()
            temp=temp.next
        temp.next=None    
        return head   
            
            
        
        
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     