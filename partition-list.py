# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smaller = ListNode(0)
        greater = ListNode(0)
        dumy = smaller
        dummygre = greater 
        while head:
            if head.val < x:
                smaller.next = ListNode(head.val)
                smaller = smaller.next 
            
            else:
                greater.next = ListNode(head.val)
                greater = greater.next   
            head = head.next  

        smaller.next = dummygre.next 

        return dumy.next