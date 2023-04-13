# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

       
        dummy=head=ListNode(0)
        carry=0
        while l1 and l2:
            total=l1.val+l2.val+carry
            carry=total//10
            res=total%10
            head.next=ListNode(res)
            l1=l1.next
            l2=l2.next
            head=head.next
        while l1:
            total=l1.val+carry
            carry=total//10
            res=total%10
            head.next=ListNode(res)
            l1=l1.next
            head=head.next
        while l2:
            total=l2.val+carry
            carry=total//10
            res=total%10
            head.next=ListNode(res)
            l2=l2.next
            head=head.next

        if carry!=0:
            head.next=ListNode(carry)
            head=head.next

        return dummy.next