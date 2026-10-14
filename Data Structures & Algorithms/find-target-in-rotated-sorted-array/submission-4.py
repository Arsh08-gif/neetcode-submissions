class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        first_idx = float("inf")
        min_val = float("inf")

        while(start <= end):
            if start == end: 
                if nums[start] < min_val:
                    min_val = nums[start]
                    first_idx = start
                break
            mid = (start + end) // 2
            if nums[mid] < min_val:
                min_val = nums[mid]
                first_idx = mid
            if nums[end] < nums[mid]:
                start = mid + 1
            else : end = mid
        
        start = 0
        end = n - 1
        k = first_idx
        while (start <= end):
            mid = (start + end) // 2
            real = (mid + k) % n
            if nums[real] == target : return real
            if nums[real] > target : 
                end = mid - 1
            else : start = mid + 1
        
        return -1



    
# [3,4,5,6,1,2], 1
# [1,2,3,4,5,6]
        