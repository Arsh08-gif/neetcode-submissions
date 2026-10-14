class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0]*n
        suffix_max = [0]*n
        pre_max = height[0]
        suff_max = height[n-1]
        for i in range(1,n):
            pre_max = max(pre_max, height[i-1])
            prefix_max[i] = pre_max
        for i in range(n-2,-1,-1):
            suff_max = max(suff_max, height[i+1])
            suffix_max[i] = suff_max
        
        total = 0
        for j in range(n):
            amount = min(prefix_max[j],suffix_max[j]) - height[j]
            if amount < 0 : continue
            total += amount
        
        return total



        