class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        # print(nums)
        for i in range(k+1):
            if i == k-1:
                return nums[i]
            
        
        