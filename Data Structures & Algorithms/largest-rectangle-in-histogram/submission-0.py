class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx,top = stack.pop()
                width = i - idx
                max_area = max(max_area, top*width)
                start = idx

            stack.append((start,heights[i]))
            
        n = len(heights)
        while stack:
            idx,top = stack.pop()
            width = n-idx
            max_area = max(max_area, top*width)
            
        return max_area


# heights = [7,1,7,2,2,4]
# stack = [(0,1)]
# max_area = 7