class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:


        left = 1
        right = max(nums)-1
        best = 0
        while left <= right:

            mid = left + (right - left)//2

            if self.binary(nums, mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1 
            
        return left        

    def binary(self, arr, temp):

        result = 0

        for n in arr:
            result += math.ceil(n/temp)
        return result    


        