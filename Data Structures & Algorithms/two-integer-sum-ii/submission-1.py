class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        st = 0
        end = n-1
        res = []
        while(st < end):
            sum = numbers[st] + numbers[end]
            if sum > target:
                end -= 1 
            elif sum < target:
                st += 1
            else:
                res.append(st+1)
                res.append(end+1)
                return res
        
        return res

# numbers=[2,3,4]
#  t = 6
        