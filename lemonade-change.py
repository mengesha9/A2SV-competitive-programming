class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        totalfive = 0
        totalten = 0
      
        i = 0
        while i < len(bills):

            if bills[i] == 5 :
                totalfive += 1

            if bills[i] == 10:
                if totalfive >0:
                    totalten += 1
                    totalfive -= 1
                else:
                    return False     

            if bills[i] == 20 :
                if totalten > 0 and totalfive > 0 :
                     totalten -= 1
                     totalfive -= 1
                elif totalfive > 2:
                    totalfive -= 3
                else:
                    return  False
            i += 1

        
        return True