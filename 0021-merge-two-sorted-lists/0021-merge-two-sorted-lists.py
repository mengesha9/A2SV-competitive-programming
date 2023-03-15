# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        return self.merge(list1, list2)

    def merge(self, node1, node2):
        if not node1 and not node2:
            return 
        if not node1 :
            return node2
        if not node2: 
            return node1
        if node1.val <= node2.val:
            temp = node1
            temp.next = self.merge(node1.next, node2)
            return temp
        elif node1.val > node2.val:
            temp = node2
            temp.next = self.merge(node1, node2.next)
            return temp
            





             


        
      