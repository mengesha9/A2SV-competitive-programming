class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if sum(people) <= limit:
            return 1

        people.sort()
        l , r = 0,len(people)-1
        count = 0
        while l<=r:
            remain = limit - people[r]

            if remain >= people[l]:
                l += 1
            r -= 1
            count += 1    

        return count