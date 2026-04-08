class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        last_num = None
        nums.sort()

        for num in nums:
            if last_num == num:
                output = True
                break
            last_num = num

        return output
                
            