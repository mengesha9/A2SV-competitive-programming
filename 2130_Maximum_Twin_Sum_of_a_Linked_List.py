# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        arr=[]
        
        while head:
            arr.append(head.val)
            head=head.next
        print(arr) 

        i=0
        total=0
        n=len(arr)
        while i<(n//2):
            if 0<=i<=((n/2)-1):
                total=max(total,arr[i]+arr[n-1-i])
            i+=1
        return total 
