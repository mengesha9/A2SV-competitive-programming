class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        for i in range(len(nums1)):
            nums1[i] = nums1[i]-nums2[i]
        self.diff = diff    
        self.count = 0
        self.merge(nums1, 0, len(nums1)-1)
        return self.count 
    def merge(self, arr, s, e):
        if s == e:
            return [arr[s]]
        mid = s + (e-s)//2
        left  = self.merge(arr, s, mid)
        right = self.merge(arr,mid+1,e)
        
        i = j = 0
        while  i < len(right):
            while  j < len(left) and right[i] + self.diff >= left[j] :
                j += 1
            self.count += j
            i += 1

        l = r = 0
        arr = []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])  
                r += 1

        while l < len(left):
            arr.append(left[l])
            l += 1


        while r < len(right):
            arr.append(right[r])
            r += 1


        return arr                   





    
        