class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start = image[sr][sc]
        def dfs(r,c):

            if  min(r,c) < 0 or r == len(image) or c == len(image[0]) or  start != image[r][c] or image[r][c] == color :
                return 

            image[r][c] = color
            dfs(r+1,c)  
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)
        return image      



