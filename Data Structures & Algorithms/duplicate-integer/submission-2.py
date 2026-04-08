class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        last_num = None
        nums.sort()

        for num in nums:
            if last_num == num:
                return True
            last_num = num

        return False
                
            