import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = [0]*26
        for task in tasks:
            ch_int = ord(task) - ord("A")
            freq_count[ch_int] += 1
        
        max_heap = [-f for f in freq_count if f > 0]
        heapq.heapify(max_heap)
        q = []
        
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                freq = heapq.heappop(max_heap) + 1
                if freq != 0:
                    q.append((freq, time+n))
             
            if q and q[0][1] <= time : 
                heapq.heappush(max_heap, q.pop(0)[0])
        
        return time



        