# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        curr  =  dummy
        
        count = 1
        arr = []

        while  head :
            
            if count < left:
                curr.next = ListNode(head.val)
                curr = curr.next

            if left <= count <= right:
                arr.append(head.val)
            count += 1
            head = head.next
            if count > right:
                break
        
        while arr:
            curr.next = ListNode(arr.pop())
            curr = curr.next

        curr.next= head

        return dummy.next