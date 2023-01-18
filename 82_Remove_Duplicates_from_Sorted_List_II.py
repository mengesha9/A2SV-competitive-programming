# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr={}
        curr=head
        while curr:
            if curr.val not in arr:
                arr[curr.val]=1
            else:
                arr[curr.val]+=1  
            curr=curr.next
            
        prev=ListNode()
        curr=prev
        while head:
            if arr[head.val]==1:
                curr.next=ListNode(head.val)
                curr=curr.next
            head=head.next          
        return prev.next  
