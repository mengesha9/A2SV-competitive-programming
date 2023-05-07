# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for li in lists:
            while li:
                heap.append(li.val)
                li = li.next
        heapq.heapify(heap)

        head = newlist = ListNode(0)
        while heap:
            node = heapq.heappop(heap)
            newlist.next = ListNode(node)
            newlist = newlist.next 
        return head.next