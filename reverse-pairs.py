class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergeSort(0, len(nums)-1, nums)
        return self.count 
    def mergeSort(self, s, e, arr):

        if s == e:
            return [arr[s]] 

        mid = s + (e-s)//2  

        left = self.mergeSort(s, mid, arr)
        right = self.mergeSort(mid + 1, e, arr)
        
        


        
        j = i = 0
        while i < len(left) :

            while j < len(right) and left[i] > 2*right[j]:
                j += 1
            self.count += j          
            i += 1   
       
            
            
        arr = []
        i = j = 0

        while i< len(left) and j < len(right):
            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1

        while i < len(left):
            arr.append(left[i])
            i += 1

        while j < len(right):
            arr.append(right[j])
            j += 1


        return arr