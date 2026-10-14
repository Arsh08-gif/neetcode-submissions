class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        # min_item = float("inf")
        min_item = nums[0]
        
        # APPROACH - 1
        # def recursion(start:int,end:int,min_item:int,nums:List[int]):
        #     if start == end :
        #         return min(min_item, nums[start])
        #     if start > end : return min_item
        #     pivot = (start + end) // 2
        #     min_item = min(min_item, nums[pivot])
        #     left_recurse = recursion(start, pivot-1, min_item, nums)
        #     right_recurse = recursion(pivot+1, end, min_item, nums)
        #     return min(min_item, left_recurse, right_recurse)
        
        # min_item = recursion(start,end,min_item,nums)

        # APPROACH - 2
        while start <= end:
            if start == end : 
                return min(min_item, nums[start])
            mid = (start + end) // 2
            min_item = min(min_item, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else : end = mid

        return min_item

# [2, 1]
# [3,4,5,6,1,2]
# [1,2,3,4,5,6]




