class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = False
        #true if s and t are anagrams: same characters but div order
        #just sort each string and compare if the same dough
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            output = True
        return output

