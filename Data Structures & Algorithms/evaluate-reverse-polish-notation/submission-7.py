class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        top = 0  # Points to the next available spot in our in-place "stack"
        
        for t in tokens:
            if t not in operators:
                tokens[top] = int(t)
                top += 1
            else:
                # The last two numbers are right behind our 'top' pointer
                n1 = tokens[top - 1]
                n2 = tokens[top - 2]
                
                # Overwrite the older number (n2) with the new result
                if t == "+": tokens[top - 2] = n2 + n1
                elif t == "-": tokens[top - 2] = n2 - n1
                elif t == "*": tokens[top - 2] = n2 * n1
                elif t == "/": tokens[top - 2] = int(n2 / n1)
                
                # Shrink the "stack" size by 1 (2 elements merged into 1)
                top -= 1
                
        # The final result is the only remaining element at index 0
        return tokens[0]