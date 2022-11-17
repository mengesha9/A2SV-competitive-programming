class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        right = []
        left = []
        
        stack = []
        
        for i in range(len(heights)):
            cur = heights[i]
            
            while stack and cur <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                left.append(stack[-1])
            
            else:
                left.append(-1)
            
            stack.append(i)
        
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            cur = heights[i]
            
            while stack and cur <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                right.append(stack[-1])
            
            else:
                right.append(len(heights))
            stack.append(i)
        
        result = 0
        right = right[::-1]
        print(right, left)
        for i in range(len(heights)):
            cur = heights[i]
            temp_area = (right[i] - left[i] - 1) * cur
            
            result = max(result, temp_area)
        
        return result
        