class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            costs[i] = [-costs[i][0]+costs[i][1],costs[i][0],costs[i][1]]
        costs.sort() 
        total = 0
        for i in range(len(costs)): 
            if i < len(costs)//2:
                total += costs[i][2]
            else:
                total += costs[i][1]    

        return total   






        

                 

        
