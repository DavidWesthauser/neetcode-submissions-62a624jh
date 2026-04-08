class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            try:
                # Most tokens are numbers. 
                # Jumping straight to int() is faster than if-checking strings.
                stack.append(int(t))
            except ValueError:
                # If int(t) fails, it's an operator
                n1 = stack.pop()
                n2 = stack.pop()
                if t == '+':
                    stack.append(n2 + n1)
                elif t == '-':
                    stack.append(n2 - n1)
                elif t == '*':
                    stack.append(n2 * n1)
                else:
                    # Using int(n2/n1) is faster than floor division // for negative numbers
                    stack.append(int(n2 / n1))
        return stack[0]