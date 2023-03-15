class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        return self.predict(0, 0, 0, len(self.nums)-1, 1)
    def predict(self,  score2, score1, l, r, turn):
        if l > r:
            return score1 >= score2
        if turn :
            return self.predict(score2, score1 + self.nums[l], l+1, r, 1-turn)  or self.predict(score2,score1 + self.nums[r], l, r-1, 1-turn)  
        else:
            return   self.predict(score2 + self.nums[l], score1, l+1, r, 1-turn) and self.predict(score2 + self.nums[r], score1, l, r-1, 1-turn)

    




