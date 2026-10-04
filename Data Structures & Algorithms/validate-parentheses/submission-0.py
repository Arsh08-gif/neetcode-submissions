class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       for i in range(len(s)):
        if s[i] == "[" or s[i] == "{" or s[i] == "(":
            stack.append(s[i])
        if s[i] == "]" :
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
            
        if s[i] == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if s[i] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
       
       return True if not stack else False
        
    
        