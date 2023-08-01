class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        i = 1
        length = 1

        while i <= query_row:
            newarray = [0.0] * (length + 1)
            flag = False
            for j in range(length):
                if curr[j]>1:
                    newarray[j] += (curr[j] - 1) / 2.0
                    newarray[j + 1] += (curr[j] - 1) / 2.0
           
            i += 1
            curr = newarray
            length += 1

        return min(curr[query_glass], 1.00)