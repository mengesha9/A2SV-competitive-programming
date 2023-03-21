# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return 
        if not head.next:
            return head
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(temp)

        newNode  = ListNode(0)
        curr = newNode

        while left and right:
            if left.val <= right.val:
                newNode.next = ListNode(left.val)
                left = left.next
            else:
                newNode.next = ListNode(right.val)
                right = right.next
            newNode = newNode.next
        
        if left :
            newNode.next = left
        if right:
            newNode.next = right 


        return curr.next            





        
        
