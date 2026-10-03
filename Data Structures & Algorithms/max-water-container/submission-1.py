class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_dim = 0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         width = j-i
        #         height = min(heights[j],heights[i])
        #         dim = width * height
        #         max_dim = max(max_dim, dim)

        l = 0
        r = n-1
        while(l<r):
            width = r-l
            height = min(heights[l],heights[r])
            dim = width * height
            max_dim = max(max_dim, dim)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else :
                if heights[l+1] > heights[r-1]:
                    l+=1
                elif heights[l+1] < heights[r-1]:
                    r-=1
                else:
                    l+=1
                    r-=1
                    
        return max_dim
                
        