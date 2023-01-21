class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=nums[:]
        arr.sort()
        dic={}
        for i in range(len(arr)):
            if arr[i] not in  dic:
                dic[arr[i]]=i
        print(dic)  
        print(nums)

        for i in range(len(nums)):
            nums[i]=dic[nums[i]]
        return nums   
