class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        # while(start <= end):
        #     mid = (start + end)//2
        #     if nums[mid] == target : return mid
        #     elif nums[mid] < target:
        #         start = mid+1
        #     else : end = mid-1
        
        ans = self.bin_recursion(start,end,nums, target)
        return ans

    
    def bin_recursion(self,start,end,nums, target):
        if start >= end: 
            if nums[start] == target: return start
            else : return -1
        
        mid = (start + end) // 2
        ans = 0
        if nums[mid] == target : return mid
        elif nums[mid] > target : ans =  self.bin_recursion(start,mid-1,nums,target)
        else: ans = self.bin_recursion(mid+1,end,nums,target)
        return ans

# [-1,0,2,4,6,8]
# target = 4
        