class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        max_len = 1
        curr_len = 1

        nums = sorted(set(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                curr_len += 1
            else : curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len


        
# [2,20,4,10,3,4,5] --> [2,3,4,5,10,20]
# [0,3,2,5,4,6,1,1] --> [0,1,2,3,4,5,6]

