import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []
        for point in points:
            x,y = point
            dist = x*x + y*y
            heapq.heappush(heap, (-dist,point))
            while len(heap) > k:
                heapq.heappop(heap)
        return [pt for _, pt in heap]


        