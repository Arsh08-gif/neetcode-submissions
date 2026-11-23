import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        # print(max_heap)
        while(len(max_heap) > 1):
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x==y : continue
            y = x-y
            heapq.heappush(max_heap, -y)
            # print(max_heap)
        return -max_heap[0] if max_heap else 0



            




# [2, 7, 6, 6]
# []