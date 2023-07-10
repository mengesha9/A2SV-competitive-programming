class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def find_permutation(nums, perm, index, count):
            if count == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if (index & (1 << i)) == 0:
                    index |= (1 << i)
                    perm[i] = nums[count]
                    find_permutation(nums, perm, index, count + 1)
                    index &= ~(1 << i)
        
        find_permutation(nums, [None] * len(nums), 0, 0)
        return res