class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area_max = 0
        n = len(heights)

        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx,val = stack.pop()
                width = i-idx
                area_max = max(area_max, val*width)
                start = idx
            
            stack.append((start, heights[i]))
        
    
        while stack:
            idx,val = stack.pop()
            width = n-idx
            area_max = max(area_max, val*width)
        
        return area_max


# [2,1,5,6,2,3], n = 6
#  stack = [(0,1),(2,5),(3,2),()]  
#  area = 6


        