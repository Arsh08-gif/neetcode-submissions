class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        while (start < end):
            height = min(heights[start], heights[end])
            width = end - start
            area = height * width
            max_area = max(max_area, area)

            if heights[start] < heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else :
                if heights[start+1] < heights[end-1]:
                    end -= 1
                elif heights[start+1] > heights[end-1]:
                    start += 1
                else : start += 1
            
        return max_area
        