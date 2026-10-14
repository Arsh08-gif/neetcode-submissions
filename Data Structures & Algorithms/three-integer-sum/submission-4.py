class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            while(j < k):
                two_sum = nums[j] + nums[k]
                total = nums[i] + two_sum
                if total == 0 : 
                    triplet = ([nums[i],nums[j], nums[k]])
                    if triplet not in ans:
                        ans.append([nums[i],nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif total > 0 :
                    k -= 1
                else : j += 1
        
        return ans



            
