import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        max_heap = [-x for x in self.nums]
        heapq.heapify(max_heap)
        for i in range(1,self.k+1):
            ans = -heapq.heappop(max_heap)
            if i == self.k: return ans
        return -1
