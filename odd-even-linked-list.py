# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head 

        dummeven = even = ListNode(0)
        dummodd = odd = ListNode(0)
        count = 1
        while head:
            if count % 2 == 0:
                even.next = ListNode(head.val)
                even  = even.next 
            else:
                odd.next = ListNode(head.val)
                odd = odd.next 
            head = head.next 
            count += 1
        odd.next = dummeven.next

        return dummodd.next