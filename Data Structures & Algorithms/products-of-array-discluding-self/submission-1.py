class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        # print(prefix)
        # print(suffix)
        # prefix : [1,1,2,8]
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1]*prefix[i-1]
        # print(prefix)
        # suffix : [1,6,24,48]
        for j in range(len(nums)-2, -1, -1):
            # suffix[len(nums)-j-1] = nums[j+1]*suffix[len(nums)-j-2]
            suffix[j] = nums[j+1]*suffix[j+1]
        # print(suffix)
        for k in range(len(nums)):
            nums[k] = prefix[k]*suffix[k]
        return nums



# 4 --> j = 2 , s(1 --- n-j-1)