# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr=[]
        dummy=ListNode(0,head)
        after=dummy.next
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()  
        arr=arr[::-1]
        
        while len(arr) >0:
            after.val=arr.pop()
            after=after.next
        return dummy.next