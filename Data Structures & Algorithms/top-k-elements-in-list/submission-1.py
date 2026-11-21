class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        ans = []
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        # freq_map = dict(sorted(freq_map.items(), key=lambda item:item[1], reverse=True))
        bucket = [[] for _ in range(len(nums)+1)]
        for num,count in freq_map.items():
            bucket[count].append(num)

        i = 0
        for j in range(len(bucket)-1, -1, -1):
            for num in bucket[j]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        

# [1,2,2,3,3,3] k = 3
# [3:3,2:2,1:1]

