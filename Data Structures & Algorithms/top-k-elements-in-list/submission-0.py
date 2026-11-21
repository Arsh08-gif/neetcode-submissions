class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        ans = []
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        freq_map = dict(sorted(freq_map.items(), key=lambda item:item[1], reverse=True))

        i = 0
        for key in freq_map:
            ans.append(key)
            i+=1
            if i==k:break
        
        return ans

# [1,2,2,3,3,3] k = 3
# [3:3,2:2,1:1]

