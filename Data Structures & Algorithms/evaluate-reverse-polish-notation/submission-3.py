class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+": stack.append(a+b)
                elif tokens[i] == "-": stack.append(a-b)
                elif tokens[i] == "*": stack.append(a*b)
                elif tokens[i] == "/": 
                    stack.append(int(a/b))
            else : stack.append(int(tokens[i]))
        
        return stack[0]



        

# ["1","2","+","3","*","4","-"]
# 
                

        