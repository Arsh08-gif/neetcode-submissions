class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        ans = []
        while (start < end):
            idx_sum = numbers[start] + numbers[end]
            if idx_sum == target: 
                ans.append(start + 1)
                ans.append(end + 1)
                return ans
            
            elif idx_sum > target:
                end -= 1
            else: start += 1

        return ans


        