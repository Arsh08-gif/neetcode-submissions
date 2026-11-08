class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            token_num = 0
            if len(token) > 1:
                token_num = int(token)
                stack.append(token_num)
            
            elif token.isdigit():
                token_num = int(token)
                stack.append(token_num)
            else : 
                b = stack.pop()
                a = stack.pop()
                # print(token)
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    q = abs(a) // abs(b)
                    q = -q if (a < 0) != (b < 0) else q
                    stack.append(q)
            # print(stack)
        return stack[0]




