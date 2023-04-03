class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team = set()
        product = 0
        i = 0
        j = len(skill)-1
        while i<j:
            total = skill[j] + skill[i]
            team.add(total)
            product += skill[i]*skill[j]
            i += 1
            j -= 1
        if len(team) == 1:
            return product
        return -1        

