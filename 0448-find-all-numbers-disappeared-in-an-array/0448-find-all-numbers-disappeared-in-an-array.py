class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:


        i = 0
        arr = []
        freq = defaultdict(int)
        while i < len(nums):
            if nums[i] != i+1:
                postion = nums[i] - 1
                if nums[postion] == nums[i]:
                    if nums[i] not in freq:
                        arr.append(nums[i])
                        freq[nums[i]] += 1
                    i += 1
                else:
                    nums[postion] , nums[i] = nums[i],nums[postion]
            else:
                i += 1

        answer = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                answer.append(i+1)
        return answer        





        