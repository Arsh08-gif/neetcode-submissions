class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        n = len(piles)
        start = 1
        end = m
        min_k = m
        while (start <= end):
            k = (start+end)//2
            total_hrs = 0
            for i in range(n):
                # total_hrs += math.ceil((piles[i] + k - 1) // k)
                # total_hrs += math.ceil((piles[i]) // k) this will give wrong ans
                # total_hrs += -(-piles[i] // k)
                total_hrs += math.ceil((piles[i]) / k)
            
            if total_hrs <= h : 
                min_k = k
                end = k-1
            else : start = k+1
        
        return min_k
    
# [1,4,3,2], h = 9
# m = 4, n = 4
# 1 ---> 4, k=2, min_k = 2