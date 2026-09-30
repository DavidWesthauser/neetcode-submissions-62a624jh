class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = set()
        for n in nums:
            if n not in list:
                list.add(n)
            else:
                return True
        return False