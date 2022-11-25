"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        current=head
        mapping={}
        
        while current:
            mapping[current]=Node(current.val)
            
            current=current.next
        
        for  node in mapping:
            if node.next:
                mapping[node].next=mapping[node.next]
            if node.random:
                mapping[node].random=mapping[node.random]
        
            
        return mapping[head]   
        
       
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        