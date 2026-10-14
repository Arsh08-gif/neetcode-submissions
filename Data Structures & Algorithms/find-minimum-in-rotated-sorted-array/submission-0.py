class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        min_item = float("inf")
        
        def recursion(start:int,end:int,min_item:int,nums:List[int]):
            if start == end :
                return min(min_item, nums[start])
            if start > end : return min_item
            pivot = (start + end) // 2
            min_item = min(min_item, nums[pivot])
            left_recurse = recursion(start, pivot-1, min_item, nums)
            right_recurse = recursion(pivot+1, end, min_item, nums)
            return min(min_item, left_recurse, right_recurse)
        
        min_item = recursion(start,end,min_item,nums)
        return min_item




# [3,4,5,6,1,2]
# [1,2,3,4,5,6]