class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles) # O(nlogn)
        start = 1
        end = piles[len(piles) - 1]
        # min_k = float('inf')
        while(start <= end):
            k = (start + end) // 2
            total_hrs = 0
            for i in range(len(piles)):
                total_hrs += math.ceil(piles[i] / k)
            if total_hrs <= h:
                # min_k = k
                end = k - 1
            else : start = k + 1
        # return min_k
        return start


# [1,2,3,4]
# [4,10,23,25]