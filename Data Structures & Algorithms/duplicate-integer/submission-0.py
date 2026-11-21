class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set([])

        for num in nums:
            if uniq and num in uniq : return True
            uniq.add(num)
        
        return False



# []
# 