class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        ans = []
        for i,num in enumerate(nums):
            idx_map[num] = i
        
        for i,num in enumerate(nums):
            b = target - num
            if b in idx_map:
                idx = idx_map[b]
                if idx > i : 
                    ans.append(i)
                    ans.append(idx)
                    return ans
                elif idx < i :
                    ans.append(idx)
                    ans.append(i)
                    return ans
                else : continue
        
        return ans



# [-3,-3] t = -6
# -6+3 = -3