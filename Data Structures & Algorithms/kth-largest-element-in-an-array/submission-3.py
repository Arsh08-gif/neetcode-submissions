import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       max_heap = [-x for x in nums]
       heapq.heapify(max_heap)
    #    print(max_heap)
       temp = 0
       while temp <= k-1:
        ans = -heapq.heappop(max_heap)
        if temp == k-1:
            return ans
        temp += 1

            
        
        