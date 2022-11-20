# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        dummy=ListNode(0,prev)   
        left=dummy
        while n>1:
            left=left.next
            
            n-=1
        left.next=left.next.next 
        
        newList=dummy.next
        prevList=None
        while newList:
            cur=newList
            newList=newList.next
            cur.next=prevList
            prevList=cur
        

        
        return prevList
            
        
    
            
            
        
        