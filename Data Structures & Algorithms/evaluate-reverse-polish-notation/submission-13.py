class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+": stack.append(n2 + n1)
                elif t == "-": stack.append(n2 - n1)
                elif t == "*": stack.append(n2 * n1)
                elif t == "/": stack.append(int(n2 / n1))
                
        return stack[0]