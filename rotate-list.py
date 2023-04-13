# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        curr = newarr = head  
        count = 0
        while newarr:
            count += 1
            newarr = newarr.next 
        dummy = ListNode(0)
        print(count )
        reorder = k % count 
        while reorder>0:

            dummy.next = curr 
            tmp = dummy
            prev = curr 
            while  prev.next :
                prev = prev.next 
                tmp = tmp.next 
            tmp .next = None
            prev.next = dummy.next
            curr = prev 
            
            reorder -= 1
        return curr