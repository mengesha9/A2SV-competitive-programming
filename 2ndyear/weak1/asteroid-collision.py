class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        res = []
        for i in range(len(asteroids)):
            if res and asteroids[i] < 0:
                while res and res[-1] > 0 and abs(res[-1]) < abs(asteroids[i]):
                    res.pop()
                if res and (abs(asteroids[i] ) == abs(res[-1]) and res[-1] > 0):
                    res.pop()
                    continue
                elif len(res) == 0  or res[-1] < 0:
                    res.append(asteroids[i])
            if len(res) == 0 or asteroids[i] > 0:
                res.append(asteroids[i])

        return res         







        