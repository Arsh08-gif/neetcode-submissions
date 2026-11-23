import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euc_map = {}
        ans = []
        for point in points:
            x,y = point
            a = x*x
            b = y*y
            dist = math.sqrt(a+b)
            euc_map[(x,y)] = dist
        # print(euc_map)
        euc_dist = list(euc_map.values())
        # print(euc_dist)
        heapq.heapify(euc_dist)
        # print(euc_dist)

        temp = k
        k_dist = []
        while(temp > 0):
            min_dist = heapq.heappop(euc_dist)
            k_dist.append(min_dist)
            temp -= 1
        # print(k_dist)

        # for key, val in list(euc_map.items()):   
        #     for dist in k_dist:
        #         if dist == val:
        #             euc_map.pop(key)
        #             ans.append(key)              
        #             break   

        for key, val in euc_map.items():
            if val in k_dist:
                ans.append(key)                     
        
        return ans


        