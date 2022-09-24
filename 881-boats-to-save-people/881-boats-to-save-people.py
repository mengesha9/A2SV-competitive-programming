class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
           
        boat=0
        l,r=0,len(people)-1
        while l<=r :
            remain=limit-people[r]
           
            if l <=r and remain>=people[l]:
                l+=1
            r-=1
            boat+=1    
        return boat  