# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dic={}
        prev=None
        while head:
            prev=head
            if head in dic:
                return prev
            else:
                dic[head]=True  
            head=head.next   
        return None