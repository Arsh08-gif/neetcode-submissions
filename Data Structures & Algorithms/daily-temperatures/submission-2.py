class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            # print(i)
            while stack and temperatures[stack[-1]] < temp:
                ans = i -  stack[-1]
                # print(ans)
                result[stack[-1]] = ans
                stack.pop()
            stack.append(i)
            # print(stack)
        
        while stack:
            result[stack[-1]] = 0
            stack.pop()
        return result
                
                
# [0,]