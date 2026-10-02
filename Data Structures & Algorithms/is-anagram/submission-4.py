class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if len(s) != len(t):
            return False

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for char in t:
            if char in counts:
                counts[char]=counts[char]-1
                if counts[char] == 0:
                    counts.pop(char)
            else:
                return False
        return True
            