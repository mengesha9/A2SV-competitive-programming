class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        

        
        nums.sort(key = cmp_to_key(self.compare))

        return str(int("".join(nums)))

    def compare(self, x, y):
            if x + y < y + x:
                return 1

            elif x + y > y + x:
                return -1
            
            return 0