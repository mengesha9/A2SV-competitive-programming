class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()

        arr[0] = 1
        max_ = 1

        for i in range(1,len(arr)):
            if max_ + 1 == arr[i]:
                max_ = arr[i]
            if max_ + 1 < arr[i]:
                arr[i]= max_ + 1
                max_ = arr[i]
        return max_