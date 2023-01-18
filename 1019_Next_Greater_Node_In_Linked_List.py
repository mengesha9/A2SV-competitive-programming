# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        stack=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next 
        ans=[0]*len(arr)
        i=0    
        while i<len(arr):
            
            while stack and stack[-1][0]<arr[i]:
                x,y=stack.pop()
                ans[y]=arr[i]
            stack.append([arr[i],i]) 
            ans[i]=0  
            i+=1   
        return ans   
