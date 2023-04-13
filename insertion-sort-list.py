# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        # arr.sort()

        for i in range(len(arr)):
            j=i
            while j>=1 and arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
        print(arr)        

        dummy=ListNode()
        newhead=dummy
        i=0
        while i<len(arr):
            newhead.next=ListNode(arr[i])  
            newhead=newhead.next
            i+=1
            
        return dummy.next