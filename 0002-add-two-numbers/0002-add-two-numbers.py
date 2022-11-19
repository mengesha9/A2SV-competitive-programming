# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        var=''
        var2=''
        while l1:
            var+=str(l1.val)
            l1=l1.next
        while l2:
            var2+=str(l2.val)
            l2=l2.next
        var=int(var[::-1])   
        var2=int(var2[::-1])
        solution=var+var2
        
        linkedlist=None
        
        for i in str(solution)[::-1]:
            if linkedlist==None:
                linkedlist=ListNode(int(i))
                head=linkedlist
            else:
                n1=ListNode(int(i))
                linkedlist.next=n1
                linkedlist=n1
        return head        
                
            
       
    
        
    
    
    
    
    
#         Definition for singly-linked list.
# class ListNode:
# def init(self, val=0, next=None):
# self.val = val
# self.next = next
# class Solution:
# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# head=l1
# count=""
# while head!=None:
# count+=str(head.val)
# head=head.next
# count=int(count[::-1])
# head=l2
# count1=""
# while head!=None:
# count1+=str(head.val)
# head=head.next
# count1=int(count1[::-1])

#     sol=count+count1
    
#     newList=None
#     for i in str(sol)[::-1]:
#         if newList ==None:
#             newList=ListNode(int(i))
#             head=newList
#         else:
#             n1=ListNode(int(i))
#             newList.next=n1
#             newList=n1
#     return head
            
        

            
        