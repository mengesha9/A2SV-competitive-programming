class Solution:
    def findComplement(self, num: int) -> int:

        q = collections.deque()
        k =0
        curr = num
        
        while num: 
            if num % 2 != 0:
                temp = 1
                curr -= 2 **(k) 
            else:
                temp  = 0  
                curr += 2**(k)  
            
            k += 1
            num = num >> 1
        return curr    
