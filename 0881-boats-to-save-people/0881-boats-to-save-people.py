class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        people.sort()
        numBoats=0
        start=0
        end=len(people)-1
        while start<=end:
            
            if people[start]+people[end]<=limit:
                start+=1
            numBoats+=1
            end-=1
        return numBoats     
        