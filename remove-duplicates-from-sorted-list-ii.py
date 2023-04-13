# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        tmp = head 
        dic = defaultdict(int)
        while tmp:
            dic[tmp.val] += 1
            tmp = tmp.next 

 
        curr = head
        prev = head
        dummy = prev = ListNode(0)   

        while curr:
            if dic[curr.val]==1:
                prev.next  = ListNode(curr.val)
                prev = prev .next 
            curr = curr.next    
        return dummy.next