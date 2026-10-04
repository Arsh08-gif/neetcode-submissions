class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        reverse_stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if reverse_stack:
                val,idx = reverse_stack[-1]
                while val < temperatures[i]:
                    ans[idx] = i-idx
                    reverse_stack.pop()
                    if reverse_stack:val,idx = reverse_stack[-1]
                    else : break
            
            reverse_stack.append((temperatures[i],i))
        
        while reverse_stack:
            val,idx = reverse_stack.pop()
            ans[idx] = 0 
            

        return ans
        