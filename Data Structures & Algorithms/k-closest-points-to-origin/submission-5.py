import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = [(x*x+y*y,[x,y]) for x,y in points]
        heapq.heapify(heap)
        # print(heap)
        temp = k
        while temp > 0:
            dist,point = heapq.heappop(heap)
            ans.append(point)
            temp -= 1
        # print(ans)
        return ans


        