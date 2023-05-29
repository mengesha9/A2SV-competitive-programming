class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        hashmap = defaultdict(int)

        coins.sort(reverse = True)

        def back(a):
            if a < 0 :
                return float("inf")
            
            if a == 0:
                return  0
            
            if a not in hashmap:
                count = float("inf")
                for c in coins:
                
                    count = min( count, 1 + back(a-c))
                
                hashmap[a] =  count 
             
            return hashmap[a]    
        
        tmp = back(amount)
        if tmp == float('inf'):
            return -1 

        return tmp