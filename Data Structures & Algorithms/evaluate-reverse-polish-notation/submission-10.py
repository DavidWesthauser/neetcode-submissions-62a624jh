class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p = 0  # Write pointer
        
        for t in tokens:
            if t == '+':
                tokens[p-2] += tokens[p-1]
                p -= 1
            elif t == '-':
                tokens[p-2] -= tokens[p-1]
                p -= 1
            elif t == '*':
                tokens[p-2] *= tokens[p-1]
                p -= 1
            elif t == '/':
                tokens[p-2] = int(tokens[p-2] / tokens[p-1])
                p -= 1
            else:
                tokens[p] = int(t)
                p += 1
                
        return tokens[0]