# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        
        dummy=ListNode(0,head)
        after=dummy.next
        arrsmall=[]
        arrlarge=[]
        while head:
            if head.val < x:
                arrsmall.append(head.val)
            else:
                arrlarge.append(head.val)
            head=head.next
        arrsmall=arrsmall[::-1]
        print(arrsmall)
        arrlarge=arrlarge[::-1]
        print(arrlarge)
        
        while len(arrsmall)>0:
            after.val=arrsmall.pop()
            after=after.next
        while len(arrlarge)>0:
            after.val=arrlarge.pop()
            
            after=after.next
        return dummy.next   
                
        
        