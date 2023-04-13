# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        arr=[]
        fast =head
        slow=head
        count=0
        while fast and  fast.next:
            count+=1
            arr.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        total=0
        while arr and slow:
            total=max(slow.val+arr[-1],total)
            slow=slow.next
            arr.pop()
        return total    


          
            
            
        print(arr)