class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []

        # for i in range(n-2):
        #     if i > 0 and nums[i] == nums[i-1]:continue
        #     for j in range(i+1,n-1):
        #         if j > i+1 and nums[j] == nums[j-1]:continue
        #         for k in range(j+1,n):
        #             if k > j+1 and nums[k] == nums[k-1]: continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.append([nums[i],nums[j],nums[k]])

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1] : continue
            st = i+1
            end = n-1
            while(st<end):
                sum = nums[i] + nums[st] + nums[end]
                if  sum > 0:
                    end -= 1
                elif sum < 0:
                    st += 1
                else :
                    res.append([nums[i],nums[st],nums[end]])
                    end -= 1
                    while(nums[end] == nums[end+1] and end>st):
                        end -= 1
        return res

    # [-2,0,1,1,2]
        