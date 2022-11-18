# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
            
        arr=arr[::-1]  
        sum=0
        for i in range(len(arr)):
            sum+=(pow(2,i))*arr[i]
        return sum    
        
        
        