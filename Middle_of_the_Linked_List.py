# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        end=head
        beg=head
        while end:
            
            if end.next == None:
                break
            beg=beg.next    
            end=end.next.next    
        return beg
 
