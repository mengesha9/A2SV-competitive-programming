# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        ans=[]
        for i in range((len(arr)//2)+1) :
            if len(arr)-2*i>2:
                ans.append(arr[i])
                ans.append(arr[len(arr)-i-1])
            else:
                ans.append(arr[i])
        i=0
        while head and i<len(ans):
            head.val=ans[i]
            head=head.next
            i+=1

        print(ans)            
                   
