class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        sum=0
        arr=[]
        for i in range(len(nums)):
            sum+=nums[i]
            arr.append(sum)
        print(arr)
        return arr    