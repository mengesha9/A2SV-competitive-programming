class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:

        num = [instructions[0]]
        cost = 0

        for i in range(1,len(instructions)):

            idr = bisect_right(num,instructions[i])
            idl = bisect_left(num,instructions[i])
            
            
            cost += min(idl,len(num)-idr)
            # print("{}{}{}".format(cost,idl,idr))
            bisect.insort(num, instructions[i])

        return cost % (10**9 + 7)