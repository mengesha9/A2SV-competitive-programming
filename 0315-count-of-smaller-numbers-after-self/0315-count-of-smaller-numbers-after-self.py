class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        temp = []
        for i in range(len(nums)):
            temp.append([nums[i],i])

        self.count = [0] * len(nums)
        self.mergesort(temp, 0, len(nums)-1)
        
        return self.count    

    def mergesort(self,arr,s,e):

            if s == e:
                return [arr[s]]

            mid = s + (e -s)//2
            left =  self.mergesort(arr,s,mid )
            right = self.mergesort(arr, mid+1, e)

            i = j = 0
            while i < len(left):
                while j < len(right) and left[i][0] > right[j][0]:
                    j += 1
                self.count[left[i][1]] += j
                i += 1

            l = r = 0
            arr = []
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
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
                          










         
   