class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = set()
        for n in nums:
            if n in list:
                return True
            list.add(n)
        return False