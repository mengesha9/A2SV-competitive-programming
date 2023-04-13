# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        arr=[]
        while head:
            arr.append(head.val) 
            head=head.next
        
        if len(arr)%2==0:
            i=math.ceil(len(arr)/2)
        else:
            i=len(arr)//2  

        dummy=curr=ListNode(0)
        while i<len(arr):
            curr.next=ListNode(arr[i])
            curr=curr.next
            i+=1
        return dummy.next