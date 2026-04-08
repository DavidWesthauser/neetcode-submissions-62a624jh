class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4 3 2 1
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1