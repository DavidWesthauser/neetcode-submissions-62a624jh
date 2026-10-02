class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsInS = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in charsInS:
                charsInS[char]= charsInS[char]+1
            else:
                charsInS[char]=1
        
        for char in t:
            if char in charsInS:
                charsInS[char]=charsInS[char]-1
                if charsInS[char] < 1:
                    charsInS.pop(char)
            else:
                return False
        return True
            