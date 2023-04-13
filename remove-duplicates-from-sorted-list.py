# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 

        dummy=ListNode(0)

        dummy.next = curr = ListNode(head.val)
        curr 
        tmp = head.next 
        while tmp:
            if tmp.val  != curr.val:
                curr.next=ListNode(tmp.val)
                curr=curr.next 
            tmp=tmp.next   
        return dummy.next