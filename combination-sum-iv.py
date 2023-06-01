class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:


        hashmap = defaultdict(int)

        def dp(amount):
            if amount < 0:
                return 0
            if amount == 0:
                return 1

            if amount not in hashmap:
                for i in nums:

                    hashmap[amount] +=  dp(amount-i)

            return hashmap[amount]  

        return dp(target)