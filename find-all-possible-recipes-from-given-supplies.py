class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:


        adjlist = defaultdict(list)
        sup = set(recipes)
        indgree = defaultdict(int)

        for i in range(len(recipes)):

            indgree[recipes[i]] = len(ingredients[i])
            for ing in ingredients[i]:
                adjlist[ing].append(recipes[i])
  
        q = deque(supplies)
        ans = []
        while q:
            s= q.popleft()
            if s in sup:
                ans .append(s)


            for r in adjlist[s]:
                indgree[r]-=1
                if indgree[r]==0:
                    q.append(r)
                   

        return ans