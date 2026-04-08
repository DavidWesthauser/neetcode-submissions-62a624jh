class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(n2 - n1)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(int(n2 / n1))
                case _:
                    stack.append(int(t))
                    
        return stack[0]