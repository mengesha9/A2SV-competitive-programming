class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:


        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])



        arr = [1]*n 

        def dfs(value,new):
            if new not in dic:
                return 
            
            for k in dic[new]:
                if labels[k] == labels[value] :
                    arr[value] += 1
               
                dfs(value,k)
                     
                      

        for k , v in dic.items():
            dfs(k,k)
           

        return arr    
