class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = self.quicksort(0, len(nums)-1, nums)
        return res[-k]

    def quicksort(self, s, e, arr):
        if s >= e:
            return arr

        pivot = arr[e]

        l = s
        r = s
        while r < e:
            if arr[r] < pivot:
                arr[r], arr[l] = arr[l], arr[r]
                l += 1
            r += 1    
        arr[e], arr[l] = arr[l], pivot

        self.quicksort(s, l-1, arr)
        self.quicksort(l+1, e, arr)

        return arr



      




